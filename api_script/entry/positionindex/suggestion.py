# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import app_header_999, get_requests


def position_index_suggestion(userToken,userId=None,ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/positionindex/suggestion'
    header = app_header_999(userToken, DA=False,userId=userId)
    return get_requests(url=url, headers=header, remark="个性化搜索",ip_port=ip_port)
