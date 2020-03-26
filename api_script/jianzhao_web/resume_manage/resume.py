# coding:utf-8
# @Time  : 2020/3/18 19:22
# @Author: Xiawang
# Description:
from utils.util import get_header, get_requests


def get_not_read_resume_count():
    url = 'https://easy.lagou.com/resume/notReadResumeCount.json'
    header = get_header(
        url='https://easy.lagou.com/resume/new/list.htm?can=false&needQueryAmount=false&parentPositionIds=')
    return get_requests(url=url, headers=header, remark="统计未读简历数").json()
