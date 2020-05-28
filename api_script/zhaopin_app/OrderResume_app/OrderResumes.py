# -*- coding: utf8 -*-
__author__ = 'cloudyyan'

from utils.util import get_app_header, form_post, get_requests, assert_equal, login, wait

'''
    1、分页查询简历
    2、生成或获取简历公开查看链接
'''


def orderResumes(userid):
    '''分页查询简历'''
    header = get_app_header(userid)
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/pages?positionId=0&resumeStage=2&onlyUnread=false&catchTag=0&pageSize=20"
    data = "{'positionId':0,'resumeStage':2,'onlyUnread':false,'catchTag':0,'pageSize':20}"
    id = get_requests(url=url, headers=header, remark="分页查询简历")
    message = id['message']
    orderId = id['content']['result'][0]['orderId']
    orderResumeId = id['content']['result'][0]['orderResumeId']
    print(orderId)
    assert_equal("操作成功", message, "分页查询简历正确", "分页查询接口报错")
    return orderId, orderResumeId


def checkOrderResumes(userid):
    '''
    生成或获取简历公开查看链接(Alanzhang)
    :return:
    '''
    login('00852', '20181205')
    wait(2000)
    id = get_requests("https://easy.lagou.com/can/new/list.json", headers=None, remark="获得简历id")
    orderid = id['content']['rows'][0]['id']
    print(orderid)
    header = get_app_header(userid)
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/" + orderid + "/public/url?generatesANew=false"
    jsonobject = get_requests(url=url, headers=header, remark="生成或获取简历公开查看链接")
    meassage = jsonobject['message']
    assert_equal("操作成功", meassage, "生成或获取简历公开查看链接", "生成公开链接错误")


def viewOrderResume(userid):
    '''
    简历详情查询
    :param userid:
    :param orderid:
    :return:
    '''
    # print(str(orderResumes(100014641)))
    list = orderResumes(84)
    orderId = list[0]
    header = get_app_header(userid)
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/getByLGOrderId?lgOrderId=" + str(orderId) + "&needImg=false"
    print(url)
    jsonobject = get_requests(url=url, headers=header, remark="简历详情查询")
    meassage = jsonobject['message']
    assert_equal("操作成功", meassage, "查看简历成功", "查看简历失败")


def viewOrderResumeid(userid):
    list = orderResumes(84)
    orderResumeId = list[1]
    orderId = list[0]
    print(orderResumeId)
    print(orderId)
    header = get_app_header(userid)
    '''
   订单简历ID，"/{id}"查询时必须,orderId，"/getByLGOrderId"查询时必须
   '''
    url = "https://gate.lagou.com/v1/zhaopin/orderResumes/" + str(orderResumeId) + "?lgOrderId=" + str(
        orderId) + "&needImg=false"
    print(url)
    jsonobject = get_requests(url=url, headers=header, remark="简历详情查询")
    meassage = jsonobject['message']
    assert_equal("操作成功", meassage, "查看简历成功", "查看简历失败")


if __name__ == '__main__':
    orderResumes(84)
    checkOrderResumes(84)
    viewOrderResume(84)
    viewOrderResumeid(84)
