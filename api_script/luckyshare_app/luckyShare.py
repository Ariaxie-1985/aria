# coding:utf-8
# @Time  : 2019-02-28 15:24
# @Author: Xiawang
from utils.util import get_app_header, get_requests, json_post

# host = "https://gate.lagou.com"
host = "http://10.1.201.110:12790"

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
    url = host + "/activity/carp/queryRedPointType?orderIds={}".format(orderIds)
    remark = "查询红点"
    return get_requests(url=url, headers=headers, remark=remark)


def activity_carp_removeRedDot():
    # todo 参数未放在body里
    url = host + "/activity/carp/removeRedDot"
    remark = "删除红点"
    return json_post(url=url, headers=headers, remark=remark)


def activity_carp_queryNotes():
    url = host + "/activity/carp/queryNotes"
    remark = "查询帖子列表"
    return get_requests(url=url, headers=headers, remark=remark)


def order_interview_queryList(ids):
    url = host + "/order/interview/queryList?ids={}".format(ids)
    remark = "批量查询面试订单"
    return get_requests(url=url, headers=headers, remark=remark)


def positions_queryList(ids):
    url = host + "/position/queryList?ids={}".format(ids)
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


def queryPositions(pageNo):
    url = host + "/activity/carp/queryPositions?pageSize=20&pageNo={}".format(pageNo)
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


def activity_carp_publicNote(companyId, content, interviewId, interviewTime, positionID, userName):
    url = host + "/activity/carp/publicNote"
    data = {
        "companyId": companyId,
        "content": content,
        "interviewId": interviewId,
        "interviewTime": interviewTime,
        "positionID": positionID,
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
