# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from util.util import get_code_token, get_requests, get_header ,form_post ,login ,json_post
import json

# login('00853','05180001')

def getonlinepositionlimit():
    # 获取在线职位，发布职位限制以及当前已用数量
    s = get_requests(url='https://easy.lagou.com/position/multiChannel/getLagouPositionPrivilege.json?isSchoolJob=false',headers=get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm'),remark='获取在线职位数和上限')
    r = json.loads(s.text)
    # return s.text
    return r['content']['data']['onlinePositionNum'],r['content']['data']['onlineLimitNum'],r['content']['data']['createPositionNum'],r['content']['data']['createLimitNum']

def isprivilige():
    # 返回false为在线职位公司，返回true为特权职位
    s = form_post(remark='判断是否特权职位',url='https://easy.lagou.com/userGoodsRecord/initPriviligePositionPage.json',headers=get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm'),data={'pageNo':1,'pageSize':1})
    if s['message']=='该公司不是特权职位公司，不允许请求初始化数据':
        return False
    else:
        return True

def getpositionlimit():
    positionlimit_url = 'https://easy.lagou.com/productContract/positionLimitWarningTips.json'
    positionlimit_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    s = form_post(url=positionlimit_url,headers=positionlimit_header,data={},remark='获取特权职位限制')
    return s['content']['data']['positionLimitNum'],s['content']['data']['onlinePositionNum']

def getrefreshpoint():
    refreshpoint_url = 'https://easy.lagou.com/position/batchRefreshInfo.json'
    refreshpoint_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    s = form_post(url=refreshpoint_url,headers=refreshpoint_header,data=None,remark='获取刷新点数')
    return s['content']['data']['remainPositionPoint']

def position(a):
    # 0:社招职位，1：校招职位
    refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
    Position_header = get_code_token(refer_createPosition_url)
    createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
    createPosition_data = {'isSchoolJob': a, 'channelTypes': 'LAGOU', 'firstType': '开发|测试|运维类',
                           'positionType': '后端开发',
                           'positionThirdType': 'Python', 'positionName': 'python后端开发拉勾测试', 'department': '111',
                           'jobNature': '全职', 'salaryMin': '11', 'salaryMax': '12', 'education': '不限',
                           'positionBrightPoint': '11111',
                           'positionDesc': '<p>111111111111111111111111111111111111111111111</p>',
                           'workAddressId': '191880',
                           'labels': '[{"id":"1","name":"电商"}]', 'extraInfor': '[{"labels":[{"id":"1","name":"电商"}]}]',
                           'channels': '108', 'useEnergyCard': 'false', 'recommend': 'false', "useEnergyCard": "false",'workYear':'不限'}
    s = form_post(url=createPosition_url, data=createPosition_data, headers=Position_header,remark='发布职位')
    return s

def position_limit():
    # 发布职位直到到到上限
    id=[]
    s = position(0)
    i = 0
    while s['message'] == '操作成功':
        id.append(s['content']['data']['parentPositionInfo']['positionChannelInfoList'][0]['positionId'])
        s = position(0)

        i=i+1
    else:
        return s,i,id

def offineposition(id):
    offine_url = 'https://easy.lagou.com/position/offlinePosition.json'
    offine_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    offine_data = {'positionId':id}
    s = form_post(url=offine_url,headers=offine_header,data=offine_data,remark='下线职位')
    return s
# print(getonlinepositionlimit())