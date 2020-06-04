# -*- coding: utf8 -*-
__author__ = 'cloudyyan'

from utils.util import get_app_header,form_post,get_requests,assert_equal,login

def OrderResumespage(userid):
    '''
    查询简历列表
    '''
    header=get_app_header(userid)
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/query"
    data=""
    object=form_post(url=url,data=data,headers=header,remark="查询简历列表")
    message=object['message']
    assert_equal("操作成功",message,"查询简历列表正确","查询简历列表接口报错")


def OrderResumespageStage(userid):
    '''
    查询简历阶段
    :param userid:
    :return:
    '''
    header=get_app_header(userid)
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/pages?positionId=0&resumeStage=2&onlyUnread=false&catchTag=0&pageSize=20"
    id=get_requests(url=url,headers=header,remark="分页查询简历")
    orderResumeId=id['content']['result'][0]['orderResumeId']
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/"+str(orderResumeId)+"/stage"
    object=get_requests(url=url,headers=header,remark="查询简历阶段")
    meassage=object['message']
    assert_equal("操作成功",meassage,"查询简历阶段","查询简历阶段接口测试失败")


def NotReadCount(userid):
    header=get_app_header(userid)
    url="https://gate.lagou.com/v1/zhaopin/orderResumes/not_read_resume_count?parentPositionId=0"
    object=get_requests(url=url,headers=header,remark="未读简历数量")
    meassage=object['message']
    assert_equal("操作成功",meassage,"未读简历数量正确","未读简历数量报错")


# OrderResumespage(100014641)
# OrderResumespageStage(100014641)
# NotReadCount(100014641)