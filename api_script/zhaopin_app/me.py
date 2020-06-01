# coding:utf-8
# @Time  : 2020/2/26 11:56
# @Author: Xiawang
# Description:
from api_script.entry.account.passport import password_login
from utils.util import app_header_999, get_requests


def get_me_info(userToken, userId=None, ip_port=None):
    url = "https://gate.lagou.com/v1/zhaopin/me/info"
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    print(header)
    remark = "获取B端用户信息"
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port)


if __name__ == '__main__':
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    get_me_info(userToken=userToken)
    # result = password_login("0085220180917", "0085220180917")
    # print(result)
