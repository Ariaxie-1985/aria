# coding:utf-8
# @Time  : 2019-04-28 15:07
# @Author: Xiawang
from utils.util import app_header_999, get_requests


def member_all(userToken):
    url = 'https://gate.lagou.com/v1/zhaopin/bUser/member/all?pageNo=1&pageSize=15'
    header = app_header_999(userToken=userToken, DA=False)
    remark = '查看我公司下的成员'
    return get_requests(url=url, headers=header, remark=remark).json()


def quickReply_all(userToken):
    url = 'https://gate.lagou.com/v1/zhaopin/bUser/quickReply/all'
    header = app_header_999(userToken=userToken, DA=False)
    remark = '获取IM的快捷回复'
    return get_requests(url=url, headers=header, remark=remark).json()


def interviewTemplate_all(userToken):
    url = 'https://gate.lagou.com/v1/zhaopin/bUser/interviewTemplate/all'
    header = app_header_999(userToken=userToken, DA=False)
    remark = '查看面试信息'
    return get_requests(url=url, headers=header, remark=remark).json()
