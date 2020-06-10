# coding:utf-8
# @Time  : 2020/6/2 10:44
# @Author: Xiawang
# Description:


from utils.util import get_requests


def open_authority_token(appid, secret, grant_type):
    url = 'https://open.lagou.com/v1/authority/token'
    data = {'appid': appid, 'secret': secret,
            'grant_type': grant_type}
    remark = '获取accessToken'
    return get_requests(url=url, data=data, remark=remark)
