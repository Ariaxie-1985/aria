# coding:utf-8
# @Time  : 2019-02-28 15:24
# @Author: Xiawang
from utils.util import get_app_header, get_requests, json_post

host = "https://gate.lagou.com/v1/entry"

headers = get_app_header(100014641)


def activity_carp_entrance(orderId=None):
    if orderId == None:
        url = host + "/activity/carp/entrance"
        remark = "查询活动入口是否展示"
        return get_requests(url=url, headers=headers, remark=remark)
    else:
        url = host + "/activity/carp/entrance?orderId={}".format(orderId)
        remark = "查询活动入口是否展示"
        return get_requests(url=url, headers=headers, remark=remark)


def activity_carp_summary():
    url = host + "/activity/carp/summary"
    remark = "查询活动简要信息"
    return get_requests(url=url, headers=headers, remark=remark)


def queryRedPointType(orderIds):
    if orderIds == None:
        url = host + "/activity/carp/queryRedPointType"
    else:
        url = host + "/activity/carp/queryRedPointType?orderIds={}".format(orderIds)
    remark = "查询红点"
    return get_requests(url=url, headers=headers, remark=remark)


def activity_carp_removeRedDot(type):
    url = host + "/activity/carp/removeRedDot"
    data = {
        "type": type
    }
    remark = "删除红点"
    return json_post(url=url, data=data, headers=headers, remark=remark)


def activity_carp_queryNotes(category1, category2, category3):
    url = host + "/activity/carp/queryNotes?pageNo=1&pageSize=20&category1={}&category2={}&category3={}".format(
        category1, category2,
        category3)
    remark = "查询帖子列表"
    return get_requests(url=url, headers=headers, remark=remark)


def order_interview_queryList(ids):
    if ids == None:
        url = host + "/order/interview/queryList"
    else:
        url = host + "/order/interview/queryList?ids={}".format(ids)
    remark = "批量查询面试订单"
    return get_requests(url=url, headers=headers, remark=remark)


def positions_queryList():
    url = host + "/position/queryList"
    remark = "批量查询职位"
    return get_requests(url=url, headers=headers, remark=remark)


def buser_hr_getList(tagType, ids):
    url = host + "/buser/hr/getList?tagType={}&ids={}".format(tagType, ids)
    remark = "批量查询HR信息"
    return get_requests(url=url, headers=headers, remark=remark)


def positionCategories_get(type):
    url = host + "/config/positionCategories/get?type={}".format(type)
    remark = "查询职位分类配置信息"
    return get_requests(url=url, headers=headers, remark=remark)


def queryPositions():
    url = host + "/activity/carp/queryPositions?pageSize=20&pageNo=1"
    remark = "查询曝光职位"
    return get_requests(url=url, headers=headers, remark=remark)


def queryHistoryNotes():
    url = host + "/activity/carp/queryHistoryNotes"
    remark = "查询历史晒贴"
    return get_requests(url=url, headers=headers, remark=remark)


def queryInterviews():
    url = host + "/activity/carp/queryInterviews"
    remark = "查询面试列表"
    return get_requests(url=url, headers=headers, remark=remark)


def activity_carp_queryNotePreview(orderId):
    url = host + "/activity/carp/queryNotePreview?orderId={}".format(orderId)
    remark = "查询发帖前的预览信息"
    return get_requests(url=url, headers=headers, remark=remark)


def activity_carp_publicNote(content, userName):
    url = host + "/activity/carp/publicNote"
    data = {
        "content": content,
        "interviewId": 0,
        "userName": userName
    }
    remark = "发帖"
    return json_post(url=url, headers=headers, data=data, remark=remark)


def cms_luckyShare_querylist(userId, status, startTime, endTime, pageNo, pageSize):
    url = "http://home.lagou.com/cms/luckyShare/querylist.json"
    data = {
        "userId": userId,
        "status": status,
        "startTime": startTime,
        "endTime": endTime,
        "pageNo": pageNo,
        "pageSize": pageSize
    }

    remark = "home后台锦鲤贴列表查询"
    return get_requests(url=url, data=data, headers=headers, remark=remark)


def cms_luckyShare_audit(ll_id, status):
    url = "http://home.lagou.com/cms/luckyShare/audit.json"
    data = {
        "id": ll_id,
        "status": status
    }
    remark = "锦鲤贴审核"
    return json_post(url=url, data=data, headers=headers, remark=remark)
