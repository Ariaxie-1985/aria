import re

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


def big_course(url):
    url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
    data = {'key': pagespeed_api_key, 'locale': 'zh_CN', 'url': url,
            'strategy': 'desktop'}
    headers[
        'Referer'] = f'https://developers.google.com/speed/pagespeed/insights/?url={url}'
    result = requests.get(url=url, params=data, headers=headers, verify=False, timeout=120).json()
    audits = result['lighthouseResult']['audits']

    info = ''
    info += f'''{audits['first-contentful-paint']['title']}:{round(audits['first-contentful-paint']['numericValue'] / 1000, 2)}秒\n'''
    info += f'''{audits['interactive']['title']}:{round(audits['interactive']['numericValue'] / 1000, 2)}秒\n'''
    info += f'''{audits['speed-index']['title']}:{round(audits['speed-index']['numericValue'] / 1000, 2)}秒\n'''
    info += f'''{audits['total-blocking-time']['title']}:{round(audits['total-blocking-time']['numericValue'], 3)}毫秒\n'''
    info += f'''{audits['largest-contentful-paint']['title']}:{round(audits['largest-contentful-paint']['numericValue'] / 1000, 2)}秒\n'''
    info += f'''{audits['cumulative-layout-shift']['title']}:{round(audits['cumulative-layout-shift']['numericValue'], 3)}\n'''

    print(info)
