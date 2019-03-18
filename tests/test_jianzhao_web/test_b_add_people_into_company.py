# coding:utf-8
# @Time  : 2019-01-07 15:28
# @Author: Xiawang

# coding:utf-8
# @Time  : 2018-12-27 16:31
# @Author: Xiawang
import logging
import random
import time

import pytest
from api_script.jianzhao_web.b_basic.home_review_person_2 import passPersonApprove
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import add_people_into_company
from utils.read_file import get_yaml_test_data
from utils.util import assert_equal, login_home

test_data = get_yaml_test_data("B_add_people_into_company.yaml")
phone = str(int(time.time())+random.randint(0,100))[2:10]  # 生成8位数字的字符串
userName = test_data['userName'] + phone


def setup_module(module):
    pass


def teardown_module(module):
    pass


@pytest.mark.parametrize('phone,countryCode,userName,companyFullName,resumeReceiveEmail',
                         [(phone, test_data['countryCode'], userName,
                           test_data['companyFullName'], test_data['resumeReceiveEmail'])])
def test_add_people_into_companyame(phone, countryCode, userName, companyFullName, resumeReceiveEmail):
    log = logging.getLogger('test_saveHR_process')
    log.info('验证注册B端-加入公司-提交招聘者审核流程是否成功')
    [r1, r2, r3, r4] = add_people_into_company(phone, countryCode, companyFullName, userName, resumeReceiveEmail)
    assert_equal(1, r1['state'], "注册用户成功，该用户名: " + str(phone), "注册用户失败，该用户名: " + str(phone))
    assert_equal(1, r2['state'], "上传B端用户信息成功，该用户性名: " + str(userName), "上传B端用户信息失败，该用户性名: " + str(userName))
    assert_equal(1, r3['state'], "加入公司成功，该公司全称: " + str(companyFullName), "加入公司失败，该公司简称: " + str(companyFullName))
    assert_equal(1, r4['state'], "提交招聘者审核成功，该用户的手机号: " + str(phone),
                 "提交招聘者审核失败，该用户的手机号: " + str(phone))


def test_passPersonApprove(login_home_k8s_default):
    log = logging.getLogger('test_passPersonApprove')
    log.info('验证home后台-审核中心-个人认证-审核招聘者是否成功')
    try:
        r1,r2,r3 = passPersonApprove()
        assert_equal(True, r1['success'], "验证home后台-审核中心-个人认证-审核招聘者成功", "验证home后台-审核中心-个人认证-审核招聘者失败")
    except Exception:
        assert_equal(True, False, "验证home后台-审核中心-个人认证-审核招聘者失败")

