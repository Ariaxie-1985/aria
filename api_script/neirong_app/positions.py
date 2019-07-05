# coding:utf-8
# @Time  : 2019-05-31 11:32
# @Author: Xiawang
from utils.util import get_requests, get_app_header


def mark_info(positionIds):
    url = 'https://gate.lagou.com/v1/neirong/positions/mark_info?positionIds={}'.format(positionIds)
    remark = '标记职位为直招'
    header = get_app_header(100014641)
    return get_requests(url=url, headers=header, remark=remark).json()
