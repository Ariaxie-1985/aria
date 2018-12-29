# coding:utf-8
# @Time  : 2018-12-29 14:23
# @Author: Xiawang
import logging
import pytest

from api_script.b_basic.home_review_person import passPersonApprove
from util.read_yaml import get_yaml_test_data
from util.util import login_home, assert_equal

test_data = get_yaml_test_data("b_basic.yaml")
print (test_data)

@pytest.mark.parametrize('username_home,password_home',[(test_data['username_home'],test_data['password_home'])])
def test_passPersonApprove(username_home,password_home):
	login_home(username_home,password_home)
	log = logging.getLogger('test_passPersonApprove')
	log.info('验证home后台-审核中心-个人认证-审核招聘者是否成功')
	r = passPersonApprove()
	assert_equal(True,r['success'],"验证home后台-审核中心-个人认证-审核招聘者成功","验证home后台-审核中心-个人认证-审核招聘者失败")
