# coding:utf-8
# @Time  : 2019-09-20 17:25
# @Author: Xiawang
# Description:
import logging
import time

import pytest

from api_script.entry.account.passport import password_login, send_verify_code, verifyCode_login, register_by_phone, \
    get_login_by_token
from api_script.entry.cuser.baseStatus import get_info, batchCancel
from api_script.home import forbid
from api_script.neirong_app.resumes import guideBasicInfo, educationExperiences, personalCards, abilityLabels, \
    expectJob, workExperiences
from utils.read_file import record_test_data
from utils.util import assert_equal, verify_code_message, login_password

time.sleep(1)


def test_send_verify_code(get_countryCode_phone):
    global countryCode, phone
    countryCode, phone = get_countryCode_phone[0], get_countryCode_phone[1]
    logging.info(msg='手机号 {} \n'.format(countryCode + phone))
    r = send_verify_code(countryCode, phone, "PASSPORT_REGISTER")
    assert_equal(1, r['state'], '校验发送验证码成功', "校验发送验证码失败")


def test_get_verify_code():
    global verify_code
    verify_code = verify_code_message(countryCode, phone)
    assert_equal(True, bool(verify_code), "校验获取验证码成功")


def test_verifyCode_login():
    r = verifyCode_login(countryCode, phone, verify_code)
    assert_equal(201001, r['state'], "校验验证码登录转注册成功")


def test_register_by_phone():
    r = register_by_phone(countryCode, phone, verify_code)
    assert_equal(1, r['state'], "校验注册成功")
    global userToken, userId
    userToken = r['content']['userToken']
    userId = r['content']['userInfo']['userId']


def test_get_login_by_token():
    r = get_login_by_token(userToken)
    logging.info(msg='userToken {} \n'.format(userToken))
    assert_equal(1, r['state'], '校验token登录成功')


def test_guideBasicInfo():
    r = guideBasicInfo(countryCode + phone, 2, userToken, joinWorkTime="暂无工作经历")
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


def test_batchCancel():
    r = batchCancel(userToken=userToken, userIds=userId)
    assert_equal(1, r['state'], "用户注册非学生但无工作经验的注销账号成功")


def test_record():
    record_test_data(type=1, userId=userId)


def test_login_home():
    # 线上home后台的用户账号和密码, 勿动
    r = login_password('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
    assert_equal(1, r['state'], '校验登录home成功！')


def test_forbid_general_user():
    forbid_result = forbid.forbid_user(userId)
    assert_equal(True, forbid_result, '校验非学生用户无工作经验的C端是否封禁成功')
