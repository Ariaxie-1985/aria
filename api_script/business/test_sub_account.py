# coding:utf-8

from api_script.util import login, get_code_token, form_post
import sys, os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
username = 20181205
login("00852",username)

userId = 100014642


def add_sub_account(userId):
	'''
	增加子账号功能
	:param userId: int, 子账号用户id
	:return: int, 请求返回结果的用户id
	'''
	refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	queryAcount_url = "https://easy.lagou.com/subAccount/addAcount.json"
	queryAcount_data = {"userId": userId}
	queryAcount_header = get_code_token(refer_queryAcount_url)
	r = form_post(queryAcount_url, queryAcount_data, queryAcount_header)
	return r['content']['data']['data'][0]['userid']

def test_add_sub_account():
	assert add_sub_account(100014642) == 100014642

def remove_sub_account(userId):
	'''
	移除子账号功能
	:param userId: int, 子账号用户id
	:return: int, 请求返回结果的用户id
	'''
	refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	queryAcount_url = "https://easy.lagou.com/subAccount/delAcount.json"
	queryAcount_data = {"userId": userId}
	queryAcount_header = get_code_token(refer_queryAcount_url)
	r = form_post(queryAcount_url, queryAcount_data, queryAcount_header)
	return r['content']['data']['data'][0]['userid']

def test_remove_sub_account():
	assert add_sub_account(100014642) == 100014642

