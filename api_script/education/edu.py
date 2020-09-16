# coding:utf-8
# @Time  : 2020/3/6 16:11
# @Author: Xiawang
# Description:

from utils.util import get_requests, get_edu_app_header

import re
hasBuy_course_id =[]
nohasBuy_course_id =[]
def get_course_list(userToken):
    url = "https://gate.lagou.com/v1/neirong/edu/homepage/getCourseList"
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "获取会员信息"
    result = get_requests(url=url, headers=header, remark=remark,rd='Yuwei Cheng')
    a = result['content']['courseCardList'][0]['courseList']
    for k in a:
        if k['hasBuy']:
            hasBuy_course_id.append(k['id'])
        else:
            nohasBuy_course_id.append(k['id'])
    return result,hasBuy_course_id,nohasBuy_course_id

def  get_content_list(userToken):
    url = "https://gate.lagou.com/v1/neirong/edu/homepage/getContentList"
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "获取训练营列表专区数据"
    result = get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')
    return result

def  get_promotion_list(userToken):
    url = "https://gate.lagou.com/v1/neirong/edu/homepage/getPromotionList"
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "获取推广促销活动列表专区数据"
    result = get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')
    return result


def  get_course_list_only_formember(get_h5_token):
    url = "https://gate.lagou.com/v1/neirong/edu/member/getCourseListOnlyForMember"
    header = get_edu_app_header(gateLoginToken=get_h5_token, DA=False)
    remark = "获取会员信息"
    result = get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')
    return result

def get_pop_dialog(userToken):
    url ='https://gate.lagou.com/v1/neirong/edu/member/popDialog'
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "拉勾教育会员/会员弹窗"
    result = get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')
    return result

def get_course_list_only_for_member(get_h5_token):
    url = 'https://gate.lagou.com/v1/neirong/edu/member/getCourseListOnlyForMember'
    header = get_edu_app_header(gateLoginToken=get_h5_token, DA=False)
    remark = "拉勾教育会员/获取用户简单信息"
    result = get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')
    return result

def draw_Course(courseId,get_h5_token):
    url = 'https://gate.lagou.com/v1/neirong/edu/member/drawCourse?courseId={}'.format(courseId)
    header = get_edu_app_header(gateLoginToken=get_h5_token, DA=False)
    remark = "拉勾教育会员/VIP免费开通课程"
    result = get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')
    return result













