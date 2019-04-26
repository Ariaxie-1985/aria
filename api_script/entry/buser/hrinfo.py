# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_app_header, get_requests, json_post

header = get_app_header(100014641)

def hrinfo():
    url='https://gate.lagou.com/v1/entry/buser/hrInfo/100013384'
    return get_requests(url=url,headers=header,remark='hr信息')

#hrinfo()