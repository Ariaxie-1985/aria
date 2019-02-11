# -*- coding: utf8 -*-
__author__ = 'cloudyyan'

from utils.util import get_app_header,form_post,get_requests,assert_equal,login,get_code_token

def MySchedule(userid):
    '''
    查询我的排期，包括共享职位
    :return:
    '''
    header=get_app_header(userid)
    url="https://gate.lagou.com/v1/zhaopin/topCard/mySchedule?pageNo=1&pageSize=10"
    object=get_requests(url=url,headers=header,remark="查询我的排期，包括共享职位")
    message=object.json()['message']
    assert_equal("操作成功",message,"查询我的排期，包括共享职位接口正确","查询我的排期，包括共享职位接口错误")

def SendBusiness(userid):
    '''
    发送商机线索
    :param userid:
    :return:
    '''
    header=get_app_header(userid)
    url="https://gate.lagou.com/v1/zhaopin/topCard/sendBusiness"
    object=get_requests(url=url,headers=header,remark="发送商机线索")
    message=object.json()['message']
    assert_equal("操作成功",message,"发送商机线索接口正确","发送商机线索接口错误")

def ScheduleList(userid):
    '''
    查询未来28天排期
    :param userid:
    :return:
    '''
    login('00852','20181205')
    position_url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    position_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    s = form_post(url=position_url,headers=position_header,data={'pageNo':1},remark='获取职位id')
    positionId=s['content']['data']['parentPositionVOs'][1]['positions'][0]['positionId']
    print(positionId)
    header=get_app_header(userid)
    url="https://gate.lagou.com/v1/zhaopin/topCard/"+str(positionId)+"/scheduleList"
    object=get_requests(url=url,headers=header,remark="查询未来28天排期")
    message=object.json()['message']
    assert_equal("操作成功",message,"查询未来28天排期接口正确","查询未来28天排期接口错误")





# MySchedule(100014641)
# SendBusiness(100014641)
# ScheduleList(100014641)