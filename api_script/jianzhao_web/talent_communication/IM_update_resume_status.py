# coding:utf-8
# @Time  : 2019-07-03 10:53
# @Author: Xiawang
import random
import string
import time

from utils.util import get_code_token, get_requests, login, get_header, json_post, form_post
import json
from faker import Faker

faker = Faker('zh_CN')


def data_provider():
    url = 'https://easy.lagou.com/im/session/list.json?pageNo=1&pageSize=50&createBy=0&unReadOnly=0'
    header = get_code_token(url='https://easy.lagou.com/im/chat/index.htm')
    session_results = get_requests(url=url, headers=header, remark='获取新简历')
    for session in session_results['content']['rows']:
        attachment = json.loads(session['attachment'])
        if attachment['resumeStage'] == 'NEW':
            sessionId = session['sessionId']
            outerPositionId = attachment['positionId']
            cUserId = attachment['cUserId']
            print(cUserId)
            session_url = 'https://easy.lagou.com/im/chat/getMDSUserInfo/{}.json'.format(sessionId)
            resume = get_requests(url=session_url, headers=header, remark='获取resumeId', rd='mandy')
            try:
                resumeId = resume['content']['data']['resumeId']
            except KeyError:
                pass

    return sessionId, cUserId, outerPositionId, resumeId


def chat_getMDSUserInfo(cUserId):
    url = 'https://easy.lagou.com/im/chat/getMDSUserInfo/{}.json?'.format(cUserId)
    header = get_header(url='https://easy.lagou.com/im/chat/index.htm')
    return get_requests(url=url, headers=header, remark='会话详情信息')


def position_selector(resumeId, sessionId):
    url = 'https://easy.lagou.com/im/session/position/selector.json?resumeId={}&sessionId={}'.format(resumeId,
                                                                                                     sessionId)
    header = get_header(url='https://easy.lagou.com/im/chat/index.htm')
    return get_requests(url=url, headers=header, remark='im切换职位列表')


def resume_interview(resumeId, positionId):
    url = 'https://easy.lagou.com/im/resume/interview.json'
    header = get_code_token(url='https://easy.lagou.com/can/new/detail.htm?resumeId={}'.format(resumeId))
    data = {
        "positionId": positionId,
        "resumeId": resumeId,
        "linkTel": 18500000000 + random.randint(10000000, 80000000),
        "linkMan": "hr",
        "linkAddress": faker.address(),
        "templateId": 4039,
        "interviewTime": str(time.time())[:10],
        "addInfo": "面试",
        "forwardUserList": [{
            "phone": "13800000000",
            "name": "aaa",
            "email": "a@kll.com"
        }]
    }
    return json_post(url=url, headers=header, data=data, remark='面试邀约')


def resume_lastInterview(resumeId):
    url = 'https://easy.lagou.com/im/resume/lastInterview.json?resumeId={}'.format(resumeId)
    header = get_header(url='https://easy.lagou.com/im/chat/index.htm')
    get_requests(url=url, headers=header, remark='获取最近一次面试邀约信息')


def resume_obsolete(resumeId):
    url = 'https://easy.lagou.com/im/resume/obsolete.json'
    header = get_code_token(url='https://easy.lagou.com/can/new/detail.htm?resumeId={}'.format(resumeId))
    data = {'resumeId': resumeId, 'contactC': False}
    return form_post(url=url, headers=header, data=data, remark='淘汰候选人')


def can_searchCc(keyWord):
    url = 'https://easy.lagou.com/can/searchCc.json'
    header = get_header(url)
    data = {'keyWord': keyWord}
    return form_post(url=url, data=data, headers=header, remark='搜索抄送记录和同事信息')


def can_recentInterviewCc():
    url = 'https://easy.lagou.com/can/recentInterviewCc.json'
    header = get_header(url)
    return form_post(url=url, headers=header, remark='获取最近抄送信息')


def send_chat():
    url = 'https://easy.lagou.com/im/chat/send/100015734.json'
    header = get_header(url='https://easy.lagou.com/im/chat/index.htm')
    data = {
        'content':'第一次测试',
        'attach':''.join(random.sample(string.ascii_letters + string.digits, 11)),
        'lagouPositionId' : '5378661'
    }
    return form_post(url=url, headers=header, data=data,remark='发送消息会话')

if __name__ == '__main__':
    login('00852', '20181205')
    # print(send_chat())
    # print(data_provider())
    # position_selector(1144459583050354688,100019968)
    # chat_getMDSUserInfo(100014095)
    # resume_interview(1144459583050354688,13849191)
    # resume_lastInterview(1144459583050354688)
