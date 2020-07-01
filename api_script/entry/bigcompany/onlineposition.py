# -*- coding:utf8 -*-
__author__ = 'arayang'
import utils
from utils.util import get_app_header,get_requests,json_post

header = utils.util.get_app_header(100012754)

def onlinepositions():
    url = "https://gate.lagou.com/v1/entry/position/queryPositions?companyId=142475&pageNo=1&pageSize=5"

    return get_requests(url=url,headers=header,remark='在招职位列表页', rd='royliu')
#onlinepositions()