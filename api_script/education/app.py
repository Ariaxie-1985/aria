# coding:utf-8
# @Time  : 2020/3/6 16:11
# @Author: Xiawang
# Description:

from utils.util import app_header_999, get_requests


def get_homepage_cards(userToken):
    url = 'https://gate.lagou.com/v1/neirong/app/getHomePageCards'
    header = app_header_999(userToken=userToken, DA=False)
    remark = "拉勾教育-获取首页卡片信息列表"
    return get_requests(url=url, headers=header, remark=remark).json()


def get_all_course_purchased_record(userToken):
    url = 'https://gate.lagou.com/v1/neirong/app/getAllCoursePurchasedRecord'
    header = app_header_999(userToken=userToken, DA=False)
    remark = "拉勾教育/获取所有已购课程的列表(大课和专栏课程)"
    return get_requests(url=url, headers=header, remark=remark).json()
