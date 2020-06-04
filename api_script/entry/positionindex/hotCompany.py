# coding:utf-8
# @Time  : 2019-09-23 11:12
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def switch_city(userToken, city):
    url = 'https://gate.lagou.com/v1/entry/positionindex/hotCompany?city={}'.format(city)
    header = app_header_999(userToken)
    return get_requests(url=url, headers=header, remark="切换搜索的职位")
