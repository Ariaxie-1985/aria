# -*- coding: utf8 -*-
__author__ = 'cloudyyan'

from utils.util import get_app_header,form_post,get_requests,assert_equal,login,json_put,json_post,wait
import time,datetime

'''
简历状态
'''
def ResumeID(userid):
    '''
    获得简历id
    :return:
    '''
    header=get_app_header(userid)
    # url="https://gate.lagou.com/v1/zhaopin/orderResumes/pages?positionId=0&resumeStage=2&onlyUnread=false&catchTag=0&pageSize=20"
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/query"
    id=json_post(url=url,headers=header,data={'catchTag':'0','channelIds':[0],'pageSize':'20','positionIds':[0],'resumeStageCode':'1'},remark="分页查询简历")
    orderResumeId=id['content']['result'][0]['orderResumeId']
    return orderResumeId


def OrderResumeState(userid,orderResumeId):
    '''
    设置为待沟通
    :param userid:
    :return:
    '''
    header=get_app_header(userid)
    # orderResumeId=ResumeID(100014641)
    wait(2000)
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/"+str(orderResumeId)+"/link"
    object=json_put(url=url,headers=header,remark="设置为待沟通")
    meassage=object['message']
    assert_equal("操作成功",meassage,"设置为待沟通成功","设置为待沟通接口报错")
    return object

def Interview(userid,orderResumeId):
    '''
    安排面试时间
    :return:
    '''
    now_time = time.time()+1000
    interviewTime=(int(round(now_time * 1000)))
    # orderResumeId=ResumeID(100014641)
    wait(4000)
    header=get_app_header(userid)
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/"+str(orderResumeId)+"/interview"
    data={'contact': '袁月','contactAddress': '中关村','contactPhone': '15011220359','interviewTime': int(interviewTime),'orderResumeId': orderResumeId}
    object=json_post(url=url,data=data,headers=header,remark="安排面试")
    message=object['message']
    assert_equal("操作成功",message,"安排面试成功","安排面试接口失败")
    wait(5000)
    return object

def reviseOrderResumesTime(userid):
    '''
    修改面试时间
    :param userid:
    :return:
    '''
    now_time = time.time()+4000
    interviewTime=(int(round(now_time * 1000)))
    orderResumeId=ResumeID(100014641)
    header=get_app_header(userid)
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/"+str(orderResumeId)+"/interview/datetime"
    data={'interviewTime': interviewTime,'orderResumeId': orderResumeId}
    object=json_put(url=url,remark="修改面试时间",headers=header,data=data)
    message=object['message']
    assert_equal("操作成功",message,"修改面试时间成功","修改面试时间失败")
    return object


def luyong(userid,orderResumeId):
    '''
    标记为录用
    转移到已入职
    淘汰
    :return:
    '''
    header=get_app_header(userid)
    # orderResumeId=ResumeID(100014641)
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/"+str(orderResumeId)+"/luyong"
    object=json_put(url=url,headers=header,remark="标记为录用")
    message=object['message']
    assert_equal("操作成功",message,"标记为录用成功","标记为录用失败")
    return object

def ruzhi(userid,orderResumeId):
    header=get_app_header(userid)
    # orderResumeId=ResumeID(userid)
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/"+str(orderResumeId)+"/employed"
    object=json_put(url=url,headers=header,remark="转移到已入职")
    message=object['message']
    assert_equal("操作成功",message,"转移到已入职成功","转移到已入职失败")
    return object

def taotai(userid,orderResumeId):
    header=get_app_header(userid)
    # orderResumeId=ResumeID(userid)
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/"+str(orderResumeId)+"/obsolete"
    object=json_put(url=url,headers=header,remark="淘汰")
    message=object['message']
    assert_equal("操作成功",message,"淘汰成功","淘汰失败")
    return object
# ResumeID(100014641)
# OrderResumeState(100014641)
# Interview(100014641)
# reviseOrderResumesTime(100014641)
# luyong(100014641)