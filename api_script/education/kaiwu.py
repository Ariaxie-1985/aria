# coding:utf-8
# @Time  : 2020/3/6 16:16
# @Author: Xiawang
# Description:
from utils.util import get_edu_app_header, get_requests, app_header_999


def check_course_share_status(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/checkCourseShareStatus?courseId={}'.format(courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "言职/开悟/分享课程状态"
    return get_requests(url=url, headers=header, remark=remark)


def get_course_description(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/getCourseDescription?courseId={}'.format(courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "言职/开悟/查询课程描述信息"
    return get_requests(url=url, headers=header, remark=remark)


def get_distribution_info(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/getDistributionInfo?courseId={}'.format(courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "言职/开悟/获取分销信息"
    return get_requests(url=url, headers=header, remark=remark)


def get_course_lessons(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/getCourseLessons?courseId={}'.format(courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "获取课程信息"
    return get_requests(url=url, headers=header, remark=remark)


def ice_breaking_location():
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/iceBreakingLocation/info'
    header = get_edu_app_header()
    remark = "一元购入口"
    return get_requests(url=url, headers=header, remark=remark)


def ice_breaking_html():
    url = 'https://kwn2.lagou.com/icebreaking/main.htm?lagoufrom=android&appVersion=1.2.5&appType=LGEdu'
    header = {}
    remark = '获取1元购618活动页面'
    return get_requests(url=url, headers=header, remark=remark)



