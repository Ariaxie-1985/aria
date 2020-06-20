# coding:utf-8
# @Time  : 2020/6/17 16:06
# @Author: Xiawang
# Description:
import json
import os
import subprocess
import time

import requests


def switch_project_root_directory():
    project_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # os.chdir(project_path)
    return project_path


report_info = {}

urls = ['https://kaiwu.lagou.com/java_basic.html',
        'https://kaiwu.lagou.com/java_architect.html',
        'https://kaiwu.lagou.com/fe_enhancement.html',
        'https://kaiwu.lagou.com/data_enhancement.html',
        'https://kaiwu.lagou.com/test_engineer.html'
        ]


def big_course(url):
    report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testdata/report.json')
    cmd_str = f'lighthouse {url} --chrome-flags="--incognito --headless" --only-categories=performance --locale=zh --emulated-form-factor=desktop --throttling-method=provided --output=json --output-path={report_path} --save-assets --quiet'
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


def send_fei_shu_report():
    content = ''
    for k, v in report_info.items():
        content += f'{k}:\n{v}\n'

    url = 'https://open.feishu.cn/open-apis/bot/hook/d96534525a0744ec9d228571730884b2'
    # url = 'https://open.feishu.cn/open-apis/bot/hook/882babeafa3e4f0b839d6ff41efa2b84'
    data = {
        "title": "页面性能报告",
        "text": content
    }
    # project_path = switch_project_root_directory()
    log_path = '/Users/wang/Desktop/lg-project/lg_api_script/log/ui.log'
    with open(log_path, 'a') as f:
        f.write(content)
    result = requests.post(url=url, json=data, verify=False).json()

    assert result.get('ok') == 1


if __name__ == '__main__':
    switch_project_root_directory()
    for url in urls:
        big_course(url)
    send_fei_shu_report()
    print('执行完成')
