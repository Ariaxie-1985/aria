# coding:utf-8
# @Time  : 2019-09-23 14:43
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def query_interview_experience(userToken, companyId, positionType, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/interviewExperience/query?companyId={}&pageNo=1&pageSize=5&positionType={}'.format(
        companyId, positionType)
    header = app_header_999(userToken, DA=False, userId=userId)
    return get_requests(url=url, headers=header, remark="查询面试评价", ip_port=ip_port, rd='royliu')


def query_positionTypes(userToken, companyId, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/neirong/company/positionTypes?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False, userId=userId)
    return get_requests(url=url, headers=header, remark="查询筛选条件", ip_port=ip_port, rd='royliu')


def query_company_score(userToken, companyId, userId=None, ip_port=None):
    url = 'https://gate.lagou.com/v1/entry/interviewExperience/queryCompanyScore?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False, userId=userId)
    return get_requests(url=url, headers=header, remark="查询公司面试评价分数", ip_port=ip_port)
