# coding:utf-8
# @Time  : 2019-09-23 14:43
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def query_interview_experience(userToken, companyId, positionType):
    url = 'https://gate.lagou.com/v1/entry/interviewExperience/query?companyId={}&pageNo=1&pageSize=5&positionType={}'.format(
        companyId, positionType)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="查询面试评价").json()


def query_positionTypes(userToken, companyId):
    url = 'https://gate.lagou.com/v1/neirong/company/positionTypes?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="查询筛选条件").json()


