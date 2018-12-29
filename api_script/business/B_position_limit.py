# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from util.util import get_code_token, get, get_header ,form_post ,login ,json_post

login('00853','05180001')

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
    s = position(0)
    i = 0
    while s['message'] == '操作成功':
        s = position(0)
        i=i+1
    else:
        return s,i


print(position_limit())