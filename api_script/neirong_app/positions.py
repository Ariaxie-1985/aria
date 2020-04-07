# coding:utf-8
# @Time  : 2019-05-31 11:32
# @Author: Xiawang
from utils.util import get_requests, app_header_999


def positions_mark_info(userToken, positionId, ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/neirong/positions/mark_info?positionIds={}'.format(positionId)
    remark = '标记职位为直招'
    header = app_header_999(userToken, DA=False, userId=userId)
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()
