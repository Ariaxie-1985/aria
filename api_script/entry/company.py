# coding:utf-8
# @Time  : 2020/2/21 17:05
# @Author: Xiawang
# Description:
from api_script.entry.account.passport import password_login
from utils.util import app_header_999, get_requests, json_post


def get_hot_company(userToken, city):
    url = 'https://gate.lagou.com/v1/entry/hotCompany/getHotCompany?city={}'.format(city)
    header = app_header_999(userToken=userToken, DA=False)
    remark = '获取热门公司'
    return get_requests(url=url, headers=header, remark=remark).json()


def get_company_questions(userToken, companyId):
    url = 'https://gate.lagou.com/v1/entry/company/queryQuestions?companyId={}&pageNo=1&pageSize=10'.format(companyId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = '获取公司的问答'
    return get_requests(url=url, headers=header, remark=remark).json()


def company_attention_add(userToken, companyId):
    url = 'https://gate.lagou.com/v1/entry/company/attention/add'
    header = app_header_999(userToken=userToken, DA=False)
    data = {
        "companyId": companyId
    }
    remark = '关注公司'
    return json_post(url=url, headers=header, data=data, remark=remark)


def company_attention_delete(userToken, companyId):
    url = 'https://gate.lagou.com/v1/entry/company/attention/delete'
    header = app_header_999(userToken=userToken, DA=False)
    data = {
        "companyId": companyId
    }
    remark = '取消关注已关注的公司'
    return json_post(url=url, headers=header, data=data, remark=remark)


def company_attention_list(userToken):
    url = 'https://gate.lagou.com/v1/entry/company/attention/list'
    header = app_header_999(userToken=userToken, DA=False)
    data = {
        "pageNo": 1,
        "pageSize": 10
    }
    print(header)
    remark = '查询关注的公司列表'
    return json_post(url=url, headers=header, data=data, remark=remark)


if __name__ == '__main__':
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    r = company_attention_list(userToken=userToken)
    print(r)
