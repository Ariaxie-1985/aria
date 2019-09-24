# coding:utf-8
# @Time  : 2019-09-20 10:42
# @Author: Xiawang
# Description:


import pytest
from api_script.entry.account.passport import password_login, send_verify_code, verifyCode_login, register_by_phone, \
    get_login_by_token
from api_script.entry.cuser.baseStatus import get_info
from api_script.neirong_app.resumes import guideBasicInfo, educationExperiences, personalCards, abilityLabels, expectJob
from utils.util import assert_equal, verify_code_message

countryCode, phone = '00852', '20180909'





def test_register_by_phone():
    r = register_by_phone(countryCode, phone, verify_code)
    assert_equal(1, r['state'], "校验注册成功")
    global userToken
    userToken = r['content']['userToken']


def test_get_login_by_token():
    r = get_login_by_token(userToken)
    assert_equal(1, r['state'], '校验token登录成功')


userToken = '97d82a3c008253fb633842b6b27129b231bea2949314555a6996cb2a3e3e0779'


def test_guideBasicInfo():
    r = guideBasicInfo(countryCode + phone, userToken)
    assert_equal(1, r['state'], '校验提交基本信息成功')


def test_educationExperiences():
    r = educationExperiences(userToken)
    assert_equal(1, r['state'], "校验提交教育经历成功")


def test_personalCards():
    r = personalCards(userToken)
    assert_equal(1, r['state'], '校验提交个人名片成功')


def test_abilityLabels():
    r = abilityLabels(userToken)
    assert_equal(1, r['state'], '校验提交综合能力成功')


def test_expectJob():
    r = expectJob(userToken)
    assert_equal(1, r['state'], '校验提交求职意向')


def test_get_info():
    r = get_info(userToken)
    assert_equal(1, r['state'], '获取C端用户信息')
