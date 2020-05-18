# coding:utf-8
# @Time  : 2020/2/25 15:11
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def get_hot_company(userToken, city, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/campus/company/getHotCompany?city={}'.format(city)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '获取校招的热门公司'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_user_info(userToken, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/campus/user/getInfo'
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '校招--获取用户信息'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()


def get_campus_count(userToken, companyId, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/campus/count/getCampusCount.json?companyId={}'.format(companyId)
    header = app_header_999(userToken=userToken, DA=False, userId=userId)
    remark = '获取校友数量'
    return get_requests(url=url, headers=header, remark=remark, ip_port=ip_port).json()
