# coding:utf-8
# @Time  : 2019-08-01 12:32
# @Author: Xiawang
from utils.util import get_code_token, get_requests, login, form_post

header = get_code_token('https://easy.lagou.com/position/multiChannel/createPosition.htm')


def address_id(code):
    '''code: 市的code'''
    url = 'https://easy.lagou.com/lbs/getChildLbsInfoByCode.json?code={}'.format(code)
    header = get_code_token(url='https://easy.lagou.com/position/multiChannel/createPosition.htm')
    remark = '获取地址id'
    content = get_requests(url=url,headers=header,remark=remark).json()
    return content['content']['data']['lbsList']




def add_work_address():
    url = "https://easy.lagou.com/workAddress/add.json"
    data = {'workAddressId': '1758187'}
    remark = '添加工作地址'
    return form_post(url=url, headers=header, data=data, remark=remark)


def remove_work_address(workAddressId):
    url = "https://easy.lagou.com/workAddress/remove.json"
    data = {'workAddressId': workAddressId}
    remark = '移除工作地址'
    return form_post(url=url, headers=header, data=data, remark=remark)

if __name__ == '__main__':
    login('00852', 20181205)
    print(address_id('110100000'))