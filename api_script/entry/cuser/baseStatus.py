# coding:utf-8
# @Time  : 2019-09-20 15:34
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def get_info(userToken):
    url = 'https://gate.lagou.com/v1/entry/cuser/baseStatus/get'
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="跳转到首页，获取C端用户信息").json()



if __name__ == '__main__':
    r = get_info("f7f79544160c5ab5942af1f98f94dab1e930cde5675647b65cd7e502e0af857b")
    print(r.json())