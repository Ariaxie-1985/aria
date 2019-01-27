# -*- coding: utf8 -*-
__author__ = 'yqzhang'
import time
from util.util import get_code_token, get_requests, get_header ,form_post ,login ,json_post
import logging
# login('00853','05180001')

def getrefreshpoint():
    refreshpoint_url = 'https://easy.lagou.com/position/batchRefreshInfo.json'
    refreshpoint_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    s = form_post(url=refreshpoint_url,headers=refreshpoint_header,data=None,remark='获取刷新点数')
    return s['content']['data']['remainPositionPoint']

def getpositionId():
    position_url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    position_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    s = form_post(url=position_url,headers=position_header,data={'pageNo':1},remark='获取职位id')
    return s['content']['data']['parentPositionVOs'][0]['positions'][0]['positionId']

def refrech(positionId):
    # 免费刷新后，需过一段时间才可以付费刷新，second为冷却时间，单位秒
    a = getrefreshpoint()
    refrech_url = 'https://easy.lagou.com/position/refreshPosition.json'
    refrech_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    refrech_data = {'positionId':positionId}
    r = form_post(url=refrech_url,headers=refrech_header,data=refrech_data,remark='刷新职位')
    # print('1')
    # b = getrefreshpoint()
    # print (r)
    '''
    if a==b:
        time.sleep(second)
        logging.info('需等待冷却时间结束后方可刷新，冷却时间'+str(second))
        s = form_post(url=refrech_url,headers=refrech_header,data=refrech_data,remark='刷新职位')
        # print('22')
        return s
    else:
        return r
    '''
    return r
# print(refrech()13844856)
# refrech(13845370)