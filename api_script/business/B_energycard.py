# -*- coding: utf8 -*-
__author__ = 'yqzhang'
import logging
from api_script.util import get_code_token, get, get_header ,form_post ,login ,json_post
import datetime

login('00853','05180001')
def getpositionId():
    position_url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    position_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    s = form_post(url=position_url,headers=position_header,data={'pageNo':1},remark='获取职位id')
    return s['content']['data']['parentPositionVOs'][0]['positions'][0]['positionId']

# positionId = getpositionId()
def energycard(positionId):

    energycard_url = 'https://easy.lagou.com/position/multiChannel/usePositionEnergyCard.json'
    energycard_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    energycard_data = {'positionId':positionId}
    s = form_post(url=energycard_url,headers=energycard_header,data=energycard_data,remark='赋能卡')
    return s
    # if s['message'] == u'操作成功':
    #     print ('赋能卡操作成功：',s)
    #     return s['content']['data']['info']['startTime'],s['content']['data']['info']['endTime']
    # else:
    #     print('赋能卡异常：',s)
# print (energycard(positionId))