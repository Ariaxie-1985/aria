# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_requests, form_post,login,get_code_token,json_post
# login('0086','18810432995')

def reward(taskLabel,taskGroup,rcode):
    url='https://jf.lagou.com/task/center/receive/reward.json'
    header=get_code_token('https://jf.lagou.com/task/center/index.htm')
    data={'taskLabel':taskLabel,'taskGroup':taskGroup,'rcode':rcode,'isAllReceive':False,'deviceType':'web'}
    return json_post(url=url,headers=header,data=data,remark='领取')

# tasks()
# reward()