# coding:utf-8
# @Time  : 2019-01-23 16:07
# @Author: Xiawang
from utils.util import get_requests, form_post


def interview_index():
	'''
	简历管理-面试日程页面
	:return:
	'''
	url = "https://easy.lagou.com/interview/index.htm"
	return get_requests(url=url)


def interview_list():
	url = "https://easy.lagou.com/interview/new/list.json"
	data = {
		"sign" : False,
		"pageNo": 1,
		"pageSize": 20,
		"notlnterview" : False,
		"range" : 0
	}
	header = {}
	remark = "面试签到列表"
	return form_post(url=url, data=data, headers=header, remark=remark)


def interview_sign():
	'''
	简历管理-面试日程-面试签到设置主页面
	:return:
	'''
	url = "https://easy.lagou.com/interview/sign.htm"
	return get_requests(url=url)


def interview_setting_save():
	url = "https://easy.lagou.com/interview/setting_save.json"
	data = {
		"companyName": "拉勾测试公司1",
		"logo": "https://yun.lagou.com/null",
		"settinggld": "4"
	}
	header = {}
	remark = "保存面试签到设置"
	return form_post(url=url, data=data, headers=header, remark=remark)


def interview_get_code():
	url = "https://easy.lagou.com/interview/get_code.json"
	remark = "获取公开码和二维码"
	return form_post(url=url, data=None, headers={}, remark=remark)


def interview_resetCode():
	url = "https://easy.lagou.com/interview/resetCode.json"
	data = {
		"[object Object]": ""
	}
	remark = "重置公开链接码"
	return form_post(url=url, data=data, headers={}, remark=remark)
