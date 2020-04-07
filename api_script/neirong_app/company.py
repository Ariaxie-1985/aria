# coding:utf-8
# @Time  : 2019-05-31 11:38
# @Author: betty
from api_script.entry.account.passport import password_login
from utils.util import json_post, get_requests, app_header_999


def create_benefit(userToken, id, ip_port):
    url = "https://gate.lagou.com/v1/neirong/company/benefit/create"
    header = app_header_999(userToken, DA=False)
    data = {
        "ids": [id]  # 这里的id是 函数benefit_category_left返回的id
    }
    return json_post(url=url, headers=header, data=data, ip_port=ip_port, remark="增加公司福利")


def benefit_category_left(userToken, ip_port):
    url = "https://gate.lagou.com/v1/neirong/company/benefit/category/left"
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, ip_port=ip_port, remark="查询公司该城市下未添加的的福利标签数据").json()


def get_benefit_baseInfo(userToken, companyId, ip_port):
    url = "https://gate.lagou.com/v1/neirong/company/benefit/baseInfo?companyId={}".format(companyId)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, ip_port=ip_port, remark="查看公司福利信息").json()


def delete_benefit(userToken, id, ip_port):
    url = "https://gate.lagou.com/v1/neirong/company/benefit/delete"
    header = app_header_999(userToken, DA=False)
    data = {
        "id": id  # 这里的id是 函数get_benefit_baseInfo返回的id
    }
    return json_post(url=url, headers=header, data=data, ip_port=ip_port, remark="删除公司福利")


def company_baseInfo(userToken, companyId, ip_port):
    url = 'https://gate.lagou.com/v1/neirong/company/baseInfo?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False)
    remark = '查询公司基本信息'
    return get_requests(url=url, headers=header, ip_port=ip_port, remark=remark).json()


def company_culture(userToken, companyId, ip_port):
    url = 'https://gate.lagou.com/v1/neirong/company/culture?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False)
    remark = '查询公司企业文化'
    return get_requests(url=url, headers=header, ip_port=ip_port, remark=remark).json()


def company_detail(userToken, companyId, ip_port):
    url = 'https://gate.lagou.com/v1/neirong/company/detail?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False)
    remark = '查询公司详情'
    return get_requests(url=url, headers=header, ip_port=ip_port, remark=remark).json()


def company_hasBenefit(userToken, companyId, ip_port):
    url = 'https://gate.lagou.com/v1/neirong/company/hasBenefit?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False)
    remark = '查询公司详情'
    return get_requests(url=url, headers=header, ip_port=ip_port, remark=remark).json()


def company_positionTypes(userToken, companyId):
    url = 'https://gate.lagou.com/v1/neirong/company/positionTypes?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False)
    remark = '根据公司返回面试评价职位类型'
    return get_requests(url=url, headers=header, remark=remark).json()


def company_question(userToken, companyId, ip_port):
    url = 'https://gate.lagou.com/v1/neirong/company/question?companyId={}&pageNo=1&pageSize=10'.format(companyId)
    header = app_header_999(userToken, DA=False)
    remark = '公司问答列表'
    return get_requests(url=url, headers=header, ip_port=ip_port, remark=remark).json()


if __name__ == '__main__':
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    r = company_positionTypes(userToken=userToken, companyId=418937)
    print(bool(r['content']['positionTypes']))
