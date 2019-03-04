# coding:utf-8
# @Author: cloudyyuan
from api_script.jianzhao_web.talent_communication.Talent import allRead, quickReplyList, greetingList, quickReplySave, \
	quickReplyTop, Save
from utils.util import login, get_code_token, form_post, get_header, get_requests, assert_equal

'''
人才沟通
'''


def setup_module(module):
	pass

def teardown_module(module):
	pass


def test_list(login_web_k8s_env_b):
	'''
	获取会话列表
	:return:
	'''
	list()
	'''
	全部标记已读
	:return:
	'''
	allRead()
	'''
	快捷回复列表
	:return:
	'''
	quickReplyList()
	'''
	招呼模版列表
	:return:
	'''
	greetingList()
	'''
	快捷回复添加、修改,删除
	:return:
	'''
	quickReplySave()
	'''
	快捷回复置顶
	:return:
	'''
	quickReplyTop()
	'''
	添加快捷回复模版，不填写id即可
	:return:
	'''
	Save()
