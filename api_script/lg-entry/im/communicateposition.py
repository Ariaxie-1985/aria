# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_app_header, get_requests, json_post

header=get_app_header(100014641)

def communicateposition():
    url='https://gate.lagou.com/v1/entry/im/communicateposition'
    data={
        "buserId": 100014641,
        "positionId":5378018 ,
        "sessionId": 1
    }
    return json_post(url=url,data=data,headers=header,remark='切换职位卡片')
# communicateposition()