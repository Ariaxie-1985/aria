# coding:utf-8
# @Time  : 2019-01-17 14:56
# @Author: Xiawang
from util.util import get_app_header, json_post

host = "https://gate.lagou.com/v1/zhaopin"
headers = get_app_header(100014641)


def goods_product_version():
	url = host + "/goods/product_version"
	remark = "获取当前用户商业产品版本号"
	return json_post(url=url, headers=headers, remark=remark)
