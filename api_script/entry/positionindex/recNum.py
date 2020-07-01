# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import get_app_header_new, get_requests, json_post
header=get_app_header_new(100014641,{"deviceType":10,"appVersion":"7.17.0","reqVersion":71700})
def recNum():
    url='https://gate.lagou.com/v1/entry/positionindex/recNum?pageNo=1&pageSize=1000'
    return get_requests(url=url,headers=header,remark='首页推荐数量', rd='royliu')

# print(recNum())
