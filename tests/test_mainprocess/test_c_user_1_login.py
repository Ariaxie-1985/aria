# coding:utf-8
# @Time  : 2019-09-20 17:20
# @Author: Xiawang
# Description:

import pytest
from api_script.entry.account.passport import password_login, send_verify_code, verifyCode_login
from utils.util import assert_equal, verify_code_message, get_verify_code_message_len, assert_not_equal

def test_password_login():
    global countryCode, phone
    countryCode, phone = "00852", "20180917"
    r = password_login(countryCode + phone, countryCode + phone)
    assert_equal(expect_value=1, actual_value=r['state'], success_message='校验密码登录成功', fail_message='校验密码登录失败', te='王霞')


def test_is_verify_code_reach_upper_limit():
    global send_verify_code_times
    send_verify_code_times = get_verify_code_message_len(countryCode, phone)
    assert_not_equal(-1, send_verify_code_times, '获取验证码发送次数用例通过', te='王霞')


@pytest.mark.skipif('send_verify_code_times >= 50', reason="验证码发送超过上限，跳过此用例")
def test_send_verify_code():
    r = send_verify_code(countryCode, phone, "PASSPORT_REGISTER")
    assert_equal(expect_value=1, actual_value=r.get('state'), success_message='校验发送验证码成功', fail_message="校验发送验证码失败", te='王霞')


@pytest.mark.skipif('send_verify_code_times >= 50', reason="验证码发送超过上限，跳过此用例")
def test_get_verify_code():
    global verify_code
    verify_code = verify_code_message(countryCode, phone, flag_num=send_verify_code_times)
    assert_equal(True, bool(verify_code), "校验获取验证码成功", te='王霞')


@pytest.mark.skipif('send_verify_code_times >= 50', reason="验证码发送超过上限，跳过此用例")
def test_verifyCode_login():
    r = verifyCode_login(countryCode, phone, verify_code)
    assert_equal(1, r['state'], "校验验证码登录成功", te='王霞')
