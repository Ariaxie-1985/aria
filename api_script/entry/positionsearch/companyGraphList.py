# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_app_header, get_requests, json_post

header=get_app_header(100014641)
def companyGraphList():
    url='https://gate.lagou.com/v1/entry/positionsearch/companyGraphList'
    data={
        "seriesName": "string",
        "type": 0
    }
    return json_post(url=url,data=data,headers=header,remark='公司图谱')
# companyGraphList()