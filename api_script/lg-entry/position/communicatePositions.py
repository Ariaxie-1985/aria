# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import get_app_header, get_requests, json_post

header=get_app_header(100014641)
def communicatePositions():
    url='https://gate.lagou.com/v1/entry/position/communicatePositions'
    data={'hrId':100013384,'pageNo':1,'pageSize':20}
    return get_requests(url=url,data=data,headers=header,remark='查询沟通职位列表')

# communicatePositions()