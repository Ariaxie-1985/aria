# coding:utf-8
# @Time  : 2019-09-19 11:24
# @Author: Xiawang
# Description:
import json

from utils.util import json_post, get_requests


def password_login(accountName, password):
    url = 'https://gate.lagou.com/v1/entry/account/passport/login'
    HEADER = {"lgId": "898BCC3F-E662-4761-87E8-845788525443_1532945379", "reqVersion": 72200, "appVersion": "7.21.0",
              "deviceType": 150}
    HEADER = json.dumps(HEADER)
    header = {"X-L-REQ-HEADER": HEADER,
              "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
    data = {
        "password": password,
        "UrlType": 1,
        "isConfirm": 0,
        "loginType": 0,
        "accountName": accountName
    }
    r = json_post(url=url, headers=header, data=data, remark="密码登录")
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
    header = {
        "X-L-REQ-HEADER": '{"lgId":"898BCC3F-E662-4761-87E8-845788525443_1532945379","reqVersion":72200,"appVersion":"7.21.0","deviceType":150}',
        "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
    r = json_post(url=url, headers=header, data=data, remark="验证码登录", verifystate=False)
    return r


def send_verify_code(countryCode, phone):
    url = 'https://gate.lagou.com/v1/entry/account/verifyCode/phone'
    data = {
        "countryCode": countryCode,
        "phone": phone,
        "verifyCodeType": 0,
        "businessType": "PASSPORT_REGISTER"
    }
    header = {
        "X-L-REQ-HEADER": '{"lgId":"898BCC3F-E662-4761-87E8-845788525443_1532945379","reqVersion":72200,"appVersion":"7.21.0","deviceType":150}',
        "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
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
    header = {
        "X-L-REQ-HEADER": '{"lgId":"898BCC3F-E662-4761-87E8-845788525443_1532945379","reqVersion":72200,"appVersion":"7.21.0","deviceType":150}',
        "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
    remark = '手机号注册账号'
    r = json_post(url=url, data=data, headers=header, remark=remark)
    return r


def get_login_by_token(userToken):
    HEADER = {"deviceType": 150, "userType": 0, "lgId": "898BCC3F-E662-4761-87E8-845788525443_1532945379",
              "reqVersion": 72200, "appVersion": "7.21.0", "userToken": '{}'.format(userToken)}
    HEADER = json.dumps(HEADER)
    url = 'https://gate.lagou.com/v1/entry/account/passport/loginByToken'
    header = {"X-L-REQ-HEADER": HEADER,
              "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
    r = get_requests(url=url, headers=header, remark="通过token登录").json()
    return r
