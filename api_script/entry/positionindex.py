# coding:utf-8
# @Time  : 2020/4/14 16:18
# @Author: Xiawang
# Description:
from utils.util import app_header_999, json_post, get_requests


def rec(userToken, expectJobId, filterCity='北京', city='北京', ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/entry/positionindex/rec'
    header = app_header_999(userToken=userToken, userId=userId)
    data = {
        "expectJobId": expectJobId,
        "isTopAd": 0,
        "filterCity": filterCity,
        "showId": "",
        "isAd": 1,
        "expectJobPageNo": 1,
        "salaryLower": 0,
        "city": city,
        "salaryUpper": 0,
        "shieldDeliveryCompany": False,
        "pageNo": 1,
        "pageSize": 10
    }
    return json_post(url=url, data=data, headers=header, remark='推荐职位', ip_port=ip_port, rd='royliu')


def expect_job_list(userToken, ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/entry/expectJob/list'
    header = app_header_999(userToken=userToken, userId=userId)
    return get_requests(url=url, headers=header, remark='求职意向', ip_port=ip_port, rd='征桂')


def new(userToken, expectJobId, filterCity='北京', ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/entry/positionindex/new'
    header = app_header_999(userToken=userToken, userId=userId)
    data = {
        "pageSize": 10,
        "salaryLower": 0,
        "pageNo": 1,
        "expectJobPageNo": 1,
        "shieldDeliveryCompany": False,
        "salaryUpper": 0,
        "filterCity": filterCity,
        "expectJobId": expectJobId
    }
    return json_post(url=url, data=data, headers=header, remark='推荐职位', ip_port=ip_port, rd='royliu')


def switch_city(userToken, city):
    url = 'https://gate.lagou.com/v1/entry/positionindex/hotCompany?city={}'.format(city)
    header = app_header_999(userToken)
    return get_requests(url=url, headers=header, remark="切换搜索的职位", rd='royliu')


# def position_index_suggestion(userToken, userId=None, ip_port=None):
#     url = 'https://gate.lagou.com/v1/entry/positionindex/suggestion'
#     header = app_header_999(userToken, DA=False, userId=userId)
#     return get_requests(url=url, headers=header, remark="个性化搜索", ip_port=ip_port)
