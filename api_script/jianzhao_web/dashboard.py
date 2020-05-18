# coding:utf-8
# @Time  : 2020/5/12 15:05
# @Author: Xiawang
# Description:
from utils.util import get_header, form_post


def getEasyPlusPrivilegeCount():
    url = 'https://easy.lagou.com/dashboard/getEasyPlusPrivilegeCount.json'
    # header = get_header(url='https://easy.lagou.com/dashboard/index.htm?')
    remark = '获取当前用户是否获取招聘者权益'
    return form_post(url=url, headers={}, remark=remark)
