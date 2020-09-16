# coding:utf-8
# @Time  : 2019-09-20 15:34
# @Author: Xiawang
# Description:
import json

from utils.util import app_header_999, get_requests, json_post


def get_info(userToken):
    url = 'https://gate.lagou.com/v1/entry/cuser/baseStatus/get'
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="跳转到首页，获取C端用户信息", rd='曾小宁')


def batchCancel(userIds, userToken=None):
    url = 'https://gate.lagou.com/v1/entry/helper/user/batchCancel'
    header = app_header_999(userToken, DA=False)
    data = {
        "ps": "fd7b546cfddb50deead1e5e89123a37fd71626ab06a5c155a7exxxdeead1e5e89123a37fd71626ab",
        "userIds": str(userIds)
    }
    remark = "注销账号"
    return json_post(url=url, headers=header, data=data, remark=remark, rd='曾小宁')


if __name__ == '__main__':
    r = get_info("f7f79544160c5ab5942af1f98f94dab1e930cde5675647b65cd7e502e0af857b")
    print(r)
