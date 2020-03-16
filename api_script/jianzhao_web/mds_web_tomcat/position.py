# coding:utf-8
# @Time  : 2020/3/13 14:48
# @Author: Xiawang
# Description:
from utils.util import get_code_token, form_post

header = get_code_token('https://easy.lagou.com/position/multiChannel/createPosition.htm')


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
