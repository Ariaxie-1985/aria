# coding:utf-8
# @Time  : 2019-05-14 12:02
# @Author: Xiawang
import time

from utils.util import get_header, form_post, login_home_code


def get_contract_list(companyId):
    header = get_header("http://home.lagou.com/")
    Request_url = "https://home.lagou.com/crm/contractController/list.json"
    data = {"companyId": companyId}
    return form_post(url=Request_url, remark="查询当前公司下的合同", data=data, headers=header, rd='李久超')


def close_contract(contractNo):
    '''终止合同
    '''
    header = get_header("https://home.lagou.com/")
    Request_url = "https://home.lagou.com/crm/valueadded/product/close.json"
    data = {"contractNo": contractNo}
    return form_post(url=Request_url, remark="终止所有合同", data=data, headers=header, rd='杨振宇')


def open_product(companyId, userId, contractNo):
    headers = get_header('https://home.lagou.com/')
    url = 'https://home.lagou.com/crm/valueadded/product/open.json'
    data = {
        'templateId': 90,
        'num': 10,
        'companyId': companyId,
        'contractNo': contractNo,
        'userId': userId,
        'startTimeStr': '2019-05-14',
        'endTimeStr': '2021-05-31',
        'upgrade': False
    }
    remark = "开启合同"
    return form_post(url=url, data=data, headers=headers, remark=remark, rd='杨振宇')['success']
