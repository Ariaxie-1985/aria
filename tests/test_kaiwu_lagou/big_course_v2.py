import re

import requests

url = 'https://developers.google.com/speed/pagespeed/insights/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Upgrade-Insecure-Requests': '1'}
result = requests.get(url=url, headers=headers, verify=False)
assert result.status_code == 200

pagespeed_api_key = re.findall(r"PAGESPEED_API_KEY='(.*?)';", result.text)[0]

url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
data = {'key': pagespeed_api_key, 'locale': 'zh_CN', 'url': 'https://kaiwu.lagou.com/test_engineer.html',
        'strategy': 'desktop'}
headers[
    'Referer'] = 'https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Fkaiwu.lagou.com%2Ftest_engineer.html'
result = requests.get(url=url, params=data, headers=headers, verify=False).json()
audits = ['lighthouseResult']['audits']
print(result['lighthouseResult']['audits']['first-contentful-paint']['title'], round(result['lighthouseResult']['audits']['first-contentful-paint']['numericValue']))
print(result['lighthouseResult']['audits']['first-contentful-paint']['title'], round(result['lighthouseResult']['audits']['first-contentful-paint']['numericValue']))

info = ''
info += f'''{audits['first-contentful-paint']['title']}:{round(audits['first-contentful-paint']['numericValue'] / 1000, 2)}秒\n'''
info += f'''{audits['interactive']['title']}:{round(audits['interactive']['numericValue'] / 1000, 2)}秒\n'''
info += f'''{audits['speed-index']['title']}:{round(audits['speed-index']['numericValue'] / 1000, 2)}秒\n'''
info += f'''{audits['total-blocking-time']['title']}:{round(audits['total-blocking-time']['numericValue'], 3)}毫秒\n'''
info += f'''{audits['largest-contentful-paint']['title']}:{round(audits['largest-contentful-paint']['numericValue'] / 1000, 2)}秒\n'''
info += f'''{audits['cumulative-layout-shift']['title']}:{round(audits['cumulative-layout-shift']['numericValue'], 3)}\n'''

print(info)
