# coding:utf-8
# @Time  : 2019-09-25 14:52
# @Author: Xiawang
# Description:
from utils.util import app_header_999, json_post


def bing_or_change_phone(userToken, countryCode, phone, verifyCode):
    url = 'https://gate.lagou.com/v1/entry/account/me/bindOrChangePhone'
    header = app_header_999(userToken, DA=False)
    data = {
        "countryCode": countryCode,
        "phone": phone,
        "businessType": "CHANGE_BIND_PHONE",
        "verifyCode": verifyCode
    }
    return json_post(url=url, remark="更换C端用户的手机号", headers=header, data=data)
