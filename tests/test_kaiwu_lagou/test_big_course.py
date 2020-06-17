# coding:utf-8
# @Time  : 2020/6/17 16:06
# @Author: Xiawang
# Description:
import os
import subprocess

import pytest


@pytest.mark.parametrize('url',
                         [('https://kaiwu.lagou.com/java_basic.html'),
                          # ('https://kaiwu.lagou.com/java_architect.html'),
                          # ('https://kaiwu.lagou.com/fe_enhancement.html'),
                          # ('https://kaiwu.lagou.com/data_enhancement.html'),
                          # ('https://kaiwu.lagou.com/test_engineer.html'),
                          # ('https://kaiwu.lagou.com/fe_enhancement.html'),
                          # ('https://kaiwu.lagou.com/data_enhancement.html'),
                          # ('https://kaiwu.lagou.com/test_engineer.html'),
                          ])
def test_big_course(url):
    global report_path
    report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'testdata/report.json')
    cmd_str = f'lighthouse {url} --chrome-flags="--incognito --headless" --only-categories=performance --locale=zh --emulated-form-factor=desktop --throttling-method=provided --output=json --output-path={report_path} --save-assets --quiet'
    ret = subprocess.run(cmd_str, shell=True, timeout=300, stdout=subprocess.PIPE, encoding='utf-8')
    assert ret.returncode == 0
    assert os.path.isfile(report_path) == True

def test_parse_report():
    pass


