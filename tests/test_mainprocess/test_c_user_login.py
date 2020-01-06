# coding:utf-8
# @Time  : 2019-09-20 17:20
# @Author: Xiawang
# Description:
import time
import pytest
from api_script.entry.account.passport import password_login, send_verify_code, verifyCode_login
from utils.util import assert_equal, verify_code_message, get_verify_code_message_len

countryCode, phone = "00852", "20180917"
r = get_verify_code_message_len(countryCode, phone)
pytestmark = pytest.mark.skipif(r == 4, reason="验证码发送超过上限，跳过此用例")


@pytestmark
def test_password_login():
    r = password_login(countryCode + phone, countryCode + phone)
    assert_equal(1, r['state'], '校验密码登录成功', '校验密码登录失败')


@pytestmark
def test_send_verify_code():
    r = send_verify_code(countryCode, phone, "PASSPORT_REGISTER")
    assert_equal(1, r['state'], '校验发送验证码成功', "校验发送验证码失败")


time.sleep(1)


@pytestmark
def test_get_verify_code():
    global verify_code
    verify_code = verify_code_message(countryCode, phone, flag_num=r)
    assert_equal(True, bool(verify_code), "校验获取验证码成功")


@pytestmark
def test_verifyCode_login():
    r = verifyCode_login(countryCode, phone, verify_code)
    assert_equal(1, r['state'], "校验验证码登录成功")
