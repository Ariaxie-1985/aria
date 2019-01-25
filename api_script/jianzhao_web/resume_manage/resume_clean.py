# coding:utf-8
# @Time  : 2019-01-23 18:19
# @Author: Xiawang
from util.util import get_code_token, form_post, get_requests


def can_new_index():
	url = "https://easy.lagou.com/can/new/index.htm"
	return get_requests(url=url)


def can_new_clean():
	url = "https://easy.lagou.com/can/new/clean.json"
	data = {
		"stages": "NEW",
		"days": "30"
	}
	header = get_code_token(
		"https://easy.lagou.com/can/index.htm?can=true&stage=NEW&needQueryAmount=true&newDeliverTime=0")
	remark = "清理30天内的新简历"
	return form_post(url=url, data=data, headers=header, remark=remark)
