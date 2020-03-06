# coding:utf-8
# @Time  : 2019-07-04 11:00
# @Author: Xiawang
import pysnooper

from api_script.entry.account.passport import password_login
from utils.util import get_app_header_new, json_post, app_header_999, get_requests


@pysnooper.snoop('/Users/wang/Desktop/lg-project/lg_api_script/tests/test_mainprocess/deliver_check.log')
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


def recommend_isExistPositionList(userToken, positionId):
    url = 'https://gate.lagou.com/v1/entry/deliver/recommend/isExistPositionList?positionId={}'.format(positionId)
    header = app_header_999(userToken, DA=False)
    remark = "投递后推荐的职位 （投了又投），是否有数据"
    return get_requests(url=url, headers=header, remark=remark).json()


def recommend_positionList(userToken, orderId, positionId):
    url = 'https://gate.lagou.com/v1/entry/deliver/recommend/positionList'
    header = app_header_999(userToken, DA=False)
    data = {
        "orderId": orderId,
        "pageNo": 1,
        "pageSize": 10,
        "positionId": positionId
    }
    remark = "投递后推荐的职位 （投了又投)"
    return json_post(url=url, headers=header, data=data, remark=remark)


if __name__ == '__main__':
    result = password_login("0085220180917", "0085220180917")
    userToken = result['content']['userToken']
    r = get_resume_info(userToken)
    print(r)
