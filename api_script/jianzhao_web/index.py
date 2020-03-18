# coding:utf-8
# @Time  : 2020/3/18 12:13
# @Author: Xiawang
# Description:
from utils.util import get_header, get_requests, form_post


def jump_easy_index_html():
    url = "https://easy.lagou.com/dashboard/index.htm?from=c_index"
    header = get_header(url='https://www.lagou.com/')
    remark = '从拉勾主站进入企业版'
    return get_requests(url=url, headers=header, remark=remark)


def search_plusSearchSelector():
    url = 'https://easy.lagou.com/search/plusSearchSelector.json?from=talentsearch'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index')
    remark = '人才查找'
    return get_requests(url=url, headers=header, remark=remark).json()


def get_easy_plus_privilegeCount():
    url = 'https://easy.lagou.com/dashboard/getEasyPlusPrivilegeCount.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index')
    remark = '获取当前用户的拉勾加权限信息'
    return form_post(url=url, headers=header, remark=remark)


def get_business_user_info():
    url = 'https://easy.lagou.com/businessUser/getBusinessUserInfo.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index')
    remark = '获取用户的商业信息'
    return get_requests(url=url, headers=header, remark=remark).json()


def get_user_goods_info():
    url = 'https://easy.lagou.com/dashboard/getUserGoodsInfo.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index')
    remark = '获取用户的权益信息'
    return get_requests(url=url, headers=header, remark=remark).json()


def get_yun_additional_info():
    url = 'https://easy.lagou.com/dashboard/getYunAdditionalInfo.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index')
    remark = '获取用户的简历的待办事项'
    return get_requests(url=url, headers=header, remark=remark).json()


def is_hunting_gray():
    url = 'https://easy.lagou.com/api/onlinehunting/isHuntingGray.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index')
    remark = '？'
    return get_requests(url=url, headers=header, remark=remark).json()


def personal_assistant():
    url = 'https://easy.lagou.com/dashboard/personal_assistant.json'
    header = get_header(url='https://easy.lagou.com/dashboard/index.htm?from=c_index')
    remark = '获取当前公司的招聘顾问'
    return get_requests(url=url, headers=header, remark=remark).json()


def get_product_version():
    url = 'https://easy.lagou.com/productContract/productVersion.json'
    header = get_header(url='https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1')
    remark = '获取当前公司的拉勾加版本号'
    return get_requests(url=url, headers=header, remark=remark).json()
