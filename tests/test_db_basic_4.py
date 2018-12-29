# coding:utf-8
# @Time  : 2018-12-29 14:23
# @Author: Xiawang
import logging
import pytest

from api_script.b_basic.home_review_person import passPersonApprove
from api_script.b_basic.toB_comleteInfo import completeInfo_process
from util.read_yaml import get_yaml_test_data
from util.util import login_home, assert_equal

test_data = get_yaml_test_data("b_basic.yaml")


@pytest.mark.parametrize('username_home,password_home',[(test_data['username_home'],test_data['password_home'])])
def test_passCompanyApprove(username_home,password_home):
	login_home(username_home,password_home)
	log = logging.getLogger('test_passCompanyApprove')
	log.info('验证home后台-公司认证-审核公司是否成功')
	r = completeInfo_process()
	assert_equal(1,r['state'],"home后台-公司认证-审核公司成功！","home后台-公司认证-审核公司成功！")
