# coding:utf-8
# @Time  : 2020-02-17 15:00
# @Author: Xiawang
from api_script.entry.account.passport import password_login
from utils.util import get_requests, app_header_999


def query_company_index(userToken, companyId):
    url = 'https://gate.lagou.com/v1/entry/bigCompany/query?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="查询公司主页").json()


def query_all_company(userToken):
    url = 'https://gate.lagou.com/v1/entry/bigCompany/queryAll'
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="查询所有大公司ID列表").json()


def query_urgent_positions(userToken, companyId):
    url = 'https://gate.lagou.com/v1/entry/bigCompany/queryUrgentPositions?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="查询公司急招职位").json()


def is_big_company(userToken, companyId):
    url = 'https://gate.lagou.com/v1/entry/bigCompany/verify?companyId={}'.format(companyId)
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="是否大公司").json()


if __name__ == '__main__':
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    r = is_big_company(userToken=userToken, companyId=1880)
    print(r)
