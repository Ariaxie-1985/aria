# coding:utf-8
# @Time  : 2019-01-17 14:56
# @Author: Xiawang
from utils.util import json_post, app_header_999

host = "https://gate.lagou.com/v1/zhaopin"


def goods_product_version(userToken, userId=None, ip_port=None):
    url = host + "/goods/product_version"
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "获取当前用户商业产品版本号"
    return json_post(url=url, headers=header, remark=remark, ip_port=ip_port)
