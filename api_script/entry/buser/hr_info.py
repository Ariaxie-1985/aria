# coding:utf-8
# @Time  : 2020-02-17 15:50
# @Author: Xiawang
from api_script.entry.account.passport import password_login
from utils.util import get_requests, app_header_999


def get_hr_info(userToken, publisherId):
    url = 'https://gate.lagou.com/v1/entry/buser/hrInfo/{}'.format(publisherId)
    header = app_header_999(userToken)
    return get_requests(url=url, headers=header, remark="获取HR信息").json()


def get_hr_card(userToken, publisherId):
    url = 'https://gate.lagou.com/v1/entry/buser/hr/getHRCard?id={}'.format(publisherId)
    header = app_header_999(userToken)
    return get_requests(url=url, headers=header, remark="获取HR卡片信息").json()


def get_info(userToken, publisherId):
    url = 'https://gate.lagou.com/v1/entry/buser/get'
    header = app_header_999(userToken, DA=False, userId=publisherId)
    return get_requests(url=url, headers=header, remark="获取HR信息").json()


def get_baseStatus(userToken, publisherId):
    url = 'https://gate.lagou.com/v1/entry/buser/baseStatus/get'
    header = app_header_999(userToken, DA=False, userId=publisherId)
    print(header)
    return get_requests(url=url, headers=header, remark="获取HR的基本状态").json()


if __name__ == '__main__':
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    r = get_info(userToken=userToken, publisherId=15130154)
    print(r)
