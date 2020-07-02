# coding:utf-8
# @Time  : 2020/3/6 16:16
# @Author: Xiawang
# Description:
from utils.util import get_edu_app_header, get_requests, app_header_999


def check_course_share_status(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/checkCourseShareStatus?courseId={}'.format(courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "言职/开悟/分享课程状态"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')



def get_course_description(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/getCourseDescription?courseId={}'.format(courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "言职/开悟/查询课程描述信息"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')



def get_distribution_info(userToken, courseId, decorateId):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/getDistributionInfo?courseId={}&decorateId={}'.format(courseId,
                                                                                                         decorateId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "言职/开悟/获取分销信息"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')



def get_course_lessons(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/getCourseLessons?courseId={}'.format(courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "获取课程信息"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')



def ice_breaking_location():
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/iceBreakingLocation/info'
    header = get_edu_app_header()
    remark = "一元购入口"
    return get_requests(url=url, headers=header, remark=remark, rd='John Zhou')


def save_course_history(courseId, sectionId, lessonId, mediaType, historyNode, gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/saveCourseHistory?courseId={}&sectionId={}&lessonId={}&mediaType={}&historyNode={}'.format(
        courseId, sectionId, lessonId, mediaType, historyNode)
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "保存课程下课时的历史节点"
    return get_requests(url=url, headers=header, remark=remark,rd='Yuwei Cheng')


def get_lesson_play_history(lessonId, gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/getLessonPlayHistory?lessonId={}'.format(lessonId)
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取课时播放历史记录"
    return get_requests(url=url, headers=header, remark=remark,rd='Yuwei Cheng')

def get_course_history(courseId, gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/kaiwu/getCourseHistory?courseId={}'.format(courseId)
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取课程历史记录"
    return get_requests(url=url, headers=header, remark=remark,rd='Yuwei Cheng')


def ice_breaking_html():
    url = 'https://kwn2.lagou.com/icebreaking/main.htm?lagoufrom=android&appVersion=1.2.5&appType=LGEdu'
    header = {}
    remark = '获取1元购618活动页面'
    return get_requests(url=url, headers=header, remark=remark, rd='John zhou')
