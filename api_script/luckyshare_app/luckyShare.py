# coding:utf-8
# @Time  : 2019-02-28 15:24
# @Author: Xiawang
from utils.util import get_app_header, get_requests

# host = "https://gate.lagou.com"
host = "http://10.1.201.110:12790"

headers = get_app_header(100014641)



def is_open_get():
	url = host + "/luckyShare/isOpen"
	remark = "查询活动入口是否展示"
	return get_requests(url=url, headers=headers, remark=remark)



is_open_get()
