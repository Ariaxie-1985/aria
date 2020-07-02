# coding:utf-8
# @Time  : 2020/3/6 16:16
# @Author: Xiawang
# Description:
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import add_saveCompany
from utils.util import get_edu_app_header, get_requests
from api_script.entry.account.passport import password_login
import re
from bs4 import BeautifulSoup

def get_course_commentList(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/course/comment/getCourseCommentList?courseId={}&lessonId=&pageNum=1'.format(
        courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "开悟课程/获取评论"

    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')


def get_distribution_poster_data(courseId, decorateId, gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/course/distribution/getDistributionPosterData?courseId={}&decorateId={}'.format(
        courseId, decorateId)
    # header = get_header(url="https://kaiwu.lagou.com/distribution/appCenter.html")
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取分销海报数据"

    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')


def get_credit_center_info(userToken):
    url = 'https://gate.lagou.com/v1/neirong/course/user_growth/getCreditCenterInfo'
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "学分中心"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')


def get_course_credit_info(userToken, courseId):
    url = 'https://gate.lagou.com/v1/neirong/course/user_growth/getCourseCreditInfo?courseId={}'.format(courseId)
    header = get_edu_app_header(userToken=userToken, DA=False)
    remark = "个人成就中心"
    return get_requests(url=url, headers=header, remark=remark, rd='Bob')


def get_distribution_course_list(gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/course/distribution/getDistributionCourseList'
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取推广课程列表"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')



def get_my_earing(gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/course/distribution/getMyEarning'
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取我的收益"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')



def get_user_earnings_detail(gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/course/distribution/getUserEarningsDetail?nextStartId=0&amountType=0'
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取收益详情"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')



def get_wei_xin_user(gateLoginToken):
    url = 'https://gate.lagou.com/v1/neirong/course/distribution/getWeiXinUser'
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}","sec-fetch-user":"?1",'upgrade-insecure-requests':1}
    remark = "获取微信用户信息"
    return get_requests(url=url, headers=header, remark=remark,rd='Yuwei Cheng')

def get_course_info(gateLoginToken,courseId):
    url = "https://kaiwu.lagou.com/course/courseInfo.htm?courseId={}".format(courseId)
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    #header.add({"Cookie": f"WEXIN_UNIONID ={WEXIN_UNIONID};"})
    remark = "获取课程信息"
    r = get_requests(url=url, headers=header, remark=remark,rd='Yuwei Cheng')
    #专栏、视频课的价格策略id
    sellGoodsPriceId = re.findall(r'"sellGoodsPriceId":(.*?),', r)[0]
    #用户是否加入了会员
    joinMember = re.findall(r'"joinMember":(.*?),', r)[0]
    #该课程是否为秒杀课  true-秒杀课   flase-非秒杀课
    joinSeckill = re.findall(r'"joinSeckill":(.*?),', r)[0]
    lgCoinPrice = re.findall(r'"lgCoinPrice":(.*?),', r)[0]
    discounts = re.findall(r'"discounts":(.*?),', r)[0]
    #是否为免费会员
    freeForVip = re.findall(r'"freeForVip":(.*?),', r)[0]
    # 课程type 1-专栏  2-作者伴读  3-就业课 4 -视频课
    courseType = re.findall(r'"courseType":(.*?),', r)[0]
    userId = re.findall(r'userId:(.*?),',r)[0]
    soup = BeautifulSoup(r, "html.parser")
    userId = soup.find_all(type="text/javascript")[1]
    #针对就业课如果是年费会员则走
    if courseType == '3'and joinMember==True:
        print(courseType)
        memberPrice = re.findall(r'"memberPrice":(.*?),', r)
        memberStrategyPriceId = re.findall(r'"memberStrategyPriceId":(.*?),', r)
        return r, memberPrice, memberStrategyPriceId, joinMember
    else:
        return sellGoodsPriceId, joinMember, joinSeckill, lgCoinPrice, discounts, freeForVip, courseType,userId

if __name__ == '__main__':
    a = password_login('00552019120401','aaaaaa')
    print(a)

    #print(get_course_info('aa2f899270595b59b866bfbbf374643a90133d29e13e2cd59e073bbdd97f2047',319))

