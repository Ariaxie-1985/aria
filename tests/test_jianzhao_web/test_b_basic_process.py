# coding:utf-8
# @Time  : 2018-12-27 16:31
# @Author: Xiawang
import logging
import random
import time
import pytest
from api_script.jianzhao_web.b_basic.home_review_company_4 import passCompanyApprove
from api_script.jianzhao_web.b_basic.home_review_person_2 import passPersonApprove
from api_script.jianzhao_web.b_basic.toB_comleteInfo_3 import completeInfo_process
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import saveHR_process
from utils.read_file import get_yaml_test_data
from utils.util import assert_equal, login

test_data = get_yaml_test_data("test_b_basic_process.yaml")
phone = str(int(time.time()))[2:10]  # 生成8位数字的字符串
companyShortName = test_data['companyShortName'] + phone
companyFullName = test_data['companyFullName'] + phone
updateCompanyShortName = test_data['updateCompanyShortName'] + phone
userName = test_data['userName'] + phone


def setup_module(module):
    pass


def teardown_module(module):
    pass


@pytest.mark.parametrize(
    'phone, countryCode,companyShortName, companyFullName, userName, resumeReceiveEmail,updateCompanyShortName',
    [(phone, test_data['countryCode'], companyShortName, companyFullName, userName, test_data['resumeReceiveEmail'],
      updateCompanyShortName)])
def test_saveHR_process(phone, countryCode, companyShortName, companyFullName, userName, resumeReceiveEmail,
                        updateCompanyShortName):
    log = logging.getLogger('test_saveHR_process')
    log.info('验证注册B端-成立公司-提交招聘者审核流程是否成功')
    [r1, r2, r3, r4] = saveHR_process(phone, countryCode, companyShortName, companyFullName, userName,
                                      resumeReceiveEmail, updateCompanyShortName)

    assert_equal(1, r1['state'], "注册用户成功，该用户名: " + str(phone), "注册用户失败，该用户名: " + str(phone))
    assert_equal(1, r2['state'], "上传B端用户信息成功，该用户性名: " + str(userName), "上传B端用户信息失败，该用户性名: " + str(userName))
    assert_equal(1, r3['state'], "B端成立公司成功，该公司简称: " + str(companyShortName), "B端成立公司失败，该公司简称: " + str(companyShortName))
    assert_equal(1, r4['state'], "B端提交招聘者审核成功，该公司简称: " + str(updateCompanyShortName),
                 "B端提交招聘者审核失败，该公司简称: " + str(updateCompanyShortName))


def test_passPersonApprove(login_home_k8s_default):
    log = logging.getLogger('test_passPersonApprove')
    log.info('验证home后台-审核中心-个人认证-审核招聘者是否成功')
    r1, r2, r3 = passPersonApprove()
    assert_equal(True, r1['success'], "验证home后台-审核中心-个人认证-审核招聘者成功", "验证home后台-审核中心-个人认证-审核招聘者失败")


@pytest.mark.parametrize('phone', [(phone)])
def test_completeInfo_process(phone):
    login("00852", phone)
    log = logging.getLogger('test_completeInfo_process')
    log.info('验证B端提交申请认证公司流程是否成功')
    [r1, r2] = completeInfo_process()
    assert_equal(1, r1['state'], "上传营业执照成功", "上传营业执照失败")
    assert_equal(1, r2['state'], "B端申请认证公司成功", "B端申请认证公司失败")


def test_passCompanyApprove(login_home_k8s_default):
    log = logging.getLogger('test_passCompanyApprove')
    log.info('验证home后台-公司认证-审核公司是否成功')
    r = passCompanyApprove()
    assert_equal(True, r['success'], "home后台-公司认证-审核公司成功！", "home后台-公司认证-审核公司成功！")
