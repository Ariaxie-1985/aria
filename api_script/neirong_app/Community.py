# coding:utf-8
# @Time  : 2019-03-26 10:26
# @Author: Xiawang

from utils.util import get_app_header, get_requests, json_post

host = "https://gate.lagou.com/v1/neirong"


def communityMessage_clearRedSpot(userid):
    url = host + '/communityMessage/clearRedSpot'
    headers = get_app_header(userid)
    remark = '清楚言职社区通知的红点'
    return json_post(url=url, headers=headers, remark=remark)


def communityMessage_userBasicInfo(start, size, userid):
    url = host + \
          '/communityMessage/userBasicInfo?start={start}&size={size}'.format(start=start, size=size)
    headers = get_app_header(userid)
    remark = '获取言职社区通知页列表数据'
    return get_requests(url=url, headers=headers, remark=remark)

