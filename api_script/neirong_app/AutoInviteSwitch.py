# coding:utf-8
# @Time  : 2019-03-07 15:23
# @Author: Xiawang

from utils.util import get_requests, json_post, app_header_999

host = "https://gate.lagou.com/v1/neirong"


def autoInviteSwitch_status(userToken, ip_port):
    '''
    :return:
    '''
    url = host + "/autoInviteSwitch/status"
    headers = app_header_999(userToken, DA=False)
    remark = "开关状态"
    return get_requests(url=url, headers=headers, remark=remark, ip_port=ip_port).json()


def autoInviteSwitch_open(autoInviteType, status, userToken):
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
    headers = app_header_999(userToken, DA=False)
    remark = "开关"
    return json_post(url=url, headers=headers, data=data, remark=remark)
