# coding:utf-8
# @Time  : 2020/3/6 16:16
# @Author: Xiawang
# Description:
from utils.util import app_header_999, get_requests


def get_distribution_info(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/course/comment/getCourseCommentList?courseId={}&lessonId=&pageNum=1'.format(
        courseId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "言职/开悟/获取分销信息"
    return get_requests(url=url, headers=header, remark=remark)


def get_course_commentList(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/course/comment/getCourseCommentList?courseId={}&lessonId=&pageNum=1'.format(
        courseId)
    header = app_header_999(userToken=userToken, DA=False)
    remark = "开悟课程/获取评论"
    return get_requests(url=url, headers=header, remark=remark)


def get_credit_center_info(userToken):
    url = 'https://gate.lagou.com/v1/neirong/course/user_growth/getCreditCenterInfo'
    header = app_header_999(userToken=userToken,DA=False)
    remark="学分中心"
    return get_requests(url=url,headers=header,remark=remark)