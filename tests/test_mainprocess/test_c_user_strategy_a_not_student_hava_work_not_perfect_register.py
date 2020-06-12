# coding:utf-8
# @Time  : 2020-06-10
# @Author: sunnysun
# Description:
import logging
import time
from utils.loggers import logers
import pytest

from api_script.entry.account.passport import password_login, send_verify_code, verifyCode_login, register_by_phone, \
    get_login_by_token
from api_script.entry.cuser.baseStatus import get_info, batchCancel
from api_script.home import forbid
from api_script.neirong_app.resumes import guideBasicInfo, educationExperiences, personalCards, abilityLabels, \
    expectJob, workExperiences, set_basicInfo, delete_education_experiences, get_detail, delete_workExperiences
from utils.read_file import record_test_data, record_cancel_account
from utils.util import assert_equal, get_strategies_999,verify_code_message, login_password

time.sleep(2)
loger=logers()

@pytest.mark.incremental
class TestNotStudentHaveWorkRegister(object):
    def test_send_verify_code(self, get_country_code_phone_user):
        global countryCode, phone, register_state
        countryCode, phone, name = get_country_code_phone_user
        r = send_verify_code(countryCode, phone, "PASSPORT_REGISTER",1)
        register_state = r.get('state')
        assert_equal(1, register_state, '校验发送验证码成功', "失败的手机号:{}".format(phone))
    def test_get_verify_code(self):
        global verify_code
        verify_code = verify_code_message(countryCode, phone)
        assert_equal(True, bool(verify_code), "校验获取验证码成功")

    def test_verifyCode_login(self):
        r = verifyCode_login(countryCode, phone, verify_code)
        global register_state
        register_state = r.get('state', 0)
        assert_equal(201001, register_state, "校验验证码登录转注册成功", "失败的手机号:{}".format(phone))

    def test_register_by_phone(self):
        r = register_by_phone(countryCode, phone, verify_code)
        global register_state
        register_state = r.get('state', 0)
        assert_equal(1, register_state, "校验注册成功", "失败的手机号:{}".format(phone))
        global userToken, userId
        userToken = r['content']['userToken']
        userId = r['content']['userInfo']['userId']

    def test_get_login_by_token(self):
        r = get_login_by_token(userToken)
        logging.info(msg='userToken {} \n'.format(userToken))
        assert_equal(1, r.get('state'), '校验token登录成功')

    def test_guideBasicInfo(self):
        global s
        s=get_strategies_999(userToken='9bb6fe5ac8664d17bd38af909124c43ee9b92e213c6f105417c5811045c144fa')
        r = guideBasicInfo(countryCode + phone, 2, userToken)
        if s=='A' or s=='B':
            r = guideBasicInfo(countryCode + phone, 2, userToken,s)
        assert_equal(1, r.get('state'), '校验提交基本信息成功，策略'+s)
        loger.info('提交基本信息成功，策略'+s)

    def test_educationExperiences(self):
        r = educationExperiences(userToken)
        assert_equal(1, r.get('state'), "校验提交教育经历成功")

    def test_workExperiences(self):
        r = workExperiences(userToken)
        if s=='A':
            r=workExperiences(userToken,s)
        assert_equal(1, r.get('state'), '校验提交工作经历')
        loger.info('提交工作经历成功，策略' + s)

    def test_personalCards(self):
        r = personalCards(userToken)
        if s=='A':
            r=personalCards(userToken,s)
            assert_equal(1, r.get('state'), '校验跳过个人名片成功')
            loger.info('跳过个人名片成功，策略' + s)
        else:
            assert_equal(1, r.get('state'), '校验提交个人名片成功')
            loger.info('提交个人名片成功，策略' + s)

    def test_expectJob(self):
        r = expectJob(userToken)
        assert_equal(1, r.get('state'), '校验提交求职意向')


