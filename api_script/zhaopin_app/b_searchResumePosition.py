# coding:utf-8
# @Time  : 2019-01-17 10:47
# @Author: Xiawang
from util.util import get_app_header, get_requests

host = "https://gate.lagou.com/v1/zhaopin"
headers = get_app_header(100014641)


def get_strict_pages_positions():
	url = host + "/orderResumes/positions/strict/pages?pageNo=1&pageSize=20"
	remark = "分页查询用于简历查询的职位（排除没有拉勾职位id的职位）"
	return get_requests(url=url, headers=headers,remark=remark).json()


def get_strict_pages_orderResumes():
	url = host + "/orderResumes/positions/pages?pageNo=1&pageSize=20"
	remark = "分页查询用于简历查询的职位"
	return get_requests(url=url, headers=headers,remark=remark).json()
