# coding:utf-8
# @Time  : 2018-12-27 16:31
# @Author: Xiawang
import logging

from api_script.b_basic.home_review_person import passPersonApprove
from api_script.b_basic.toB_comleteInfo import completeInfo_process
from api_script.b_basic.toB_saveHR import saveHR_process
from api_script.util import login_home, login

phone = 20000218
def test_saveHR_process(phone):
	log = logging.getLogger('test_add_sub_account')
	log.info('验证注册B端-成立公司-提交招聘者审核流程是否成功')
	userName = "英皇容祖儿6"
	companyFullName = "英网测试拉勾6"
	resumeReceiveEmail = "test2018@sina.com"
	companyShortName = "英网测试6"
	updateCompanyShortName = "英皇容祖儿网测试6"
	[r1,r2,r3,r4] = saveHR_process(phone,companyShortName,companyFullName,userName,resumeReceiveEmail,updateCompanyShortName)
	assert r1['state'] == 1
	if r1['state'] == 1:
		log.info("注册用户成功，该用户名: "+str(phone))
	assert r2['state'] == 1
	if r2['state'] == 1:
		log.info("上传B端用户信息成功，该用户性名: "+str(userName))
	assert r3['state'] == 1
	if r3['state'] == 1:
		log.info("B端成立公司成功，该公司简称: "+str(companyShortName))
	assert r4['state'] == 1
	if r4['state'] == 1:
		log.info("B端提交招聘者审核成功，该公司简称: " + str(updateCompanyShortName))


# 登录home后台
username_home = 'anan@lagou.com'
password_home = "990eb670f81e82f546cfaaae1587279a"
login_home(username_home,password_home)

def test_passPersonApprove():
	log = logging.getLogger('test_passPersonApprove')
	log.info('验证home后台-审核中心-个人认证-审核招聘者是否成功')
	r = passPersonApprove()
	assert r['success'] == True
	if r['success'] == True:
		log.info("验证home后台-审核中心-个人认证-审核招聘者成功")


def test_completeInfo():
	log = logging.getLogger('test_completeInfo')
	log.info('验证home后台-审核中心-个人认证-审核招聘者是否成功')
	r = passPersonApprove()
	assert r['success'] == True
	if r['success'] == True:
		log.info("验证home后台-审核中心-个人认证-审核招聘者成功")

login("00852",phone)

def test_completeInfo_process():
	log = logging.getLogger('test_completeInfo_process')
	log.info('验证B端提交申请认证公司流程是否成功')
	[r1,r2] = completeInfo_process()
	assert r1['state'] == 1
	if r1['state'] == 1:
		log.info("上传营业执照成功")
	assert r2['state'] == 1
	if r2['state'] == 1:
		log.info("B端申请认证公司成功")
