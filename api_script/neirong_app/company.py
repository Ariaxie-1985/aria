# coding:utf-8
# @Time  : 2019-05-31 11:38
# @Author: betty
import json

from utils.util import get_app_header, json_post, get_requests


def create_fuli():
    # r = get_requests()
    url = "https://gate.lagou.com/v1/neirong/company/benefit/create"
    header = get_app_header(100014641)
    data = {
        "ids": ['23']
    }
    return json_post(url=url, headers=header, data=data, remark="增加公司福利")


def view_excess_fuli():
    url = "https://gate.lagou.com/v1/neirong/company/benefit/category/left"
    header = get_app_header(userId=100014641)
    return get_requests(url=url, headers=header, remark="查看公司剩余福利")


def view_fuli():
    info = {"companyId": 142136, "userId": 100014641}
    url = "https://gate.lagou.com/v1/neirong/company/benefit/baseInfo?companyId={}".format(info["companyId"])
    # url = "https://gate.lagou.com/v1/neirong/company/benefit/baseInfo?companyId=142136"
    c_headers = {"X-L-REQ-HEADER": {"deviceType": "10", "reqVersion": "80201"}}
    c_headers["X-L-REQ-HEADER"] = json.dumps(c_headers["X-L-REQ-HEADER"])
    header = get_app_header(info["userId"])
    header = dict(header)
    header.update(c_headers)
    return get_requests(url=url, headers=header, remark="福利信息").json()
