# coding:utf-8
# @Time  : 2019-04-28 15:19
# @Author: Xiawang

from utils.util import get_requests, app_header_999

host = 'https://gate.lagou.com/v1/zhaopin'


def notification_read(userToken, notificationId):
    url = host + '/notification/read?notificationId={}'.format(notificationId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = '标记已读'
    return get_requests(url=url, headers=header, remark=remark).json()


def notification_read_all(userToken):
    url = host + '/notification/read/all'
    header = app_header_999(userToken=userToken, DA=False)
    remark = '全部标记已读'
    return get_requests(url=url, remark=remark, headers=header).json()


def notification_query(userToken):
    url = host + '/notification/query?size=10'
    header = app_header_999(userToken=userToken, DA=False)
    remark = '简历状态消息列表'
    return get_requests(url=url, remark=remark, headers=header).json()


def notification_unread_count(userToken):
    url = host + '/notification/unread/count'
    header = app_header_999(userToken=userToken, DA=False)
    remark = '统计未读简历状态消息数'
    return get_requests(url=url, remark=remark, headers=header).json()
