# -*- coding: utf8 -*-
__author__ = 'yqzhang'

from api_script.entry.account.passport import password_login
from utils.util import app_header_999, json_post, get_requests


def search_positions(userToken, userId=None, ip_port=None, **kw):
    city = kw.get('city', '北京')
    keyword = kw.get('keyword', '测试')
    showId = kw.get('showId', "")
    salaryLower = kw.get('salaryLower', 20000)
    salaryUpper = kw.get('salaryUpper', 35000)
    header = app_header_999(userToken, DA=False, userId=userId)
    url = 'https://gate.lagou.com/v1/entry/positionsearch/searchPosition'
    data = {
        "keyword": keyword,
        "hiTag": "",
        "refreshHiTagList": True,
        "shieldDeliveyCompany": False,
        "sort": "0",
        "showId": showId,
        "workExperience": ["5-10年"],
        "keywordSource": 0,
        "lastShowCompanyId": 0,
        "isAd": "1",
        "tagType": "",
        "salaryLower": salaryLower,
        "city": city,
        "salaryUpper": salaryUpper,
        "education": [],
        "jobNature": [],
        "pageNo": 1,
        "longitudeAndLatitude": "-1.000000,-1.000000",
        "pageSize": 15
    }
    return json_post(url=url, data=data, headers=header, remark='搜索职位', ip_port=ip_port, rd='royliu')


def hotEmployee_activeHr(userToken, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/positionsearch/hotEmployee/activeHr?pageNo=1&pageSize=5'
    header = app_header_999(userToken, DA=False, userId=userId)
    remark = "专属热招-聊出好机会"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def hotEmployee_nearby(userToken, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/positionsearch/hotEmployee/nearby?pageNo=1&pageSize=5&longitude=0&latitude=0'
    header = app_header_999(userToken, DA=False, userId=userId)
    remark = "专属热招-附近热招"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def hotEmployee_selected(userToken, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/positionsearch/hotEmployee/selected?pageNo=1&pageSize=5'
    header = app_header_999(userToken, DA=False, userId=userId)
    remark = "专属热招-小勾精选"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def hotEmployee_topCompany(userToken, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/positionsearch/hotEmployee/topCompany?pageNo=1&pageSize=5'
    header = app_header_999(userToken, DA=False, userId=userId)
    remark = "专属热招-大厂专区"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


if __name__ == '__main__':
    # userToken, keyword, city, salaryLower, salaryUpper = "ddd502bdc68f7679f284efe5ea7bb1953b74a703633907b80265a4c8f2fe3436", "测试", "上海", 20000, 35000
    # r = search_positions(userToken, keyword, city, salaryLower, salaryUpper)
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    print(search_positions(userToken=userToken))
