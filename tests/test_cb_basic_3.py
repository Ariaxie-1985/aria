# coding:utf-8
# @Time  : 2018-12-27 16:31
# @Author: Xiawang
import logging
import pytest


from api_script.b_basic.toB_comleteInfo_3 import completeInfo_process
from api_script.b_basic.toB_saveHR_1 import saveHR_process
from util.read_yaml import get_yaml_test_data
from util.util import assert_equal, login

test_data = get_yaml_test_data("b_basic.yaml")


@pytest.mark.parametrize('phone',[(test_data['phone'])])
def test_completeInfo_process(phone):
	login("00852", phone)
	log = logging.getLogger('test_completeInfo_process')
	log.info('验证B端提交申请认证公司流程是否成功')
	[r1, r2] = completeInfo_process()
	assert_equal(1,r1['state'],"上传营业执照成功","上传营业执照失败")
	assert_equal(1,r2['state'],"B端申请认证公司成功","B端申请认证公司失败")
