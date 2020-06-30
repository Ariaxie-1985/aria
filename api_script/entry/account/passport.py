# coding:utf-8
# @Time  : 2019-09-19 11:24
# @Author: Xiawang
# Description:
from api_script.entry.cuser.baseStatus import batchCancel
from utils.util import json_post, get_requests, app_header_999


def password_login(accountName, password, ip_port=None, app_type='zhaopin'):
    url = 'https://gate.lagou.com/v1/entry/account/passport/login'
    header = app_header_999(app_type=app_type)
    data = {
        "password": password,
        "UrlType": 1,
        "isConfirm": 0,
        "loginType": 0,
        "accountName": accountName
    }
    r = json_post(url=url, headers=header, data=data, remark="密码登录", ip_port=ip_port)
    return r


def verifyCode_login(countryCode, phone, verify_code, app_type='zhaopin'):
    url = 'https://gate.lagou.com/v1/entry/account/passport/login'
    data = {
        "countryCode": countryCode,
        "phone": phone,
        "UrlType": 1,
        "isConfirm": 0,
        "loginType": 1,
        "verifyCode": verify_code
    }
    header = app_header_999(app_type=app_type)
    r = json_post(url=url, headers=header, data=data, remark="验证码登录", verifystate=False)
    return r


def send_verify_code(countryCode, phone, businessType, verifyCodeStyle=None, app_type='zhaopin'):
    url = 'https://gate.lagou.com/v1/entry/account/verifyCode/phone'
    data = {
        "countryCode": countryCode,
        "phone": phone,
        "verifyCodeType": 0,
        "businessType": businessType
    }
    header = app_header_999(app_type=app_type)
    if verifyCodeStyle is not None:
        data["verifyCodeStyle"] = verifyCodeStyle
    remark = "验证码登录，发送验证码"
    r = json_post(url=url, data=data, headers=header, remark=remark)
    return r


def register_by_phone(countryCode, phone, verify_code,app_type='zhaopin'):
    # 可返回userToken
    url = 'https://gate.lagou.com/v1/entry/account/passport/registerByPhone'
    data = {
        "phone": phone,
        "countryCode": countryCode,
        "verifyCode": verify_code
    }
    header = app_header_999(app_type=app_type)
    remark = '手机号注册账号'
    r = json_post(url=url, data=data, headers=header, remark=remark)
    return r


def get_login_by_token(userToken):
    url = 'https://gate.lagou.com/v1/entry/account/passport/loginByToken'
    header = app_header_999(userToken)
    r = get_requests(url=url, headers=header, remark="通过token登录,其header:{}".format(header))
    return r


if __name__ == '__main__':
    r = password_login("0085220180917", "0085220180917")
    print(r)
