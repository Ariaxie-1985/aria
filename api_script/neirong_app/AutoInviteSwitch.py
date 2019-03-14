# coding:utf-8
# @Time  : 2019-03-07 15:23
# @Author: Xiawang

from utils.util import get_app_header, get_requests, json_post

host = "https://gate.lagou.com/v1/neirong"
headers = get_app_header(100014641)


def autoInviteSwitch_status():
    '''
    :return:
    '''
    url = host + "/autoInviteSwitch/status"
    remark = "开关状态"
    return get_requests(url=url, headers=headers, remark=remark)


def autoInviteSwitch_open(autoInviteType,status):
    '''

    :param autoInviteType: int, 邀约类型 1特权/普通职位，2无曝光职位
    :param status: int, 开关状态 1关闭，2开启
    :return:
    '''
    url = host + "/autoInviteSwitch/open"
    data = {
          "autoInviteType": autoInviteType,
          "status": status
        }

    remark = "开关"
    return json_post(url=url, headers=headers, data=data, remark=remark)
