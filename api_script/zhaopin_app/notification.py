# coding:utf-8
# @Time  : 2019-04-28 15:19
# @Author: Xiawang

from utils.util import get_app_header, json_post, get_requests

host = 'https://gate.lagou.com/v1/zhaopin'
header = get_app_header(100014641)


def notification_read(notificationId):
    url = host + '/notification/read?notificationId={}'.format(notificationId)
    remark = '标记已读'
    return get_requests(url=url, headers=header, remark=remark).json()


def notification_read_all():
    url = host + '/notification/read/all'
    remark = '全部标记已读'
    return get_requests(url=url, remark=remark, headers=header).json()


def notification_query():
    url = host + '/notification/query?size=10'
    remark = '简历状态消息列表'
    return get_requests(url=url, remark=remark, headers=header).json()
