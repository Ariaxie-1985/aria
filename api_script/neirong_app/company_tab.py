# coding:utf-8
# @Time  : 2020/2/14 10:44
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def queryCompanyList(city, userToken, userId=None, ip_port=None):
    url = "https://gate.lagou.com/v1/neirong/companyTab/queryCompanyList?pageNo=0&pageSize=20&city={}".format(city)
    header = app_header_999(userToken, DA=False, userId=userId)
    remark = '查询公司TAB页'
    return get_requests(url=url, headers=header, ip_port=ip_port, remark=remark).json()
