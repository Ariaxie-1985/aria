# coding:utf-8
# @Time  : 2019-04-28 15:07
# @Author: Xiawang
from utils.util import get_app_header, get_requests

host = 'https://gate.lagou.com/v1/zhaopin'
header = get_app_header(100014641)


def member_all():
    url = host + '/bUser/member/all?pageNo=1&pageSize=15'
    remark = '查看我公司下的成员'
    return get_requests(url=url, headers=header, remark=remark)
