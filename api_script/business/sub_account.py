# coding:utf-8

from api_script.util import login, form_post, get_code_token, get_header, get
import time
import logging


username = 20181205
login("00852", username)

time = int(round(time.time() * 1000))

def get_userId():
	refer_queryUserId_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	queryUserId_url = "https://easy.lagou.com/member/all_members.json?_="+str(time)
	queryUserId_header = get_header(refer_queryUserId_url)
	remark = "获取需要添加的子账号"
	r = get(url=queryUserId_url, headers=queryUserId_header,remark=remark)
	print(r.json())
	userId = r.json()['content']['data']['members'][0]["userId"]
	if userId:
		("获取需要添加的子账号成功, 其userId: "+ str(userId))
	return userId

userId = get_userId()


def add_sub_account(userId):
	'''
	增加子账号功能
	:param userId: int, 子账号用户id
	:return: int, 请求返回结果的用户id
	'''
	refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	queryAcount_url = "https://easy.lagou.com/subAccount/addAcount.json"
	queryAcount_data = {"userId": userId}
	queryAcount_header = get_header(refer_queryAcount_url)
	remark = "增加子账号功能"
	return form_post(url=queryAcount_url, data=queryAcount_data, headers=queryAcount_header,remark=remark,)

def remove_sub_account(userId):
	'''
	移除子账号功能
	:param userId: int, 子账号用户id
	:return: string， 删除结果
	'''
	refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	queryAcount_url = "https://easy.lagou.com/subAccount/delAcount.json"
	queryAcount_data = {"userId": userId}
	queryAcount_header = get_header(refer_queryAcount_url)
	remark = "移除子账号功能"
	return  form_post(url=queryAcount_url, data=queryAcount_data,headers=queryAcount_header,remark=remark)


