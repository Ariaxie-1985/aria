# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import get_app_header_new, get_requests, json_post
header=get_app_header_new(100014641,{"deviceType":10,"appVersion":"7.17.0","reqVersion":71700})
def rec():
    url='https://gate.lagou.com/v1/entry/positionindex/rec'
    data={
        "city": "北京",
        "isAd": 1,
        "isTopAd": 1,
        "pageNo": 3,
        "pageSize": 2,
        "type": 0
    }
    return json_post(url=url,data=data,headers=header,remark='首页推荐')

# print(rec())