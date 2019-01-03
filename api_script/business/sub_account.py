# coding:utf-8
# @Author: Xiawang
import json
import logging
from util.util import form_post, get_header, get_requests, login
import time

time = int(round(time.time() * 1000))


def get_userId():
	'''
	查询需要的账号信息
	:return:userId用户id, portrait头像, name用户姓名
	'''
	userId_list = []
	refer_queryUserId_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	queryUserId_url = "https://easy.lagou.com/member/all_members.json?_=" + str(time)
	queryUserId_header = get_header(refer_queryUserId_url)
	remark = "获取需要添加的子账号id"
	r = get_requests(url=queryUserId_url, headers=queryUserId_header, remark=remark).json()
	members = r['content']['data']['members']
	for i in range(len(members)):
		flag = members[i]
		if flag['isContractManager'] == False:
			userId_list.append(flag['userId'])
	logging.info("获取到的子账号id: " + str(userId_list))
	return userId_list


def get_user_goods_info(userIdlist):
	'''
	获取调整的子账号的用户名称、头像、权益id
	:param userIdlist: list
	:return:
	'''
	userlist = {}
	goods_list = []
	for userId in userIdlist:
		querygoodsList_url = "https://easy.lagou.com/userGoodsRecord/queryAssignUserByUserId.json"
		querygoodsList_header = {}
		querygoodsList_data = {'userId': userId}
		remark = "获取调整的子账号的用户名称、头像、权益id"
		r = form_post(url=querygoodsList_url, headers=querygoodsList_header, data=querygoodsList_data, remark=remark)
		portrait = r['content']['data']['portrait']
		name = r['content']['data']['userName']
		userlist[userId] = [portrait, name]
		if r['content']['data']['info'][0]['baseGoodsName'] != "子账号数":
			if r['content']['data']['info'][1]['baseGoodsName'] != "子账号数":
				goods_list.append(r['content']['data']['info'][0]['baseGoodsId'])
				goods_list.append(r['content']['data']['info'][1]['baseGoodsId'])
				userlist[userId].append(goods_list)
	return userlist


def get_subaccunt_goods(userIdlist):
	goods_list = {}
	for userId in userIdlist:
		querygoodsList_url = "https://easy.lagou.com/userGoodsRecord/queryAssignUserByUserId.json"
		querygoodsList_header = {}
		querygoodsList_data = {'userId': userId}
		remark = "获取子账号调整为分账号的权益id"
		r = form_post(url=querygoodsList_url, headers=querygoodsList_header, data=querygoodsList_data, remark=remark)
		portrait = r['content']['data']['portrait']
		name = r['content']['data']['userName']
		if r['content']['data']['info'][-1]['baseGoodsName'] == "子账号数":
			goods_list[userId] = [portrait, name, r['content']['data']['info'][-1]['baseGoodsId']]
		elif r['content']['data']['info'][-2]['baseGoodsName'] == "子账号数":
			goods_list[userId] = [portrait, name, r['content']['data']['info'][-2]['baseGoodsId']]
		else:
			return ("没有子账号权益id")
	print(goods_list)
	return goods_list


def get_invalidUserId():
	refer_queryUserId_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	querygoodsList_url = "https://easy.lagou.com/subAccount/queryAcount.json?pageNo=1&pageSize=7&keyword="
	querygoodsList_header = get_header(refer_queryUserId_url)
	remark = "获取权益类别id"
	r = get_requests(url=querygoodsList_url, headers=querygoodsList_header, remark=remark).json()
	userid = r['content']['data']['subAcccountList'][0]['userid']
	return userid


def add_sub_account(userlist):
	'''
	增加子账号功能
	:param userId: int, 子账号用户id
	:return: int, 请求返回结果的用户id
	'''
	for userId in userlist:
		refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
		queryAcount_url = "https://easy.lagou.com/subAccount/addAcount.json"
		queryAcount_data = {"userId": userId}
		queryAcount_header = get_header(refer_queryAcount_url)
		remark = "验证增加子账号功能是否ok"
		r = form_post(url=queryAcount_url, data=queryAcount_data, headers=queryAcount_header, remark=remark)
	return r

