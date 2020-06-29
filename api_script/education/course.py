# coding:utf-8
# @Time  : 2020/3/6 16:16
# @Author: Xiawang
# Description:
from utils.util import get_edu_app_header, get_requests


def get_course_commentList(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/course/comment/getCourseCommentList?courseId={}&lessonId=&pageNum=1'.format(
        courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "开悟课程/获取评论"

    return get_requests(url=url, headers=header, remark=remark)


def get_distribution_poster_data(courseId, decorateId, gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/course/distribution/getDistributionPosterData?courseId={}&decorateId={}'.format(
        courseId, decorateId)
    # header = get_header(url="https://kaiwu.lagou.com/distribution/appCenter.html")
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取分销海报数据"
    return get_requests(url=url, headers=header, remark=remark)


def get_credit_center_info(userToken):
    url = 'https://gate.lagou.com/v1/neirong/course/user_growth/getCreditCenterInfo'
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "学分中心"
    return get_requests(url=url, headers=header, remark=remark)


def get_course_credit_info(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/course/user_growth/getCourseCreditInfo?courseId={}'.format(courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "个人成就中心"
    return get_requests(url=url, headers=header, remark=remark)


def get_distribution_course_list(gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/course/distribution/getDistributionCourseList'
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取推广课程列表"
    return get_requests(url=url, headers=header, remark=remark)


def get_my_earing(gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/course/distribution/getMyEarning'
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取我的收益"
    return get_requests(url=url, headers=header, remark=remark)


def get_user_earnings_detail(gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/course/distribution/getUserEarningsDetail?nextStartId=0&amountType=0'
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取收益详情"
    return get_requests(url=url, headers=header, remark=remark)


def get_wei_xin_user(gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/course/distribution/getWeiXinUser'
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取微信用户信息"
    return get_requests(url=url, headers=header, remark=remark)
