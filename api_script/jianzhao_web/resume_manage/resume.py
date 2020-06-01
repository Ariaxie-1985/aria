# coding:utf-8
# @Time  : 2020/3/18 19:22
# @Author: Xiawang
# Description:
from utils.util import get_header, get_requests


def get_not_read_resume_count(ip_port=None):
    url = 'https://easy.lagou.com/resume/notReadResumeCount.json'
    header = get_header(
        url='https://easy.lagou.com/resume/new/list.htm?can=false&needQueryAmount=false&parentPositionIds=',
        ip_port=ip_port)
    return get_requests(url=url, headers=header, remark="统计未读简历数", ip_port=ip_port)
