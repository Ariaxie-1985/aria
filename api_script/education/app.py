# coding:utf-8
# @Time  : 2020/3/6 16:11
# @Author: Xiawang
# Description:

from utils.util import get_requests, get_edu_app_header


def get_homepage_cards(userToken):
    url = 'https://gate.lagou.com/v1/neirong/app/getHomePageCards'
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "拉勾教育-获取首页卡片信息列表"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')


def get_all_course_purchased_record(userToken):
    url = 'https://gate.lagou.com/v1/neirong/app/getAllCoursePurchasedRecord'
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "拉勾教育/获取所有已购课程的列表(大课和专栏课程)"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')
