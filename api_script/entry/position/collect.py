# coding:utf-8
# @Time  : 2020/2/21 12:37
# @Author: Xiawang
# Description:
from api_script.entry.account.passport import password_login
from utils.util import app_header_999, json_post


def collect_add(userToken, positionId, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/position/collect/add'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    data = {
        "positionId": positionId
    }
    remark = "收藏职位"
    return json_post(url=url, headers=header, data=data, remark=remark, ip_port=ip_port)


def collect_list(userToken, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/position/collect/list'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    data = {
        "clearRedDot": True,
        "pageNo": 1,
        "pageSize": 10
    }
    remark = "收藏职位列表"
    return json_post(url=url, headers=header, data=data, remark=remark, ip_port=ip_port)


def collect_clear(userToken, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/position/collect/clear'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = "清除收藏职位的红点"
    return json_post(url=url, headers=header, remark=remark, ip_port=ip_port)


def collect_delete(userToken, positionId, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/position/collect/delete'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    data = {
        "positionId": positionId
    }
    remark = "取消已收藏职位"
    return json_post(url=url, headers=header, data=data, remark=remark, ip_port=ip_port)


if __name__ == '__main__':
    result = password_login("0085220180917", "0085220180917")
    userToken = result['content']['userToken']
    header = app_header_999(userToken=userToken)
    print(header)