def remove_sub_account(userlist):
	'''
	移除子账号功能
	:param userId: int, 子账号用户id
	:return: string， 删除结果
	'''
	for userId in userlist:
		# refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
		removeAcount_url = "https://easy.lagou.com/subAccount/delAcount.json"
		removeAcount_data = {"userId": userId}
		removeAcount_header = {}
		remark = "验证移除子账号功能是否ok"
		r = form_post(url=removeAcount_url, data=removeAcount_data, headers=removeAcount_header, remark=remark)
	return r


def recover_sub_account(userId):
	'''
	一键恢复无效子账号功能, 前置条件是公司的合同已被停用,再添加新的合同
	:param userId: int, 子账号用户id
	:return: string， 删除结果
	'''

	# refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
	recoverAcount_url = "https://easy.lagou.com/subAccount/recoverSubAccount.json"
	recoverAcount_data = {"userIds": userId}
	recoverAcount_header = {}
	remark = "验证一键恢复无效子账号功能是否ok"
	return form_post(url=recoverAcount_url, data=recoverAcount_data, headers=recoverAcount_header, remark=remark)



def reAssignAllGoods(userlist):
	'''
	调整子账号的权益
	:param userId: 子账号的userId
	:param portrait:
	:param name:
	:param goodslist:
	:return:
	'''
	recoverAcount_url = "https://easy.lagou.com/userGoodsRecord/reAssignAllGoods.json"
	for user, info in userlist.items():
		recoverAcount_data = {"accountType": 1, "userId": user,
		                      "assignInfo": [
			                      {"userid": user, "portrait": info[0], "userName": info[1], "email": "",
			                       "baseGoodsId": info[2][0], "totalNum": "0", "num": "0", "reAssignNum": "10"},
			                      {"userid": user, "portrait": info[0], "userName": info[1], "email": "",
			                       "baseGoodsId": info[2][1], "totalNum": "0", "num": "0", "reAssignNum": "10"}
		                      ]}
		recoverAcount_data["assignInfo"] = json.dumps(recoverAcount_data["assignInfo"])
		recoverAcount_header = {}
		remark = "验证调整子账号为分账号且及其权益功能是否ok"
		r =form_post(url=recoverAcount_url, data=recoverAcount_data, headers=recoverAcount_header, remark=remark)
	return r



def reAssign_subaccount_Goods(userlist):
	'''
	调整子账号为分账号
	:param userId: 子账号的userId
	:param portrait:
	:param name:
	:param goodslist:
	:return:
	'''
	recoverAcount_url = "https://easy.lagou.com/userGoodsRecord/reAssignAllGoods.json"
	for user, info in userlist.items():
		recoverAcount_data = {"accountType": 1, "userId": user,
		                      "assignInfo": [{"userid": user, "portrait": info[0], "userName": info[1], "email": "",
		       "baseGoodsId": info[2], "totalNum": "0", "num": "0", "reAssignNum": "10"}]}


		recoverAcount_data["assignInfo"] = json.dumps(recoverAcount_data["assignInfo"])
		recoverAcount_header = {}
		remark = "验证调整子账号为分账号且及其权益功能是否ok"
		r = form_post(url=recoverAcount_url, data=recoverAcount_data, headers=recoverAcount_header, remark=remark)
	return r

# username = 20181205
# login("00852", username)
# userid = get_userId()
# r = get_user_goods_info(userid)
# # s = reAssignAllGoods(r)
# userlist = get_subaccunt_goods(userid)
# reAssign_subaccount_Goods(userlist)
# userinfo = get_userId()
# userId = get_invalidUserId()
# goodslist = get_goodsList()
# add_sub_account(userId[0])
# reAssignAllGoods(userinfo[0],userinfo[1],userinfo[2],goodslist)
# recover_sub_account(userId)
