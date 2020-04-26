# coding:utf-8
# @Time  : 2019-09-19 11:24
# @Author: Xiawang
# Description:
from utils.util import json_post, get_requests, app_header_999


def password_login(accountName, password, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/account/passport/login'
    header = app_header_999()
    data = {
        "password": password,
        "UrlType": 1,
        "isConfirm": 0,
        "loginType": 0,
        "accountName": accountName
    }
    r = json_post(url=url, headers=header, data=data, remark="密码登录", ip_port=ip_port)
    return r


def verifyCode_login(countryCode, phone, verify_code):
    url = 'https://gate.lagou.com/v1/entry/account/passport/login'
    data = {
        "countryCode": countryCode,
        "phone": phone,
        "UrlType": 1,
        "isConfirm": 0,
        "loginType": 1,
        "verifyCode": verify_code
    }
    header = app_header_999()
    r = json_post(url=url, headers=header, data=data, remark="验证码登录", verifystate=False)
    return r


def send_verify_code(countryCode, phone, businessType):
    url = 'https://gate.lagou.com/v1/entry/account/verifyCode/phone'
    data = {
        "countryCode": countryCode,
        "phone": phone,
        "verifyCodeType": 0,
        "businessType": businessType
    }
    header = app_header_999()
    remark = "验证码登录，发送验证码"
    r = json_post(url=url, data=data, headers=header, remark=remark)
    return r


def register_by_phone(countryCode, phone, verify_code):
    # 可返回userToken
    url = 'https://gate.lagou.com/v1/entry/account/passport/registerByPhone'
    data = {
        "phone": phone,
        "countryCode": countryCode,
        "verifyCode": verify_code
    }
    header = app_header_999()
    remark = '手机号注册账号'
    r = json_post(url=url, data=data, headers=header, remark=remark)
    return r


def get_login_by_token(userToken):
    url = 'https://gate.lagou.com/v1/entry/account/passport/loginByToken'
    header = app_header_999(userToken)
    r = get_requests(url=url, headers=header, remark="通过token登录,其header:{}".format(header)).json()
    return r


if __name__ == '__main__':
    r = password_login("0085220181205", "0085220181205")
    print(r)
