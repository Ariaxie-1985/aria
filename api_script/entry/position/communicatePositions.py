# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import get_app_header, get_requests, json_post, app_header_999

header = get_app_header(100014641)


def communicatePositions():
    url = 'https://gate.lagou.com/v1/entry/position/communicatePositions'
    data = {'hrId': 100013384, 'pageNo': 1, 'pageSize': 20}
    return get_requests(url=url, data=data, headers=header, remark='查询沟通职位列表')


# communicatePositions()


def query_positions(userToken, companyId):
    url = 'https://gate.lagou.com/v1/entry/position/queryPositions?companyId={}&pageNo=0&pageSize=0'.format(companyId)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="查询公司的在招职位").json()


def query_by_company(userToken, companyId, positionType):
    url = 'https://gate.lagou.com/v1/entry/position/queryByCompany?companyId={}&positionType={}&pageNo=1&pageSize=10'.format(
        companyId, positionType)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark='根据筛选条件查询公司的在招职位').json()
