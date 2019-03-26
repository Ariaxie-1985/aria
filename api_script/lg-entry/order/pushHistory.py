# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_app_header, get_requests, json_post
header=get_app_header(100014641)

def pushHistory():
    url='https://gate.lagou.com/v1/entry/im/pushDeliverHistory?sessionId=1'
    return json_post(url=url,headers=header,remark='推送投递记录')

# pushHistory()