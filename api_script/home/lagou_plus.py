# coding:utf-8
# @Time  : 2019-05-14 12:02
# @Author: Xiawang
from utils.util import get_header, form_post, login_home_code


def get_contract_No(companyId):
    header = get_header("http://home.lagou.com/")
    Request_url = "https://home.lagou.com/crm/contractController/list.json"
    data = {"companyId": companyId}
    object = form_post(url=Request_url, remark="查询当前公司下的合同", data=data, headers=header)
    contractNo = object['data']['pageData'][0]['number']
    return contractNo


def close_contract(contractNo):
    '''终止合同
    '''
    header = get_header("https://home.lagou.com/")
    Request_url = "https://home.lagou.com/crm/valueadded/product/close.json"
    data = {"contractNo": contractNo}
    return form_post(url=Request_url, remark="终止所有合同", data=data, headers=header)['success']


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
    return form_post(url=url, data=data, headers=headers, remark=remark)['success']


if __name__ == '__main__':
    login_home_code('00853', 22222222)
    no = get_contract_No(96109603)
    print(close_contract(no))
