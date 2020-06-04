# coding:utf-8
# @Time  : 2020/2/17 16:24
# @Author: Xiawang
# Description:
from api_script.entry.account.passport import password_login
from utils.util import app_header_999, get_requests


def get_info(userToken, ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/entry/config/appSetting/get'
    header = app_header_999(userToken, DA=False, userId=userId)
    return get_requests(url=url, headers=header, remark="查询app端配置", ip_port=ip_port)


def get_app_theme(userToken, ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/entry/config/appSetting/getAppTheme'
    header = app_header_999(userToken, DA=False, userId=userId)
    return get_requests(url=url, headers=header, remark="查询app端主题", ip_port=ip_port)


def get_im_entrance(userToken, ip_port=None, userId=None):
    url = 'https://gate.lagou.com/v1/entry/config/appSetting/getIMEntrance'
    header = app_header_999(userToken, DA=False, userId=userId)
    return get_requests(url=url, headers=header, remark="查询APP消息页活动入口", ip_port=ip_port)


if __name__ == '__main__':
    result = password_login("19910626899", "000000")
    userToken = result['content']['userToken']
    r = get_im_entrance(userToken)
    print(r)
