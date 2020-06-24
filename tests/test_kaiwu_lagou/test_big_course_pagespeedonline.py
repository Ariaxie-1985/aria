# coding:utf-8
# @Time  : 2020/6/24 12:16
# @Author: Xiawang
# Description:
import json
import os
import re

import pytest

content = ''
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Upgrade-Insecure-Requests': '1'}
import requests


def get_pagespeed_api_key():
    url = 'https://developers.google.com/speed/pagespeed/insights/'
    result = requests.get(url=url, headers=headers, verify=False)
    assert result.status_code == 200
    global pagespeed_api_key
    pagespeed_api_key = re.findall(r"PAGESPEED_API_KEY='(.*?)';", result.text)[0]
    return pagespeed_api_key


@pytest.mark.flaky(reruns=2, reruns_delay=10)
@pytest.mark.parametrize('big_course_url', [('https://kaiwu.lagou.com/java_basic.html'),
                                            ('https://kaiwu.lagou.com/java_architect.html'),
                                            ('https://kaiwu.lagou.com/fe_enhancement.html'),
                                            ('https://kaiwu.lagou.com/data_enhancement.html'),
                                            ('https://kaiwu.lagou.com/test_engineer.html')
                                            ])
def test_big_course(big_course_url):
    url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
    data = {'key': get_pagespeed_api_key(), 'locale': 'zh_CN', 'url': big_course_url,
            'strategy': 'desktop'}
    headers[
        'Referer'] = f'https://developers.google.com/speed/pagespeed/insights/?url={big_course_url}'
    result = requests.get(url=url, params=data, headers=headers, verify=False, timeout=120).json()
    assert isinstance(result, dict)
    audits = result['lighthouseResult']['audits']

    global content
    content += f'''{big_course_url}\n'''
    content += f'''{audits['first-contentful-paint']['title']}:{round(audits['first-contentful-paint']['numericValue'] / 1000, 2)}秒\n'''
    content += f'''{audits['interactive']['title']}:{round(audits['interactive']['numericValue'] / 1000, 2)}秒\n'''
    content += f'''{audits['speed-index']['title']}:{round(audits['speed-index']['numericValue'] / 1000, 2)}秒\n'''
    content += f'''{audits['total-blocking-time']['title']}:{round(audits['total-blocking-time']['numericValue'], 3)}毫秒\n'''
    content += f'''{audits['largest-contentful-paint']['title']}:{round(audits['largest-contentful-paint']['numericValue'] / 1000, 2)}秒\n'''
    content += f'''{audits['cumulative-layout-shift']['title']}:{round(audits['cumulative-layout-shift']['numericValue'], 3)}\n'''

    log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'log/ui.log')
    with open(log_path, 'a') as f:
        f.write(content)

    # global report_info, report_path
    # report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testdata/report.json')
    # with open(report_path, 'r') as fp:
    #     load_json = json.load(fp)
    #     audits = load_json['audits']
    #     info = ''
    #     info += f'''{audits['first-contentful-paint']['title']}:{round(audits['first-contentful-paint']['numericValue'] / 1000, 2)}秒\n'''
    #     info += f'''{audits['interactive']['title']}:{round(audits['interactive']['numericValue'] / 1000, 2)}秒\n'''
    #     info += f'''{audits['speed-index']['title']}:{round(audits['speed-index']['numericValue'] / 1000, 2)}秒\n'''
    #     info += f'''{audits['total-blocking-time']['title']}:{round(audits['total-blocking-time']['numericValue'], 3)}毫秒\n'''
    #     info += f'''{audits['largest-contentful-paint']['title']}:{round(audits['largest-contentful-paint']['numericValue'] / 1000, 2)}秒\n'''
    #     info += f'''{audits['cumulative-layout-shift']['title']}:{round(audits['cumulative-layout-shift']['numericValue'], 3)}\n'''
    #     report_info.setdefault(url, info)


def test_send_fei_shu_report():
    # content = ''
    # for k, v in report_info.items():
    #     content += f'{k}:\n{v}\n'

    # log_path = '/Users/wang/Desktop/lg-project/lg_api_script/log/ui.log'

    url = 'https://open.feishu.cn/open-apis/bot/hook/d96534525a0744ec9d228571730884b2'
    # url = 'https://open.feishu.cn/open-apis/bot/hook/882babeafa3e4f0b839d6ff41efa2b84'
    data = {
        "title": "页面性能报告",
        "text": content
    }
    result = requests.post(url=url, json=data, verify=False).json()

    assert result.get('ok') == 1
