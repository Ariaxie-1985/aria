# coding:utf-8
# @Time  : 2019-03-07 14:34
# @Author: Xiawang
import json

from utils.util import get_app_header, get_requests

host = "https://gate.lagou.com/v1/entry"
header = get_app_header(100014641)

def baseStatus_get():
    '''
    :return:
    '''
    url = host+ "/cuser/baseStatus/get"
    c_headers = {"X-L-REQ-HEADER":{"deviceType":"150","appVersion":"70800", "reqVersion":"70800"}}
    c_headers["X-L-REQ-HEADER"] = json.dumps(c_headers["X-L-REQ-HEADER"])
    headers = dict(header)
    headers.update(c_headers)
    remark = "查询职位分类配置信息"
    return get_requests(url=url,headers=headers,remark=remark)


