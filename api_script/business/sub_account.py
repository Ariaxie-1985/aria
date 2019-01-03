# coding:utf-8
import logging
from util.util import form_post, get_header, get_, login
import time

time = int(round(time.time() * 1000))


def get_userinfo():
	refer_queryUserId_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	queryUserId_url = "https://easy.lagou.com/member/all_members.json?_=" + str(time)
	queryUserId_header = get_header(refer_queryUserId_url)
	remark = "验证获取需要添加的子账号是否ok"
	r = get_(url=queryUserId_url, headers=queryUserId_header, remark=remark).json()
	members = r['content']['data']['members']
	for i in range(len(members)):
		flag = members[i]
		if flag['isContractManager'] == False:
			if flag["userId"]:
				logging.info("获取需要添加的子账号成功, 其userId: " + str(flag["userId"]))
				return [flag["userId"], flag["portrait"], flag["name"]]


def get_goodsList():
	refer_queryUserId_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	querygoodsList_url = "https://easy.lagou.com/subAccount/queryAcount.json?pageNo=1&pageSize=7&keyword="
	querygoodsList_header = get_header(refer_queryUserId_url)
	remark = "获取权益类别id"
	r = get_(url=querygoodsList_url, headers=querygoodsList_header, remark=remark).json()
	goodsList = r['content']['data']['goodsList']
	if len(goodsList) > 2:
		return [goodsList[0], goodsList[1]]


def get_invalidUserId():
	refer_queryUserId_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	querygoodsList_url = "https://easy.lagou.com/subAccount/queryAcount.json?pageNo=1&pageSize=7&keyword="
	querygoodsList_header = get_header(refer_queryUserId_url)
	remark = "获取权益类别id"
	r = get_(url=querygoodsList_url, headers=querygoodsList_header, remark=remark).json()
	userid = r['content']['data']['subAcccountList'][0]['userid']
	return userid

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
	remark = "验证增加子账号功能是否ok"
	return form_post(url=queryAcount_url, data=queryAcount_data, headers=queryAcount_header, remark=remark, )


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
	remark = "验证移除子账号功能是否ok"
	return form_post(url=removeAcount_url, data=removeAcount_data, headers=removeAcount_header, remark=remark)


def recover_sub_account(userId):
	'''
	一键恢复无效子账号功能, 前置条件是公司的合同已被停用,再添加新的合同
	:param userId: int, 子账号用户id
	:return: string， 删除结果
	'''
	refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	recoverAcount_url = "https://easy.lagou.com/subAccount/recoverSubAccount.json"
	recoverAcount_data = {"userIds": userId}
	recoverAcount_header = get_header(refer_queryAcount_url)
	remark = "验证一键恢复无效子账号功能是否ok"
	return form_post(url=recoverAcount_url, data=recoverAcount_data, headers=recoverAcount_header, remark=remark)


def reAssignAllGoods(userId,portrait,name,goodslist):
	refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	recoverAcount_url = "https://easy.lagou.com/subAccount/recoverSubAccount.json"
	# todo 解决传参里带列表嵌套字典
	recoverAcount_data = {"accountType": 1, "userId": userId,
	                      "assignInfo": [
		                      {"userid": userId, "portrait": portrait[0],"userName": name, "email": "",
		                       "baseGoodsId": goodslist[0], "totalNum": "0", "num": "0","reAssignNum": "1"},
		                      {"userid": userId, "portrait": portrait[1],"userName": name, "email": "",
		                       "baseGoodsId": goodslist[1], "totalNum": "0", "num": "0","reAssignNum": "1"}
		                     ]}
	recoverAcount_header = get_header(refer_queryAcount_url)
	remark = "验证调整子账号为分账号且及其权益功能是否ok"
	return form_post(url=recoverAcount_url, data=recoverAcount_data, headers=recoverAcount_header, remark=remark)


username = 20181205
login("00852",username)
userId = get_invalidUserId()
# goodslist = get_goodsList()
# add_sub_account(userId[0])
# reAssignAllGoods(userId[0],userId[1],userId[2],goodslist)
recover_sub_account(userId)
