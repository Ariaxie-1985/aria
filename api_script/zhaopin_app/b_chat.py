# coding:utf-8
# @Time  : 2019-01-17 14:35
# @Author: Xiawang
from util.util import get_app_header, json_post, get_requests

host = "https://gate.lagou.com/v1/zhaopin"
headers = get_app_header(100014641)


def chat_invite_msg(positionId, userId):
	url = host + "/chat/invite_msg"
	data = {
		"positionId": positionId, "message": "您好，我对您的简历非常感兴趣, 可否发我简历进一步沟通呢？", "userId": userId
	}
	remark = "邀请投递"
	return json_post(url=url, data=data, headers=headers, remark=remark)


def chat_inspect_reports(ids):
	'''
	:param ids: list, C端用户的userid
	:return:
	'''
	url = host + "/chat/inspect/reports"
	data = {
		"ids": ids
	}
	remark = "谁看过我,标记已读"
	return json_post(url=url, data=data, headers=headers, remark=remark)


def chat_inspect_reports_all(createBy):
	'''
	:param createBy: int, 谁发起的:0全部，1我发起的，2对方发起的
	:return:
	'''
	url = host + "/chat/inspect/reports/all?createBy="+str(createBy)
	remark = "谁看过我,标记已读"
	return get_requests(url=url, headers=headers, remark=remark).json()


def chat_inspect_list():
	'''
	:param createBy: int, 谁发起的:0全部，1我发起的，2对方发起的
	:return:
	'''
	url = host + "/chat/inspect/list?pageSize=20"
	remark = "谁看过我"
	return get_requests(url=url, headers=headers, remark=remark).json()