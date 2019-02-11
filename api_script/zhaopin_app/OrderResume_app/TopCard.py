# -*- coding: utf8 -*-
__author__ = 'cloudyyan'

from utils.util import get_app_header,form_post,get_requests,assert_equal,login,get_code_token,put_requests
from api_script.zhaopin_app.b_searchResumePosition import get_strict_pages_orderResumes
import datetime
import  time
def PositionId():
    '''
    获取职位id
    :param userid:
    :return:
    '''
    login('00852','20181205')
    res=get_strict_pages_orderResumes()
    positionId=res['content']['result'][0]['id']
    return positionId
def TopCard(userid):
    '''
    使用置顶卡，既添加置顶卡排期
    :return:
    '''
    id=PositionId()
    times=time.strftime('%Y%m%d',time.localtime(time.time()+90000))
    header=get_app_header(userid)
    url="https://gate.lagou.com/v1/zhaopin/topCard/addSchedule?positionId="+str(id)+"&ids="+str(times)+"-1-1.0"
    src=put_requests(url=url,remark="使用置顶卡，即添加置顶卡排期",headers=header)
    message=src.json()['message']
    assert_equal("操作成功",message,"使用置顶卡，即添加置顶卡排期正确","使用置顶卡，即添加置顶卡排期接口报错")

def offlineWin(userid):
    '''
    置顶卡操作前，弹窗判断
    :return: 
    '''
    login('00852','20181205')
    header = get_code_token('https://easy.lagou.com/userGoodsRecord/toCard/index.htm')
    sechedule_url="https://easy.lagou.com/topCard/my-schedule.json?positionId=&city=&location=&status=&pageNo=1&pageSize=10"
    object=get_requests(url=sechedule_url,remark="获取置顶卡排序id",headers=header).json()
    id=object['content']['data']['scheduleList'][0]['id']
    print(id)
    url="https://gate.lagou.com/v1/zhaopin/topCard/"+str(id)+"/offlineWin?operate=offline"
    header=get_app_header(userid)
    src=get_requests(url=url,remark="置顶卡操作前，弹窗判断",headers=header)
    message=src.json()['message']
    assert_equal("操作成功",message,"置顶卡操作前，弹窗判断正确","置顶卡操作前，弹窗判断接口报错")
    return id
def OperateSchedule(userid):
    '''
    置顶卡操作下线或取消预订
    :return:
    '''
    login('00852','20181205')
    header = get_code_token('https://easy.lagou.com/userGoodsRecord/toCard/index.htm')
    sechedule_url="https://easy.lagou.com/topCard/my-schedule.json?positionId=&city=&location=&status=&pageNo=1&pageSize=10"
    object=get_requests(url=sechedule_url,remark="获取置顶卡排序id",headers=header).json()
    id=object['content']['data']['scheduleList'][0]['id']
    print(id)
    header=get_app_header(userid)
    url="https://gate.lagou.com/v1/zhaopin/topCard/"+str(id)+"/operateSchedule?operate=offline"
    src=put_requests(url=url,remark="置顶卡操作下线或取消预订",headers=header)
    print(src.json())
    message=src.json()['message']
    assert_equal("操作成功",message,"置顶卡操作下线或取消预订正确","置顶卡操作下线或取消预订接口报错")



PositionId()
TopCard(100014641)
offlineWin(100014641)
OperateSchedule(100014641)
