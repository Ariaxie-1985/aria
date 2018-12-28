# coding:utf-8
# @Time  : 2018-12-27 16:31
# @Author: Xiawang
import logging

import pytest

from api_script.b_basic.home_review_person import passPersonApprove
from api_script.b_basic.toB_comleteInfo import completeInfo_process
from api_script.b_basic.toB_saveHR import saveHR_process
from util.util import login_home, login, assert_equal

# 需注册的B端账号
phone = 20000219
# 登录home后台
username_home = 'anan@lagou.com'
password_home = "990eb670f81e82f546cfaaae1587279a"


@pytest.mark.order1
class Test_saveHR_process(object):
	def test_saveHR_process(self):
		log = logging.getLogger('test_add_sub_account')
		log.info('验证注册B端-成立公司-提交招聘者审核流程是否成功')
		userName = "英皇容祖儿6"
		companyFullName = "英网测试拉勾6"
		resumeReceiveEmail = "test2018@sina.com"
		companyShortName = "英网测试6"
		updateCompanyShortName = "英皇容祖儿网测试6"
		[r1, r2, r3, r4] = saveHR_process(phone, companyShortName, companyFullName, userName, resumeReceiveEmail,
		                                  updateCompanyShortName)
		assert_equal(r1['state'],1,"注册用户成功，该用户名: " + str(phone),"注册用户失败，该用户名: " + str(phone))
		assert_equal(r2['state'],1,"上传B端用户信息成功，该用户性名: " + str(userName),"上传B端用户信息失败，该用户性名: " + str(userName))
		assert_equal(r3['state'],1,"B端成立公司成功，该公司简称: " + str(companyShortName),"B端成立公司失败，该公司简称: " + str(companyShortName))
		assert_equal(r4['state'],1,"B端提交招聘者审核成功，该公司简称: " + str(updateCompanyShortName),"B端提交招聘者审核失败，该公司简称: " + str(updateCompanyShortName))


@pytest.mark.order2
class Test_passPersonApproveClass(object):
	login_home(username_home, password_home)

	def test_passPersonApprove(self):
		log = logging.getLogger('test_passPersonApprove')
		log.info('验证home后台-审核中心-个人认证-审核招聘者是否成功')
		r = passPersonApprove()
		assert r['success'] == True
		if r['success'] == True:
			log.info("验证home后台-审核中心-个人认证-审核招聘者成功")

	def test_completeInfo(self):
		log = logging.getLogger('test_completeInfo')
		log.info('验证home后台-审核中心-个人认证-审核招聘者是否成功')
		r = passPersonApprove()
		assert r['success'] == True
		if r['success'] == True:
			log.info("验证home后台-审核中心-个人认证-审核招聘者成功")


@pytest.mark.order3
class Test_completeInfo_process(object):

	login("00852", phone)

	def test_completeInfo_process(self):
		log = logging.getLogger('test_completeInfo_process')
		log.info('验证B端提交申请认证公司流程是否成功')
		[r1, r2] = completeInfo_process()
		assert r1['state'] == 1
		if r1['state'] == 1:
			log.info("上传营业执照成功")
		assert r2['state'] == 1
		if r2['state'] == 1:
			log.info("B端申请认证公司成功")


@pytest.mark.order4
class Test_passCompanyApprove(object):

	login("00852", phone)

	def test_passCompanyApprove(self):
		log = logging.getLogger('test_passCompanyApprove')
		log.info('验证home后台-公司认证-审核公司是否成功')
		r = completeInfo_process()
		assert r['state'] == 1
		if r['state'] == 1:
			log.info("home后台-公司认证-审核公司成功！")
