# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import get_app_header_new, get_requests, json_post
header=get_app_header_new(100014641,{"deviceType":10,"appVersion":"7.17.0","reqVersion":71700})
def checkHomepageStatus():
    url='https://gate.lagou.com/v1/entry/positionindex/checkHomepageStatus'
    return get_requests(url=url,headers=header,remark='查询是否有刷新')

# print(checkHomepageStatus().text)