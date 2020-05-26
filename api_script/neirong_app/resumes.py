# coding:utf-8
# @Time  : 2019-04-28 11:05
# @Author: Xiawang
import json
import random

from utils.util import get_app_header, json_post, form_post, app_header_999, get_requests, delete_requests
from faker import Faker

host = 'https://gate.lagou.com/v1/neirong'

fake = Faker('zh_CN')
sex = ['女', '男']


def resumes_list(userToken, ip_port=None, userId=None):
    url = host + '/resumes/list'
    header = app_header_999(userToken, DA=False, userId=userId)
    remark = '消息--对话--发送简历--显示简历列表，包含附件和在线简历'
    return form_post(url=url, headers=header, remark=remark, ip_port=ip_port)


def guideBasicInfo(phone, userIdentity, userToken, joinWorkTime="2013.07", name=None):
    '''

    :param phone:
    :param userIdentity:1 学生, 2 非学生
    :param userToken:
    :return:
    '''
    if phone[0:4] != '0086':
        phone = '+' + phone
    if name is None:
        name = '拉勾测试自动化' + fake.name()
    url = 'https://gate.lagou.com/v1/neirong/resumes/guideBasicInfo'
    header = app_header_999(userToken, DA=False)
    data = {
        "phone": phone,
        "userIdentity": userIdentity,
        "headPic": "https://www.lgstatic.com/common/image/pc/default_boy_headpic2.png",
        "liveCity": "北京",
        "email": fake.email(),
        "birthday": "1990.05",
        "sex": sex[random.randint(0, 1)],
        "name": name
    }
    if userIdentity == 1:
        return json_post(url=url, data=data, headers=header, app=True, remark="提交类型为学生的基本信息")
    if joinWorkTime == '暂无工作经历':
        data["joinWorkTime"] = "暂无工作经历"
        return json_post(url=url, data=data, headers=header, app=True, remark="提交类型为非学生但无工作经历的基本信息")
    data["joinWorkTime"] = joinWorkTime
    return json_post(url=url, data=data, headers=header, app=True, remark="提交类型为非学生但有工作经历的基本信息")


def educationExperiences(userToken, **kwargs):
    url = 'https://gate.lagou.com/v1/neirong/educationExperiences/'
    schoolName = kwargs.get('schoolName', '陕西文理学院')
    education = kwargs.get('education', '本科')
    startDate = kwargs.get('startDate', '2009.09')
    endDate = kwargs.get('endDate', '2013.07')
    data = {
        "education": education,
        "endDate": endDate,
        "id": 0,
        "isUnifiedEntrance": 1,
        "professional": "计算机科学与技术",
        "schoolName": schoolName,
        "startDate": startDate
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
        "positionNameType2": "影视|媒体",
        "expectStatus": "积极找工作",
        "expectCity": "北京",
        "positionType": "实习",
        "positionName": "经纪人|星探",
        "expectArrivalTime": "随时",
        "positionNameType1": "文娱|传媒|艺术|体育",
        "expectSalary": "8k-12k"
    }
    header = app_header_999(userToken, DA=False)
    return json_post(url=url, data=data, headers=header, remark="提交求职意向")


def workExperiences(userToken, **kwargs):
    url = 'https://gate.lagou.com/v1/neirong/workExperiences/'
    startDate = kwargs.get('startDate', '2015.09')
    endDate = kwargs.get('endDate', '至今')
    companyName = kwargs.get('companyName', '杰威尔音乐有限公司')
    data = {
        "id": 0,
        "workContent": "<p>跟进迭代测试工作，用户反馈；</p><p>dubbo接口测试，http接口测试</p>",
        "positionType1": "销售类",
        "isFilter": True,
        "positionType": "销售顾问",
        "positionType2": "销售",
        "endDate": endDate,
        "positionName": "艺人经纪",
        "companyName": companyName,
        "startDate": startDate,
        "companyIndustry": "分类信息",
        "department": "用户价值部",
        "skillLabels": ["测试"]
    }
    header = app_header_999(userToken, DA=False)
    return json_post(url=url, data=data, headers=header, remark="提交工作经历")


def set_basicInfo(userToken, phone):
    url = 'https://gate.lagou.com/v1/neirong/resumes/basicInfo/'
    header = app_header_999(userToken)
    data = {
        "phone": phone,
        "userIdentity": 2,
        "joinWorkTime": "2013.07",
        "headPic": "https://www.lgstatic.com/common/image/pc/default_boy_headpic2.png",
        "portrait": "https://www.lgstatic.com/common/image/pc/default_boy_headpic2.png",
        "birthday": "1990.05",
        "email": "bcui@jing.cn",
        "liveCity": "北京",
        "sex": "男",
        "name": "刘岩"
    }
    return json_post(url=url, headers=header, data=data, remark="更新简历的基本信息")


def get_detail(userToken):
    url = 'https://gate.lagou.com/v1/neirong/resumes/detail'
    header = app_header_999(userToken, DA=False)
    return get_requests(url=url, headers=header, remark="获取简历详情").json()


def delete_education_experiences(userToken, id):
    url = 'https://gate.lagou.com/v1/neirong/educationExperiences/{}'.format(id)
    header = app_header_999(userToken, DA=False)
    return delete_requests(url=url, headers=header, remark="删除教育经历")


def delete_workExperiences(userToken, id):
    url = 'https://gate.lagou.com/v1/neirong/workExperiences/{}'.format(id)
    header = app_header_999(userToken, DA=False)
    return delete_requests(url=url, headers=header, remark="删除工作经历")


if __name__ == '__main__':
    r = guideBasicInfo(phone='0085220180914',
                       userToken='97d82a3c008253fb633842b6b27129b231bea2949314555a6996cb2a3e3e0779')
    print(r)
