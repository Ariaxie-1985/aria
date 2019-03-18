# coding:utf-8
# @Time  : 2019-01-17 14:56
# @Author: Xiawang
from utils.util import get_app_header, json_post

host = "https://gate.lagou.com/v1/zhaopin"
headers = get_app_header(84)


def goods_product_version():
	url = host + "/goods/product_version"
	remark = "获取当前用户商业产品版本号"
	return json_post(url=url, headers=headers, remark=remark)


# yq新增:2019.2.16
def getPopUpData():
	url = host+'/probation/getPopUpData'
	remark = '试用期弹窗'
	return json_post(url=url, headers=headers, remark=remark)

def getRightsList ():
	url = host+'/rights/getRightsList'
	remark = '查询我的权益'
	return json_post(url=url, headers=headers, remark=remark)

def getUserInfo ():
	url = host+'/userInfo/getUserInfo'
	remark = '获取用户信息'
	return json_post(url=url, headers=headers, remark=remark)

# getPopUpData()
# getRightsList()
# getUserInfo()
