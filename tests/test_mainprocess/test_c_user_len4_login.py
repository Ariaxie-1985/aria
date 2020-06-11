# coding:utf-8
# @Time  : 2020-06-08
# @Author: sunnysun
# Description:四位验证码登录

import pytest
from api_script.entry.account.passport import password_login, send_verify_code, verifyCode_login
from utils.util import assert_equal, verify_code_message, get_verify_code_message_len, assert_not_equal

global countryCode, phone
countryCode, phone = "00852", "20180917"

def test_is_verify_code_reach_upper_limit():
    global send_verify_code_times
    send_verify_code_times = get_verify_code_message_len(countryCode, phone)
    assert_not_equal(-1, send_verify_code_times, '获取验证码用例通过')


@pytest.mark.skipif('send_verify_code_times >= 50', reason="验证码发送超过上限，跳过此用例")
@pytest.mark.incremental
class TestVerifyLoginLen4(object):

    def test_send_verify_code(self):
        r = send_verify_code(countryCode, phone, "PASSPORT_REGISTER", 1)
        assert_equal(1, r.get('state'), '校验发送验证码4位成功', "校验发送验证码4位失败")

    def test_get_verify_code(self):
        global verify_code
        verify_code = verify_code_message(countryCode, phone, flag_num=send_verify_code_times)
        assert_equal(True, bool(verify_code), "校验获取验证码4位成功")

    def test_verifyCode_login(self):
        r = verifyCode_login(countryCode, phone, verify_code)
        assert_equal(1, r['state'], "校验验证码4位登录成功")
