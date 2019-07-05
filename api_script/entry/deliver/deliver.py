# coding:utf-8
# @Time  : 2019-07-04 11:00
# @Author: Xiawang
from utils.util import get_app_header_new, json_post


def deliver_check(positionId):
    url = 'https://gate.lagou.com/v1/entry/deliver/check'
    header = get_app_header_new(userId=100014648,
                                X_L_REQ_HEADER={"appVersion": "V_70000_1", "deviceType": 150, "reqVersion": 71300,
                                                "userType": 0})
    data = {
        "positionId": positionId
    }
    remark = '投递前检查'

    return json_post(url=url, headers=header, data=data, remark=remark)


def deliver_create(positionId, resumeId, resumeType):
    url = 'https://gate.lagou.com/v1/entry/deliver/create'
    header = get_app_header_new(userId=100014648,
                                X_L_REQ_HEADER={"appVersion": "V_70000_1", "deviceType": 150, "reqVersion": 71300,
                                                "userType": 0})
    data = {
        "isTalk": True,
        "positionId": positionId,
        "resumeId": resumeId,
        "resumeType": resumeType
    }
    remark = '投递简历'

    return json_post(url=url, headers=header, data=data, remark=remark)


def deliver_get():
    url = 'https://gate.lagou.com/v1/entry/deliver/get'
    header = get_app_header_new(userId=100014648,
                                X_L_REQ_HEADER={"appVersion": "V_70000_1", "deviceType": 150, "reqVersion": 71300,
                                                "userType": 0})
    data = {
              "orderId": 1143814243902828544
            }
    remark = '获取投递的简历详情'

    return json_post(url=url, headers=header, data=data, remark=remark)


if __name__ == '__main__':
    deliver_check()
