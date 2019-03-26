# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import get_app_header, get_requests, json_post

header=get_app_header(100014641)
def operations():
    url='https://gate.lagou.com/v1/entry/im/operations'
    data={'sessionId':'1','positionId':'1'}
    return get_requests(url=url,data=data,headers=header,remark='获取操作区信息')
# operations()