# coding:utf-8
import logging
from api_script.util import form_post, get_header, get, login
import time

time = int(round(time.time() * 1000))

def get_userId():
	refer_queryUserId_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	queryUserId_url = "https://easy.lagou.com/member/all_members.json?_="+str(time)
	queryUserId_header = get_header(refer_queryUserId_url)
	remark = "获取需要添加的子账号"
	r = get(url=queryUserId_url, headers=queryUserId_header,remark=remark)
	members = r.json()['content']['data']['members']
	for i in range(len(members)):
		flag = members[i]
		if flag['isContractManager'] == False:
			userId = flag["userId"]
			if userId:
				logging.info("获取需要添加的子账号成功, 其userId: " + str(userId))
				return userId





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
	removeAcount_url = "https://easy.lagou.com/subAccount/delAcount.json"
	removeAcount_data = {"userId": userId}
	removeAcount_header = get_header(refer_queryAcount_url)
	remark = "移除子账号功能"
	return  form_post(url=removeAcount_url, data=removeAcount_data,headers=removeAcount_header,remark=remark)


def recover_sub_account(userId):
	'''
	一键恢复无效子账号功能, 前置条件是公司的合同已被停用
	:param userId: int, 子账号用户id
	:return: string， 删除结果
	'''
	refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	recoverAcount_url = "https://easy.lagou.com/subAccount/recoverSubAccount.json"
	recoverAcount_data = {"userId": userId}
	recoverAcount_header = get_header(refer_queryAcount_url)
	remark = "一键恢复无效子账号功能"
	return  form_post(url=recoverAcount_url, data=recoverAcount_data,headers=recoverAcount_header,remark=remark)

