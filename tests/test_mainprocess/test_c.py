# coding:utf-8
# @Time  : 2019-09-20 10:42
# @Author: Xiawang
# Description:


import pytest

from api_script.entry.account.passport import password_login, send_verify_code, verifyCode_login, register_by_phone, \
    get_login_by_token
from api_script.neirong_app.resumes import guideBasicInfo, educationExperiences
from utils.util import assert_equal, verify_code_message

countryCode, phone = '00852', '20180917'


@pytest.mark.parametrize("accountName,password", [("admin", "admin")])
def test_password_login(accountName, password):
    r = password_login(accountName, password)
    assert_equal(1, r['state'], '校验密码登录成功', '校验密码登录失败')


@pytest.mark.mainprocess
def test_send_verify_code():
    r = send_verify_code(countryCode, phone)
    assert_equal(1, r['state'], '校验发送验证码成功', "校验发送验证码失败")


@pytest.mark.mainprocess
def test_get_verify_code():
    global verify_code
    verify_code = verify_code_message(countryCode, phone)


@pytest.mark.mainprocess
def test_verifyCode_login():
    r = verifyCode_login(countryCode, phone, verify_code)
    assert_equal(201001, r['state'], "校验登录转待注册成功")


@pytest.mark.mainprocess
def test_register_by_phone():
    r = register_by_phone(countryCode, phone, verify_code)
    assert_equal(1, r['state'], "校验注册成功")
    global userToken
    userToken = r['content']['userToken']


def test_get_login_by_token():
    r = get_login_by_token(userToken)
    assert_equal(1, r['state'], '校验token登录成功')


def test_guideBasicInfo():
    new_phone = countryCode + phone
    r = guideBasicInfo(new_phone, userToken)
    assert_equal(1, r['state'], '校验提交基本信息成功')


def test_educationExperiences():
    r = educationExperiences(userToken)
    assert_equal(1, r['state'], "校验提交教育经历成功")
