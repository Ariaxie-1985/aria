# coding:utf-8
# @Time  : 2019-05-14 16:30
# @Author: Xiawang
from utils.util import get_app_header, get_requests, json_post

host = 'https://gate.lagou.com/v1/zhaopin/'


def integral_recruitcard_pop(userId):
    url = host + '/integral/mall/recruitcard/pop'
    header = get_app_header(userId=userId)
    remark = '是否弹出直招卡弹窗'
    return get_requests(url=url, headers=header, remark=remark)


