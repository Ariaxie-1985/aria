# coding:utf-8
# @Time  : 2019-04-28 11:05
# @Author: Xiawang
import json
import random

from utils.util import get_app_header, json_post, form_post, app_header_999
from faker import Faker

host = 'https://gate.lagou.com/v1/neirong'
header = get_app_header(100014641)

fake = Faker('zh_CN')
sex = ['女', '男']


def resumes_list():
    url = host + '/resumes/list'
    remark = '消息--对话--发送简历--显示简历列表，包含附件和在线简历'
    return form_post(url=url, headers=header, remark=remark)


def guideBasicInfo(phone, userIdentity, userToken, joinWorkTime="2013.07"):
    '''

    :param phone:
    :param userIdentity:1 学生, 2非学生
    :param userToken:
    :return:
    '''
    if phone[0:4] != '0086':
        phone = '+' + phone
    url = 'https://gate.lagou.com/v1/neirong/resumes/guideBasicInfo'
    header = app_header_999(userToken, DA=False)
    if userIdentity == 1:
        data = {
            "phone": phone,
            "userIdentity": userIdentity,
            "headPic": "https://www.lgstatic.com/common/image/pc/default_boy_headpic2.png",
            "liveCity": "北京",
            "email": fake.email(),
            "birthday": "1990.05",
            "sex": sex[random.randint(0, 1)],
            "name": fake.name()
        }
        return json_post(url=url, data=data, headers=header, app=True, remark="提交类型为学生的基本信息")
    if joinWorkTime == '暂无工作经历':
        data = {
            "phone": phone,
            "userIdentity": userIdentity,
            "headPic": "https://www.lgstatic.com/common/image/pc/default_boy_headpic2.png",
            "liveCity": "北京",
            "email": fake.email(),
            "birthday": "1990.05",
            "sex": sex[random.randint(0, 1)],
            "name": fake.name(),
            "joinWorkTime": "暂无工作经历"
        }
        return json_post(url=url, data=data, headers=header, app=True, remark="提交类型为非学生但无工作经历的基本信息")
    data = {
        "phone": phone,
        "userIdentity": userIdentity,
        "headPic": "https://www.lgstatic.com/common/image/pc/default_boy_headpic2.png",
        "liveCity": "北京",
        "email": fake.email(),
        "birthday": "1990.05",
        "sex": sex[random.randint(0, 1)],
        "name": fake.name(),
        "joinWorkTime": joinWorkTime
    }
    return json_post(url=url, data=data, headers=header, app=True, remark="提交类型为非学生但有工作经历的基本信息")


def educationExperiences(userToken):
    url = 'https://gate.lagou.com/v1/neirong/educationExperiences/'
    data = {
        "cardType": 0,
        "resumeId": 0,
        "major": "计算机科学与技术",
        "professional": "计算机科学与技术",
        "schoolBadge": "",
        "schoolName": "北京理工大学",
        "id": 0,
        "education": "本科",
        "startDate": "2009",
        "endDate": "2013",
        "logo": ""
    }
    header = app_header_999(userToken, DA=False)
    return json_post(url=url, data=data, headers=header, remark="提交教育经历")


def personalCards(userToken):
    url = 'https://gate.lagou.com/v1/neirong/personalCards/'
    data = {
        "selfDescription": "<p>虽然我是学生，但我很有冲劲，选我吧！</p>"
    }
    header = app_header_999(userToken, DA=False)
    return json_post(url=url, data=data, headers=header, remark="提交个人名片")


def abilityLabels(userToken):
    url = 'https://gate.lagou.com/v1/neirong/abilityLabels/'
    data = ["沟通协调能力", "自驱动", "团队管理"]
    header = app_header_999(userToken, DA=False)
    return json_post(url=url, data=data, headers=header, remark="提交综合能力")


def expectJob(userToken):
    url = 'https://gate.lagou.com/v1/entry/expectJob'
    data = {
        "positionNameType2": "后端开发",
        "expectStatus": "积极找工作",
        "expectCity": "北京",
        "positionType": "实习",
        "positionName": "Python",
        "expectArrivalTime": "随时",
        "positionNameType1": "开发|测试|运维类",
        "expectSalary": "8k-12k"
    }
    header = app_header_999(userToken, DA=False)
    return json_post(url=url, data=data, headers=header, remark="提交求职意向")


def workExperiences(userToken):
    url = 'https://gate.lagou.com/v1/neirong/workExperiences/'
    data = {
        "id": 0,
        "workContent": "<p>跟进迭代测试工作，用户反馈；</p><p>dubbo接口测试，http接口测试</p>",
        "positionType1": "开发|测试|运维类",
        "isFilter": True,
        "positionType": "测试工程师",
        "positionType2": "测试",
        "endDate": "至今",
        "positionName": "测试工程师",
        "companyName": "拉勾网",
        "startDate": "2015.09",
        "companyIndustry": "分类信息",
        "department": "用户价值部",
        "skillLabels": ["测试"]
    }
    header = app_header_999(userToken, DA=False)
    return json_post(url=url, data=data, headers=header, remark="提交工作经历")


if __name__ == '__main__':
    r = guideBasicInfo(phone='0085220180914',
                       userToken='97d82a3c008253fb633842b6b27129b231bea2949314555a6996cb2a3e3e0779')
    print(r)
