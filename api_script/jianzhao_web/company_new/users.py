# coding:utf-8
# @Time  : 2019-11-26 15:05
# @Author: Xiawang
# Description: 仅用于999环境
from utils.util import get_code_token, form_post


def user_register_lagou(countryCode,phone,verify_code):
    b_register_url = 'https://passport.lagou.com/register/register.html?from=b'
    register_url = "https://passport.lagou.com/register/register.json"
    register_data = {"isValidate": "true", "phone": phone, "phoneVerificationCode": verify_code, "challenge": 111,
                     "type": 1, "countryCode": countryCode}
    register_header = get_code_token(b_register_url)
    remark = "验证B端注册"
    return form_post(url=register_url, data=register_data, headers=register_header, remark=remark)