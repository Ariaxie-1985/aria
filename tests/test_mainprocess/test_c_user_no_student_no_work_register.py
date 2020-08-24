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
from utils.read_file import record_test_data, record_cancel_account
from utils.util import assert_equal, verify_code_message, login_password

time.sleep(2)


@pytest.mark.incremental
class TestNotStudentNotWorkRegister(object):
    def test_send_verify_code(self, get_country_code_phone_user):
        global countryCode, phone, register_state
        countryCode, phone, name = get_country_code_phone_user
        r = send_verify_code(countryCode, phone, "PASSPORT_REGISTER")
        assert_equal(expect_value=1, actual_value=r.get('state'), success_message='校验发送验证码成功',
                     fail_message=f"失败的手机号:{phone}", te='王洋')

    def test_get_verify_code(self):
        global verify_code
        verify_code = verify_code_message(countryCode, phone)
        assert_equal(True, bool(verify_code), "校验获取验证码成功", te='王洋')

    def test_verifyCode_login(self):
        r = verifyCode_login(countryCode, phone, verify_code)
        global register_state
        register_state = r.get('state', 0)
        assert_equal(expect_value=201001, actual_value=register_state, success_message="校验验证码登录转注册成功",
                     fail_message="失败的手机号:{}".format(phone), te='王洋')

    def test_register_by_phone(self):
        r = register_by_phone(countryCode, phone, verify_code)
        global register_state
        register_state = r.get('state', 0)
        assert_equal(expect_value=1, actual_value=register_state, success_message="校验注册成功",
                     fail_message="失败的手机号:{}".format(phone), te='王洋')
        global userToken, userId
        userToken = r['content']['userToken']
        userId = r['content']['userInfo']['userId']

    def test_get_login_by_token(self):
        r = get_login_by_token(userToken)
        logging.info(msg='userToken {} \n'.format(userToken))
        assert_equal(1, r.get('state'), '校验token登录成功', te='王洋')

    def test_guideBasicInfo(self):
        r = guideBasicInfo(countryCode + phone, 2, userToken, joinWorkTime="暂无工作经历")
        assert_equal(1, r.get('state'), '校验提交基本信息成功', te='王洋')

    def test_educationExperiences(self):
        r = educationExperiences(userToken)
        assert_equal(1, r.get('state'), "校验提交教育经历成功", te='王洋')

    def test_personalCards(self):
        r = personalCards(userToken)
        assert_equal(1, r.get('state'), '校验提交个人名片成功', te='王洋')

    def test_abilityLabels(self):
        r = abilityLabels(userToken)
        assert_equal(1, r.get('state'), '校验提交综合能力成功', te='王洋')

    def test_expectJob(self):
        r = expectJob(userToken)
        assert_equal(1, r.get('state'), '校验提交求职意向', te='王洋')

    def test_get_info(self):
        time.sleep(1)
        r = get_info(userToken)
        assert_equal(1, r.get('state'), '获取C端用户信息', te='王洋')
