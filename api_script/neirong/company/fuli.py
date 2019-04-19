#coding:utf-8
#@Author:betty
import json

from  utils.util import get_app_header,get_requests

#获取公司福利信息

def benefit_baseInfo():
    info = {"companyId": 142136, "userId": 100014641}
    # url = "https://gate.lagou.com/v1/neirong/company/benefit/baseInfo?companyId={}".format(info["companyId"])
    url = "https://gate.lagou.com/v1/neirong/company/benefit/baseInfo?companyId=142136"
    c_headers = {"X-L-REQ-HEADER": {"deviceType": "10", "reqVersion": "80201"}}
    c_headers["X-L-REQ-HEADER"] = json.dumps(c_headers["X-L-REQ-HEADER"])
    header = get_app_header(info["userId"])
    header = dict(header)
    header.update(c_headers)
    return get_requests(url=url, headers=header, remark="福利信息").json()

s=benefit_baseInfo()
print(s)
