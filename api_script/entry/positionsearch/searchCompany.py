# coding:utf-8
# @Time  : 2020/2/24
# @Author: Xiawang
from utils.util import json_post, app_header_999
import json


def searchCompany(userToken):
    url = 'https://gate.lagou.com/v1/entry/positionsearch/searchCompany'
    data = {
        "city": "北京",
        "keyword": "Java",
        "pageNo": 1,
        "pageSize": 5,
        "sortType": 0
    }
    header = app_header_999(userToken, DA=False)
    return json_post(url=url, data=data, headers=header, remark='搜索公司')


def search_company(userToken, **kwargs):
    header = app_header_999(userToken, DA=False)
    url = 'https://gate.lagou.com/v1/entry/positionsearch/searchCompany'
    city = kwargs.get('city', '北京')
    keyword = kwargs.get('keyword', '百度')
    data = {
        "pageSize": 10,
        "fundsStage": "",
        "city": city,
        "pageNo": 1,
        "sortType": 0,
        "keyword": keyword,
        "otherCondition": "",
        "industry": "",
        "scale": ""
    }
    return json_post(url=url, headers=header, data=data, remark='搜索公司')
