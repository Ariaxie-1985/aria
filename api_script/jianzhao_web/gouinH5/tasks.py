# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_requests, form_post,login,get_code_token
# login('0086','18810432995')
# login('00852','20181205')
def tasks():
    url='https://jf.lagou.com/task/center/task.json'
    return get_requests(url=url,remark='任务中心首页')
# tasks()
# s=tasks()
# list=s['content']['data']['taskPage']['dayTasks']['taskList']
# for i in list:
#     if i['status']=='COMPLETED':
#
#         break
# print (i)