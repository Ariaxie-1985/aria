# coding:utf-8
# @Time  : 2019-09-24 11:32
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def get_jd(userToken, positionId):
    url = 'https://gate.lagou.com/v1/entry/position/jd?positionId={}&isCInspectB=1'.format(positionId)
    header = app_header_999(userToken,DA=False)
    return get_requests(url=url, headers=header, remark="获取职位jd页").json()


