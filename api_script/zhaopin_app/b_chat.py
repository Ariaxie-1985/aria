# coding:utf-8
# @Time  : 2019-01-17 14:35
# @Author: Xiawang
from utils.util import get_requests, app_header_999


def chat_c_info(userToken, cUserId):
    url = 'https://gate.lagou.com/v1/zhaopin/chat/cinfo?cUserId={}'.format(cUserId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "获取C端用户信息"
    return get_requests(url=url, headers=header, remark=remark)


def chat_c_lastResume(userToken, cUserId, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/zhaopin/chat/lastResume/{}'.format(cUserId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "获取候选人最近一次投递状态"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


def chat_inspect_list(userToken):
    url = "https://gate.lagou.com/v1/zhaopin/chat/inspect/list?pageSize=20&lastInspectId=&showId="
    header = app_header_999(userToken=userToken, DA=False)
    remark = "谁看过我"
    return get_requests(url=url, headers=header, remark=remark)


def chat_position(userToken, cUserId, positionId):
    url = "https://gate.lagou.com/v1/zhaopin/chat/position?cUserId={}&positionId={}".format(cUserId, positionId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "获取IM在沟通的职位"
    return get_requests(url=url, headers=header, remark=remark)


def chat_interview_check(userToken, resumeId):
    url = "https://gate.lagou.com/v1/zhaopin/chat/interview/check?resumeId={}".format(resumeId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "检查IM是否能邀约面试"
    return get_requests(url=url, headers=header, remark=remark)
