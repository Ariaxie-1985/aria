# coding:utf-8
# @Time  : 2020/3/6 16:31
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def get_course_info(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/bigcourse/getCourseInfo?courseId={}'.format(courseId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "获取大课的课程基本信息"
    return get_requests(url=url, headers=header, remark=remark)


def get_course_outline(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/bigcourse/getCourseOutline?courseId={}'.format(courseId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "获取大课的课程大纲"
    return get_requests(url=url, headers=header, remark=remark)


def get_week_lessons(userToken, courseId, weekId):
    url = 'https://gate.lagou.com/v1/neirong/bigcourse/getWeekLessons?courseId={}&weekId={}'.format(courseId, weekId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "获取大课一周下的所有课时"
    return get_requests(url=url, headers=header, remark=remark)


def get_watch_percent(userToken, courseId, weekId):
    url = 'https://gate.lagou.com/v1/neirong/bigcourse/getWatchPercent?courseId={}&weekId={}'.format(courseId, weekId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "获取大课一周录播视频观看进度"
    return get_requests(url=url, headers=header, remark=remark)
