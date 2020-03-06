# coding:utf-8
# @Time  : 2020/2/26 18:41
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests, json_post


def get_vip_detail(userToken):
    url = "https://gate.lagou.com/v1/zhaopin/vip/vipDetail"
    header = app_header_999(userToken=userToken, DA=False)
    remark = "获取拉勾VIP模板详情"
    return get_requests(url=url, headers=header, remark=remark).json()



def post_vip_detail(userToken):
    url = "https://gate.lagou.com/v1/zhaopin/vip/vipDetail"
    header = app_header_999(userToken=userToken, DA=False)
    remark = "获取拉勾VIP模板详情"
    return json_post(url=url, headers=header, remark=remark)