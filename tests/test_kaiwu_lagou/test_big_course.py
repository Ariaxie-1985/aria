# coding:utf-8
# @Time  : 2020/6/17 16:06
# @Author: Xiawang
# Description:
import json
import os
import subprocess
import pytest
import requests

report_info = {}


@pytest.mark.flaky(reruns=2, reruns_delay=10)
@pytest.mark.parametrize('url',
                         [('https://kaiwu.lagou.com/java_basic.html'),
                          ('https://kaiwu.lagou.com/java_architect.html'),
                          ('https://kaiwu.lagou.com/fe_enhancement.html'),
                          ('https://kaiwu.lagou.com/data_enhancement.html'),
                          ('https://kaiwu.lagou.com/test_engineer.html')
                          ])
def test_big_course(url):
    global report_info, report_path
    report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testdata/report.json')
    # cmd_str = f'lighthouse {url} --chrome-flags="--incognito --headless" --only-categories=performance --locale=zh --emulated-form-factor=desktop --throttling-method=provided --output=json --output-path={report_path} --save-assets --quiet'
    lighthouse_path = 'node /home/test/software/node-v12.18.0-linux-x64/lib/node_modules/lighthouse/lighthouse-cli'
    lighthouse_cmd_str = f'--chrome-flags="--incognito --headless" --only-categories=performance --locale=zh --emulated-form-factor=desktop --throttling-method=provided --output=json --output-path={report_path} --save-assets --disable-storage-reset --quiet'
    cmd_str = f'{lighthouse_path} {url} {lighthouse_cmd_str}'

    ret = subprocess.run(cmd_str, shell=True, timeout=300, stdout=subprocess.PIPE, encoding='utf-8')
    assert ret.returncode == 0
    assert os.path.isfile(report_path) == True

    with open(report_path, 'r') as fp:
        load_json = json.load(fp)
        audits = load_json['audits']
        info = ''
        info += f'''{audits['first-contentful-paint']['title']}:{round(audits['first-contentful-paint']['numericValue'] / 1000, 2)}秒\n'''
        info += f'''{audits['interactive']['title']}:{round(audits['interactive']['numericValue'] / 1000, 2)}秒\n'''
        info += f'''{audits['speed-index']['title']}:{round(audits['speed-index']['numericValue'] / 1000, 2)}秒\n'''
        info += f'''{audits['total-blocking-time']['title']}:{round(audits['total-blocking-time']['numericValue'], 3)}毫秒\n'''
        info += f'''{audits['largest-contentful-paint']['title']}:{round(audits['largest-contentful-paint']['numericValue'] / 1000, 2)}秒\n'''
        info += f'''{audits['cumulative-layout-shift']['title']}:{round(audits['cumulative-layout-shift']['numericValue'], 3)}\n'''
        report_info.setdefault(url, info)


def test_send_fei_shu_report():
    content = ''
    for k, v in report_info.items():
        content += f'{k}:\n{v}\n'

    # log_path = '/Users/wang/Desktop/lg-project/lg_api_script/log/ui.log'
    with open(report_path, 'a') as f:
        f.write(content)

    # url = 'https://open.feishu.cn/open-apis/bot/hook/d96534525a0744ec9d228571730884b2'
    url = 'https://open.feishu.cn/open-apis/bot/hook/882babeafa3e4f0b839d6ff41efa2b84'
    data = {
        "title": "页面性能报告",
        "text": content
    }
    result = requests.post(url=url, json=data, verify=False).json()

    assert result.get('ok') == 1
