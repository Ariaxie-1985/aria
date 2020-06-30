# -*- coding: utf8 -*-
__author__ = 'Arayang'

import utils
from utils.util import get_app_header, get_requests, json_post

header = utils.util.get_app_header(100012754)


# def companyinfos(con):
# url='https://gate.lagou.com/v1/entry/bigCompany/query?companyId={}'.format(con)
def positionfilter():
    url = "https://gate.lagou.com/v1/entry/position/queryByCompany"
    data = {
        "companyId": 142475,
        "pageNo": 1,
        "pageSize": 10,
        "positionType": "技术",
        "city": "北京",
        "salary": "",
        "workYear": ""
    }
    return get_requests(url=url, headers=header, data=data, remark='公司主页职位筛选', rd='royliu')

# positionfilter()
