# coding:utf-8
# @Time  : 2020/6/15 14:38
# @Author: Xiawang
# Description:
import time

import pytest
import requests
import urllib3
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from utils.loggers import logers

loger = logers()
urllib3.disable_warnings()
content = ''


# def test_setup():
#     global driver
#     options = Options()
#     options.page_load_strategy = 'normal'
#     # options.headless = True
#     # options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-gpu')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('–incognito')
#     driver = Chrome(executable_path='/Users/wang/Downloads/chromedriver', options=options)
#     # driver = Chrome(executable_path='/home/test/chrome/chromedriver', options=options)
#

def test_re_write_log():
    with open('/Users/wang/Desktop/lg-project/lg_api_script/log/py_auto_test_result.log', 'w') as fp:
        pass


@pytest.mark.parametrize('url',
                         [('https://kaiwu.lagou.com/java_basic.html'),
                          ('https://kaiwu.lagou.com/java_architect.html'),
                          ('https://kaiwu.lagou.com/fe_enhancement.html'),
                          ('https://kaiwu.lagou.com/data_enhancement.html'),
                          ('https://kaiwu.lagou.com/test_engineer.html'),
                          ('https://kaiwu.lagou.com/java_basic.html'),
                          ('https://kaiwu.lagou.com/java_architect.html'),
                          ('https://kaiwu.lagou.com/fe_enhancement.html'),
                          ('https://kaiwu.lagou.com/data_enhancement.html'),
                          ('https://kaiwu.lagou.com/test_engineer.html'),
                          ('https://kaiwu.lagou.com/java_basic.html'),
                          ('https://kaiwu.lagou.com/java_architect.html'),
                          ('https://kaiwu.lagou.com/fe_enhancement.html'),
                          ('https://kaiwu.lagou.com/data_enhancement.html'),
                          ('https://kaiwu.lagou.com/test_engineer.html'),
                          ('https://kaiwu.lagou.com/java_basic.html'),
                          ('https://kaiwu.lagou.com/java_architect.html'),
                          ('https://kaiwu.lagou.com/fe_enhancement.html'),
                          ('https://kaiwu.lagou.com/data_enhancement.html'),
                          ('https://kaiwu.lagou.com/test_engineer.html'),
                          ('https://kaiwu.lagou.com/java_basic.html'),
                          ('https://kaiwu.lagou.com/java_architect.html'),
                          ('https://kaiwu.lagou.com/fe_enhancement.html'),
                          ('https://kaiwu.lagou.com/data_enhancement.html'),
                          ('https://kaiwu.lagou.com/test_engineer.html')
                          ])
def test_big_course(url):
    global content
    options = Options()
    options.page_load_strategy = 'normal'
    # options.add_argument('--normal')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--incognito')
    driver = Chrome(executable_path='/Users/wang/Downloads/chromedriver', options=options)

    t0 = time.perf_counter()
    driver.get(url)
    elapsed = time.perf_counter() - t0

    # log = f'{url}, 页面大小:{round(len(driver.page_source) / 1024, 3)}KB, 耗时:{round(elapsed, 3)}s'
    loger.info(f'{url}, 页面大小:{round(len(driver.page_source) / 1024, 3)}KB, 耗时:{round(elapsed, 3)}s')
    # content += log + '\n'
    driver.quit()
    time.sleep(1)


def test_generated_content():
    import re
    global content

    with open('/Users/wang/Desktop/lg-project/lg_api_script/log/py_auto_test_result.log', 'r') as fp:
        index = {}
        for line in fp.readlines():
            url = re.findall(r'([a-zA-z]+://[^\s]*),', line)[0][1:]
            size = re.findall(r'页面大小:(.*?)KB', line)[0]
            time = re.findall(r'耗时:(.*?)s', line)[0]
            index.setdefault(url, {}).setdefault('size', []).append(float(size))
            index[url].setdefault('time', []).append(float(time))

        for url, data in index.items():
            content += f'{url}, {round(sum(data["size"]) / 5, 3)}kb, {round(sum(data["time"]) / 5, 3)}s\n'


def test_send_fei_shu_report():
    url = 'https://open.feishu.cn/open-apis/bot/hook/d96534525a0744ec9d228571730884b2'
    data = {
        "title": "页面大小和请求耗时的平均结果(执行五次,除5)",
        "text": content
    }

    result = requests.post(url=url, json=data, verify=False).json()

    assert result.get('ok') == 1


'''

options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
'''
