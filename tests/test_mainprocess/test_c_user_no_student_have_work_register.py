# coding:utf-8
# @Time  : 2019-09-20 17:59
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
    expectJob, workExperiences, set_basicInfo, delete_education_experiences, get_detail, delete_workExperiences
from utils.read_file import record_test_data, record_cancel_account
from utils.util import assert_equal, verify_code_message, login_password

time.sleep(2)


@pytest.mark.incremental
class TestNotStudentHaveWorkRegister(object):
    def test_send_verify_code(self, get_country_code_phone_user):
        global countryCode, phone, register_state
        countryCode, phone, name = get_country_code_phone_user
        r = send_verify_code(countryCode, phone, "PASSPORT_REGISTER")
        register_state = r.get('state')
        assert_equal(expect_value=1, actual_value=register_state, success_message='校验发送验证码成功',
                     fail_message="失败的手机号:{}".format(phone), te='王洋')

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
        r = guideBasicInfo(countryCode + phone, 2, userToken)
        assert_equal(1, r.get('state'), '校验提交基本信息成功', te='王霞')

    def test_workExperiences(self):
        r = workExperiences(userToken, )
        assert_equal(1, r.get('state'), '校验提交工作经历', te='王霞')

    def test_educationExperiences(self):
        r = educationExperiences(userToken)
        assert_equal(1, r.get('state'), "校验提交教育经历成功", te='王霞')

    def test_personalCards(self):
        r = personalCards(userToken)
        assert_equal(1, r.get('state'), '校验提交个人名片成功', te='王霞')

    def test_abilityLabels(self):
        r = abilityLabels(userToken)
        assert_equal(1, r.get('state'), '校验提交综合能力成功', te='王霞')

    def test_expectJob(self):
        r = expectJob(userToken)
        assert_equal(1, r.get('state'), '校验提交求职意向', te='王霞')

    def test_get_info(self):
        time.sleep(1)
        r = get_info(userToken)
        assert_equal(1, r.get('state'), '获取C端用户信息', te='王霞')

    def test_get_detail(self):
        r = get_detail(userToken)
        assert_equal(1, r.get('state'), "校验获取简历详情页面成功", te='王霞')
        global ed_id, wk_id
        ed_id = r['content']['educationExperiences'][0]['id']
        wk_id = r['content']['workExperiences'][0]['id']

    def test_delete_education_experiences(self):
        r = delete_education_experiences(userToken, ed_id)
        assert_equal(2105005, r.get('state'), '校验删除唯一段教育经历成功', te='王霞')

    @pytest.mark.parametrize("schoolName,education,startDate,endDate",
                             [('陕西文理大学', '硕士', '2014.09', '2017.07')])
    def test_update_educationExperiences(self, schoolName, education, startDate, endDate):
        r = educationExperiences(userToken=userToken, schoolName=schoolName, education=education, startDate=startDate,
                                 endDate=endDate)
        assert_equal(1, r.get('state'), '校验增加一段教育经历成功', te='王霞')

    def test_delete_education_experiences_2(self):
        r = delete_education_experiences(userToken, ed_id)
        assert_equal(1, r.get('state'), '校验删除一段教育经历成功', te='王霞')

    def test_delete_workExperiences(self):
        r = delete_workExperiences(userToken, wk_id)
        assert_equal(2105005, r.get('state'), '校验删除唯一段工作经历成功', te='王霞')

    @pytest.mark.parametrize("companyName,startDate,endDate", [("杰威尔音乐有限公司销售事业部", "2013.07", "2015.09")])
    def test_update_workExperiences(self, companyName, startDate, endDate):
        r = workExperiences(userToken, companyName=companyName, startDate=startDate, endDate=endDate)
        assert_equal(1, r.get('state'), '校验增加一段工作经历成功', te='王霞')

    def test_delete_workExperiences_2(self):
        r = delete_workExperiences(userToken, wk_id)
        assert_equal(1, r.get('state'), '校验删除一段工作经历成功', te='王霞')
