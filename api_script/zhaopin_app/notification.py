# coding:utf-8
# @Time  : 2019-04-28 15:19
# @Author: Xiawang

from utils.util import get_requests, app_header_999

host = 'https://gate.lagou.com/v1/zhaopin'


def notification_read(userToken, notificationId,userId=None, ip_port=None):
    url = host + '/notification/read?notificationId={}'.format(notificationId)
    header = app_header_999(userToken=userToken, DA=False,userId=userId)
    remark = '标记已读'
    return get_requests(url=url, headers=header, remark=remark,ip_port=ip_port)


def notification_read_all(userToken,userId=None, ip_port=None):
    url = host + '/notification/read/all'
    header = app_header_999(userToken=userToken, DA=False,userId=userId)
    remark = '全部标记已读'
    return get_requests(url=url, remark=remark, headers=header,ip_port=ip_port)


def notification_query(userToken, userId=None, ip_port=None):
    url = host + '/notification/query?size=10'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '简历状态消息列表'
    return get_requests(url=url, remark=remark, headers=header, ip_port=ip_port)


def notification_unread_count(userToken,userId=None, ip_port=None):
    url = host + '/notification/unread/count'
    header = app_header_999(userToken=userToken, DA=False,userId=userId)
    remark = '统计未读简历状态消息数'
    return get_requests(url=url, remark=remark, headers=header,ip_port=ip_port)
