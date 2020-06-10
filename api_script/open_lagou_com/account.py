# coding:utf-8
# @Time  : 2020/6/2 10:53
# @Author: Xiawang
# Description:
from utils.util import get_requests


def openid_query(access_token, credential):
    url = 'https://open.lagou.com/v1/account/openid/query'
    data = {'access_token': access_token, 'credential': credential}
    remark = '根据账号查询其openid'
    return get_requests(url=url, data=data, remark=remark)


def openid_list(access_token):
    url = 'https://open.lagou.com/v1/account/openid/list'
    data = {'access_token': access_token, 'page_size': 200, 'page_no': 1}
    remark = '获取全公司所有人的openid'
    return get_requests(url=url, data=data, remark=remark)
