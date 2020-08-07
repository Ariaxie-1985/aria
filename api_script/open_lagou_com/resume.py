# coding:utf-8
# @Time  : 2020/6/4 11:28
# @Author: Xiawang
# Description:
import datetime
import time

from utils.util import get_requests, form_post
from faker import Faker

fake = Faker('zh_CN')


def get_resume_list(access_token, stage='NEW'):
    url = f'https://open.lagou.com/v1/resume/list'
    today = datetime.datetime.now()
    start_time = int(str(time.mktime(time.strptime((today - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
                                                   '%Y-%m-%d %H:%M:%S')) * 1000).split(".")[0])
    end_time = int(str(int(time.time())) + '000')
    data = {'access_token': access_token, 'start_time': start_time, 'end_time': end_time, 'stage': stage}
    remark = '获取简历列表信息'
    return get_requests(url=url, data=data, remark=remark, rd='刘汝鹏')


def get_online_resume(access_token, resume_id):
    url = f'https://open.lagou.com/v1/resume/online/get'
    data = {'resume_id': resume_id, 'access_token': access_token}
    remark = '获取在线简历信息'
    return get_requests(url=url, data=data, remark=remark)


def get_attachment_resume(access_token, resume_id):
    url = f'https://open.lagou.com/v1/resume/attachment/get'
    data = {'resume_id': resume_id, 'access_token': access_token}
    remark = '获取附件简历信息'
    return get_requests(url=url, data=data, remark=remark)


def get_contact(access_token, resume_id):
    url = f'https://open.lagou.com/v1/resume/contact/get'
    data = {'resume_id': resume_id, 'access_token': access_token}
    remark = '标记初筛'
    return get_requests(url=url, data=data, remark=remark)


def get_interview(access_token, resume_id, **kwargs):
    link_phone = kwargs.get('link_phone', '18500000000')
    link_man = kwargs.get('link_man', fake.name())
    interview_address = kwargs.get('interview_address', fake.address())
    interview_time = kwargs.get('interview_time', int(round(time.time() * 1000)))
    url = f'https://open.lagou.com/v1/resume/interview?access_token={access_token}'
    data = {'resume_id': resume_id, 'link_phone': link_phone, 'link_man': link_man,
            'interview_address': interview_address, 'interview_time': interview_time}
    remark = '邀约面试'
    return form_post(url=url, data=data, remark=remark)


def get_obsolete(access_token, resume_id):
    url = f'https://open.lagou.com/v1/resume/obsolete?access_token={access_token}'
    data = {'resume_id': resume_id}
    remark = '淘汰候选人'
    return form_post(url=url, data=data, remark=remark)
