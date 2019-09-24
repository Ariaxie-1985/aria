# coding:utf-8
# @Time  : 2019-07-04 11:00
# @Author: Xiawang
from utils.util import get_app_header_new, json_post, app_header_999


def deliver_check(positionId, H9=False, userToken=None):
    url = 'https://gate.lagou.com/v1/entry/deliver/check'
    if H9 == True:
        header = app_header_999(userToken, DA=False)
    else:
        header = get_app_header_new(userId=100014648,
                                    X_L_REQ_HEADER={"appVersion": "V_70000_1", "deviceType": 150, "reqVersion": 71300,
                                                    "userType": 0})
    data = {
        "positionId": positionId
    }
    remark = '投递前检查'

    return json_post(url=url, headers=header, data=data, remark=remark)


def deliver_create(positionId, resumeId, resumeType, isTalk=True, userToken=None, H9=False):
    url = 'https://gate.lagou.com/v1/entry/deliver/create'
    if H9 == True:
        header = app_header_999(userToken, DA=False)
    else:
        header = get_app_header_new(userId=100014648,
                                    X_L_REQ_HEADER={"appVersion": "V_70000_1", "deviceType": 150, "reqVersion": 71300,
                                                    "userType": 0})
    data = {
        "isTalk": isTalk,
        "positionId": int(positionId),
        "resumeId": resumeId,
        "resumeType": resumeType
    }
    remark = '投递简历'

    return json_post(url=url, headers=header, data=data, remark=remark)


def deliver_get(orderId, userToken=None, H9=False):
    url = 'https://gate.lagou.com/v1/entry/deliver/get'
    if H9 == True:
        header = app_header_999(userToken)
    else:
        header = get_app_header_new(userId=100014648,
                                    X_L_REQ_HEADER={"appVersion": "V_70000_1", "deviceType": 150, "reqVersion": 71300,
                                                    "userType": 0})
    data = {
        "orderId": orderId
    }
    remark = '获取投递的简历详情'

    return json_post(url=url, headers=header, data=data, remark=remark)


def get_resume_info(userToken):
    url = 'https://gate.lagou.com/v1/neirong/resumes/list'
    header = app_header_999(userToken, DA=False)
    return json_post(url=url, headers=header, remark="获取简历类型")


if __name__ == '__main__':
    deliver_check()
