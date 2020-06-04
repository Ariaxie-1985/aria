# coding:utf-8
# @Time  : 2020/2/20 18:42
# @Author: Xiawang
# Description:
from api_script.entry.account.passport import password_login
from utils.util import app_header_999, get_requests


def get_position_delivered(userToken, positionId, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/positionrec/delivered/{}?pageno=1&pagesize=5'.format(positionId)
    header = app_header_999(userToken, DA=False, userId=userId)
    return get_requests(url=url, headers=header, remark="投了又投", ip_port=ip_port)


def get_position_rec(userToken, positionId, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/positionrec/posrec/{}?pageno=1&pagesize=5'.format(positionId)
    header = app_header_999(userToken, DA=False, userId=userId)
    return get_requests(url=url, headers=header, remark="相似职位", ip_port=ip_port)


def get_position_user_rec(userToken, positionId,userId=None,ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/positionrec/userrec/{}?pageno=1&pagesize=5'.format(positionId)
    header = app_header_999(userToken, DA=False,userId=userId)
    return get_requests(url=url, headers=header, remark="猜你喜欢",ip_port=ip_port)


def get_position_view(userToken, positionId,userId=None,ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/positionrec/view/{}?pageno=1&pagesize=5'.format(positionId)
    header = app_header_999(userToken, DA=False,userId=userId)
    return get_requests(url=url, headers=header, remark="看了又看",ip_port=ip_port)


if __name__ == '__main__':
    positionId = 6656633
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    print(get_position_delivered(userToken=userToken, positionId=positionId))
    print(get_position_rec(userToken=userToken, positionId=positionId))
    print(get_position_user_rec(userToken=userToken, positionId=positionId))
    print(get_position_view(userToken=userToken, positionId=positionId))
