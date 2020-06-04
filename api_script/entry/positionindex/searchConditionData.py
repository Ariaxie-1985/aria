# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from utils.util import get_app_header, get_requests, json_post

header = get_app_header(100014641)


def searchConditionData():
    url = 'https://gate.lagou.com/v1/entry/positionindex/searchConditionData'
    return get_requests(url=url, headers=header, remark='搜索静态数据')


if __name__ == '__main__':
    print(searchConditionData())
