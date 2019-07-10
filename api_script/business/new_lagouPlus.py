# coding:utf-8
# @Time  : 2019-07-09 14:39
# @Author: Xiawang
import random

from utils.util import get_header, form_post, login_home_code, get_requests


def contractController_list(companyId):
    '''查询合同编号'''
    url = 'https://home.lagou.com/crm/contractController/list.json'
    header = get_header('https://home.lagou.com/')
    data = {'companyId': companyId}
    res = form_post(url=url, data=data, headers=header, remark='获取合同')
    if res['data']['totalCount'] >= 1:
        contractNo = res['data']['pageData'][0]['number']
        return contractNo
    else:
        return 0


def product_info():
    '''查询产品套餐'''
    url = 'https://home.lagou.com/crm/valueadded/product/query.json?pageNo=1&pageSize=30&name=&baseName=&status=&t={}'.format(
        random.randint(111111, 999999))
    header = get_header('https://home.lagou.com/')
    res = get_requests(url=url, headers=header, remark='获取产品信息').json()
    iterms = res['data']['result']
    return {'message': 'success', 'items': iterms}


def close_contract(contractNo):
    '''终止合同'''
    url = 'https://home.lagou.com/crm/valueadded/product/close.json'
    header = get_header('https://home.lagou.com/')
    data = {'contractNo': contractNo}
    return form_post(url=url, data=data, headers=header, remark='终止合同')['success']


def open_product(templateId, companyId, contractNo, userId, startTimeStr, endTimeStr):
    url = 'https://home.lagou.com/crm/valueadded/product/open.json'
    header = get_header('https://home.lagou.com/')
    data = {'templateId': templateId, 'num': 100, 'companyId': companyId, 'contractNo': contractNo,


            'userId': userId, 'startTimeStr': startTimeStr, 'endTimeStr': endTimeStr, 'upgrade': False}
    return form_post(url=url, data=data, headers=header, remark='开启合同')


def parase_product_info():
    pass


if __name__ == '__main__':
    login_home_code('00853', 22222222)
    # print(product_info())
