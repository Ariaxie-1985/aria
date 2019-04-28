# coding:utf-8
# @Time  : 2019-04-28 11:05
# @Author: Xiawang
from utils.util import get_app_header, json_post, form_post

host = 'https://gate.lagou.com/v1/neirong'
header = get_app_header(100014641)


def resumes_list():
    url = host + '/resumes/list'
    remark = '消息--对话--发送简历--显示简历列表，包含附件和在线简历'
    return form_post(url=url, headers=header, remark=remark)
