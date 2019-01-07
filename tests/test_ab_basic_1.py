# coding:utf-8
# @Time  : 2018-12-27 16:31
# @Author: Xiawang
import logging
import pytest


from api_script.b_basic.toB_saveHR_1 import saveHR_process
from util.read_yaml import get_yaml_test_data
from util.util import assert_equal

test_data = get_yaml_test_data("b_basic.yaml")
@pytest.mark.parametrize('phone, companyShortName, companyFullName, userName, resumeReceiveEmail,updateCompanyShortName',
                         [(test_data['phone'],test_data['companyShortName'],test_data['companyFullName'],test_data['userName'],
                           test_data['resumeReceiveEmail'],test_data['updateCompanyShortName'])])
def test_saveHR_process(phone, companyShortName, companyFullName, userName, resumeReceiveEmail,updateCompanyShortName):
	log = logging.getLogger('test_saveHR_process')
	log.info('验证注册B端-成立公司-提交招聘者审核流程是否成功')
	[r1, r2, r3, r4] = saveHR_process(phone, companyShortName, companyFullName, userName, resumeReceiveEmail,updateCompanyShortName)
	assert_equal(1,r1['state'],"注册用户成功，该用户名: " + str(phone), "注册用户失败，该用户名: " + str(phone))
	assert_equal(1,r2['state'],"上传B端用户信息成功，该用户性名: " + str(userName), "上传B端用户信息失败，该用户性名: " + str(userName))
	assert_equal(1,r3['state'],"B端成立公司成功，该公司简称: " + str(companyShortName), "B端成立公司失败，该公司简称: " + str(companyShortName))
	assert_equal(1,r4['state'],"B端提交招聘者审核成功，该公司简称: " + str(updateCompanyShortName),
	             "B端提交招聘者审核失败，该公司简称: " + str(updateCompanyShortName))





