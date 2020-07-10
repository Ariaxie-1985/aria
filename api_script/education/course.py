# coding:utf-8
# @Time  : 2020/3/6 16:16
# @Author: Xiawang
# Description:
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import add_saveCompany
from utils.util import get_edu_app_header, get_requests, json_post
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
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取微信用户信息"
    return get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')


# 通过接口返回相关参数
def get_course_info(courseId, gateLoginToken):
    url = "https://kaiwu.lagou.com/course/courseInfo.htm?courseId={}".format(courseId)
    # header = {"Cookie": f"WEXIN_UNIONID=908538efc0e17cfae112d0d3cdd41a965731cf2a550fa7b765061451416c167e0fdcaf6e2c1327bbf6224a5a9e6f89c30e71e26831e408cad1527f57c28339808317c7f2185bfbfc; WEIXIN_OPENID_2=ec7ee26837c6d8df09aa5a00b589ae594b976a767bab7faa2ffab0895d2508d98d35f6ab8842733083a1fc1059a9b1c64656abe5972cce4fe6a600934e0b1ff32f7b0855bfb2af64; JSESSIONID=ABAAABAAAECABEH4FB74FC04CF8A133331985555C909346; gate_login_token=aa2f899270595b59b866bfbbf374643a90133d29e13e2cd59e073bbdd97f2047; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215763008%22%2C%22first_id%22%3A%221730e5bb03429e-0844bd9e5982be-91c1932-346800-1730e5bb0356c1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Linux%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2278.0.3904.62%22%7D%2C%22%24device_id%22%3A%221730e5bb03429e-0844bd9e5982be-91c1932-346800-1730e5bb0356c1%22%7D", "X-L-REQ-HEADER": "{deviceType:1}"}
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remark = "获取课程信息"
    r = get_requests(url=url, headers=header, remark=remark, rd='Yuwei Cheng')
    soup = BeautifulSoup(r, "html.parser")
    orderTokenlist = soup.find_all(type="text/javascript")[1]
    # print(orderTokenlist)
    orderToken1 = re.findall(r'window.orderToken =(.*)', str(orderTokenlist))[0]
    # 删除两边‘；和空字符串
    orderToken = orderToken1.strip().strip("';")
    # 专栏、视频课的价格策略id
    sellGoodsPriceId = re.findall(r'"sellGoodsPriceId":(.*?),', r)[0]
    # 用户是否加入了会员
    joinMember = re.findall(r'"joinMember":(.*?),', r)[0]
    # 该课程是否为秒杀课  true-秒杀课   flase-非秒杀课
    joinSeckill = re.findall(r'"joinSeckill":(.*?),', r)[0]
    lgCoinPrice = re.findall(r'"lgCoinPrice":(.*?),', r)[0]
    discounts = re.findall(r'"discounts":(.*?),', r)[0]
    # 是否为免费会员
    freeForVip = re.findall(r'"freeForVip":(.*?),', r)[0]
    # 课程type 1-专栏  2-作者伴读  3-就业课 4 -视频课
    courseType = re.findall(r'"courseType":(.*?),', r)[0]
    # 当用户么有购买过课，则从这里获取shopOrderToken，已购买的从上次订单中获取shopOrderToken值

    # orderToken = re.findall(r'"orderToken":(.*?),', r)[0]
    # 针对就业课如果是年费会员则走,目前可暂时不考虑-从正常的列表内无法获取到就业课id
    if courseType == '3' and joinMember == "true":
        memberPrice = re.findall(r'"memberPrice":(.*?),', r)
        memberStrategyPriceId = re.findall(r'"memberStrategyPriceId":(.*?),', r
        print(sellGoodsPriceId, joinMember, joinSeckill, lgCoinPrice, discounts, freeForVip, courseType, orderToken)
        return sellGoodsPriceId, joinMember, joinSeckill, lgCoinPrice, discounts, freeForVip, courseType, orderToken, memberPrice, memberStrategyPriceId
    else:
        print(sellGoodsPriceId, joinMember, joinSeckill, lgCoinPrice, discounts, freeForVip, courseType, orderToken)
        return sellGoodsPriceId, joinMember, joinSeckill, lgCoinPrice, discounts, freeForVip, courseType, orderToken


def receive_credit(gateLoginToken):
    data = {
        "taskAbbreviation": "CREDIT_CENTER_DAILY_LOGIN"
    }
    url = 'https://gate.lagou.com/v1/neirong/course/user_growth/receiveCredit'
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remarke = '学分领取成功'
    return json_post(url=url, headers=header, remark=remarke, data=data, rd='Bob')


def exchange_present(gateLoginToken):
    data = {
        "presentId": 5
    }
    url = 'https://gate.lagou.com/v1/neirong/course/user_growth/exchangePresent'
    header = {"Cookie": f"gate_login_token ={gateLoginToken};", "X-L-REQ-HEADER": "{deviceType:1}"}
    remarke = '礼物兑换成功'
    return json_post(url=url, headers=header, remark=remarke, data=data, rd='Bob')
