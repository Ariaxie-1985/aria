# coding:utf-8
# -*-coding:utf-8-*-
from urllib import parse

import requests


def get_requests_json():
    r = requests.get('http://127.0.0.1:18980/data/')
    code = r.json()
    #print(r)
    return code


def get_requests_html():
    r = requests.get('http://127.0.0.1:18980/data/html')
    code = r.text
    return code


def post_requests_json():
    payload = {"positionId": 8834,
        "positionName": "高级市场营销经理",
        "firstType": "市场|商务类",
        "positionType": "市场|营销",
        "positionThirdType": "市场营销",
        "workAddress": "北京市海淀区时代网络大厦4层"}
    r = requests.post('http://127.0.0.1:18980/data/position', data=payload)
    code = r.json()
    return code

def post_requests_form():
    payload = {"positionId": 1889,
        "positionName": "高级市场营销经理",
        "firstType": "市场|商务类",
        "positionType": "市场|营销",
        "positionThirdType": "市场营销",
        "workAddress": "北京市海淀区时代网络大厦4层"}
    #data = parse.urlencode(payload)
    r = requests.post('http://127.0.0.1:18980/data/position', data=payload)
    #r.encoding = 'utf-8'
    code = r.text
    return code

if __name__ == '__main__':
    r = get_requests_json()
    print(r)
    # get_requests_html()
    #post_requests_json()
    #post_requests_form()
