# coding:utf-8
# @Time  : 2019-09-20 17:20
# @Author: Xiawang
# Description:
import pytest
from api_script.entry.account.passport import password_login, send_verify_code, verifyCode_login
from utils.util import assert_equal, verify_code_message


@pytest.mark.parametrize("accountName,password", [("0085220180917", "0085220180917")])
def test_password_login(accountName, password):
    r = password_login(accountName, password)
    assert_equal(1, r['state'], '校验密码登录成功', '校验密码登录失败')


countryCode, phone = "00852", "20180917"


def test_send_verify_code():
    r = send_verify_code(countryCode, phone)
    assert_equal(1, r['state'], '校验发送验证码成功', "校验发送验证码失败")


def test_get_verify_code():
    global verify_code
    verify_code = verify_code_message(countryCode, phone)
    assert_equal(True, bool(verify_code), "校验获取验证码成功")


def test_verifyCode_login():
    r = verifyCode_login(countryCode, phone, verify_code)
    assert_equal(1, r['state'], "校验验证码登录成功")
