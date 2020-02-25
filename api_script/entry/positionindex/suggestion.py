# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import app_header_999, get_requests


def position_index_suggestion(userToken):
    url = 'https://gate.lagou.com/v1/entry/positionindex/suggestion'
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="个性化搜索").json()
