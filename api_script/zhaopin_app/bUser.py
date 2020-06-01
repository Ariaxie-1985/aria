# coding:utf-8
# @Time  : 2019-04-28 15:07
# @Author: Xiawang
from utils.util import app_header_999, get_requests, json_post, delete_requests


def member_all(userToken, ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/zhaopin/bUser/member/all?pageNo=1&pageSize=15'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '查看我公司下的成员'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def quickReply_all(userToken):
    url = 'https://gate.lagou.com/v1/zhaopin/bUser/quickReply/all'
    header = app_header_999(userToken=userToken, DA=False)
    remark = '获取IM的快捷回复'
    return get_requests(url=url, headers=header, remark=remark)


def interviewTemplate_all(userToken, ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/zhaopin/bUser/interviewTemplate/all'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '查看面试信息'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def interviewTemplate_create_update(userToken, ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/zhaopin/bUser/interviewTemplate/update'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    data = {
        "id": 0,
        "ownerId": 0,
        "companyId": 0,
        "linkPhone": "17700000001",
        "linkMan": "王子",
        "address": "北京市海淀区海置创投大厦4楼"
    }
    remark = '创建面试信息'
    return json_post(url=url, headers=header, data=data, remark=remark, ip_port=ip_port)


def interviewTemplate_del(userToken, templateId, ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/zhaopin/bUser/interviewTemplate/del?templateId={}'.format(templateId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '删除面试信息'
    return delete_requests(url=url, headers=header, remark=remark, ip_port=ip_port)
