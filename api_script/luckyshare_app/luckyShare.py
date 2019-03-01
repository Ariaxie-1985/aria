# coding:utf-8
# @Time  : 2019-02-28 15:24
# @Author: Xiawang
from utils.util import get_app_header, get_requests, json_post

# host = "https://gate.lagou.com"
host = "http://10.1.201.110:12790"

headers = get_app_header(100014641)


def is_open_get():
    url = host + "/luckyShare/isOpen"
    remark = "查询活动入口是否展示"
    return get_requests(url=url, headers=headers, remark=remark)


def queryCard():
    url = host + "/luckyShare/queryCard"
    remark = "查询锦鲤卡片信息"
    return get_requests(url=url, headers=headers, remark=remark)


def queryRedPointType():
    # todo 确定订单id为英文
    url = host + "/luckyShare/queryRedPointType?id={}".format(1)
    remark = "查询红点"
    return get_requests(url=url, headers=headers, remark=remark)


def deleteRedPoint():
    # todo 参数未放在body里
    url = host + "/luckyShare/deleteRedPoint"
    remark = "删除红点"
    return json_post(url=url, headers=headers, remark=remark)


def interview_queryByIds():
    # todo 根据面试订单id查询订单信息
    url = host + "/interview/queryByIds?id={}".format(1)
    remark = "根据面试订单id查询订单信息"
    return get_requests(url=url, headers=headers, remark=remark)


def positions_queryByIds():
    # todo 根据职位id查询职位信息
    url = host + "/positions/queryByIds?id={}".format(1)
    remark = "根据职位id查询职位信息"
    return get_requests(url=url, headers=headers, remark=remark)


def positions_types():
    url = host + "/positions/types?id={}".format(1)
    remark = "获取所有的职位类型"
    return get_requests(url=url, headers=headers, remark=remark)


def queryExposePositions():
    # todo 查询职位曝光卡
    url = host + "/luckyShare/queryExposePositions?pageSize=20&page={}".format(1)
    remark = "查询面试曝光卡"
    return get_requests(url=url, headers=headers, remark=remark)


def queryHistoryNotes():
    url = host + "/luckyShare/queryHistoryNotes"
    remark = "查询历史晒贴"
    return get_requests(url=url, headers=headers, remark=remark)


def queryInterviews():
    url = host + "/luckyShare/queryInterviews"
    remark = "查询面试列表"
    return get_requests(url=url, headers=headers, remark=remark)


def queryNoteNeedMsg(orderId):
    url = host + "/luckyShare/queryNoteNeedMsg?=orderId={}".format(orderId)
    remark = "查询发帖所需信息"
    return get_requests(url=url, headers=headers, remark=remark)


def publicNote():
    # todo 确定参数化的字段
    url = host + "/luckyShare/publicNote"
    data = {
        "companyId": 0,
        "content": "string",
        "hrVo": {
            "impressionTags": [
                "string"
            ],
            "name": "string",
            "portrait": "string",
            "positionName": "string",
            "resumeDealLevel": "string",
            "userId": 0
        },
        "interviewId": 0,
        "interviewTime": "2019-02-28T02:33:38.750Z",
        "positionID": 0,
        "userName": "string"
    }
    remark = "晒邀约"
    return json_post(url=url, data=data, headers=headers, remark=remark)


def cms_luckyShare_querylist(userId, status):
    url = "http://home.lagou.com/cms/luckyShare/querylist.json?userId={}&status={}&startTime=111&endTime=22".format(
        userId, status)
    remark = "home后台锦鲤贴列表查询"
    return get_requests(url=url, headers=headers, remark=remark)


def cms_luckyShare_audit(ll_id, status):
    url = "http://home.lagou.com/cms/luckyShare/audit.json?"
    data = {
        "id": ll_id,
        "status": status
    }
    remark = "home后台锦鲤贴列表查询"
    return json_post(url=url, data=data, headers=headers, remark=remark)
