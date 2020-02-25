# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import get_app_header, get_requests, json_post, app_header_999


def operations(userToken):
    url = 'https://gate.lagou.com/v1/entry/im/operations'
    data = {'sessionId': '1', 'positionId': '1'}
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, data=data, headers=header, remark='获取操作区信息')
