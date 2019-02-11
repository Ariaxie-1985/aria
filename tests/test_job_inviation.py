# coding:utf-8
# @Author: cloudyyuan

'''
发布职位邀约
'''
from api_script.jianzhao_web.job_inviation.job_inviation import hot, invaitonnumber
from utils.util import login, get_code_token, form_post, get_header, get_requests, assert_equal


def setup_module(module):
	login('00852', '20181205')


def teardown_module(module):
	pass


def test_hot():
	'''
	判断是否是热门职位
	:return:
	'''
	hot()


def test_invaitonnumber():
	'''
	查询邀约候选人数量
	:return:
	'''
	invaitonnumber()
