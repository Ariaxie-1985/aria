# coding:utf-8
# @Time  : 2020/6/3 19:26
# @Author: Sunnyzhang
# Description:
from utils.util import  get_requests,app_header_999
import re
def getToken(userToken):
    url = 'https://gate.lagou.com/v1/entry/account/h5/getToken'
    # header = get_header(url="https://kaiwu.lagou.com/distribution/appCenter.html")
    header = app_header_999(userToken=userToken,DA=False,appType=1)
    remark = "获取gate_login_token"
    r = get_requests(url=url, headers=header, remark=remark)
    gate_login_token = r['content']['gateLoginToken']
    return gate_login_token
