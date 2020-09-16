# coding:utf-8
# @Time  : 2020/8/7 16:54
# @Author: Xiawang
# Description:
from utils.util import get_requests


def debugSelfCheck():
    url = 'https://passport.lagou.com/login/debugSelfCheck.json'
    remark = '校验是否可以跳过极光校验'
    return get_requests(url=url, remark=remark)


