# coding:utf-8
# @Author: Xiawang
from api_script.entry.account.passport import password_login
from utils.util import form_post, get_code_token, login

'''
职位 - 下线 在线职位列表的第一个职位
'''


# 下线职位
def get_online_positionId():
    refer_offlinePosition_url = "https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1"
    Position_header = get_code_token(refer_offlinePosition_url)
    myonlinepostions_url = "https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json"
    myonlinepostions_data = {"pageNo": 1}
    remark = "获取下线职位的职位id"
    r = form_post(url=myonlinepostions_url, data=myonlinepostions_data, headers=Position_header, remark=remark)
    positionId = r['content']['data']['parentPositionVOs'][0]['positions'][0]['positionId']
    return positionId


def offlinePosition(positionId):
    refer_offlinePosition_url = 'https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1'
    Position_header = get_code_token(refer_offlinePosition_url)
    offlinePosition_url = "https://easy.lagou.com/position/offlinePosition.json"
    offlinePosition_data = {"positionId": positionId}
    remark = "下线职位"
    return form_post(url=offlinePosition_url, data=offlinePosition_data, headers=Position_header, remark=remark)


def online_positionId_outerPositionId():
    refer_offlinePosition_url = "https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1"
    Position_header = get_code_token(refer_offlinePosition_url)
    myonlinepostions_url = "https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json"
    myonlinepostions_data = {"pageNo": 1}
    remark = "获取下线职位的职位id"
    r = form_post(url=myonlinepostions_url, data=myonlinepostions_data, headers=Position_header, remark=remark)
    try:
        positionId = r['content']['data']['parentPositionVOs'][0]['positions'][0]['positionId']
        outerPositionId = r['content']['data']['parentPositionVOs'][0]['positions'][0]['outerPositionId']
    except KeyError:
        positionId = 0
        outerPositionId = 0
    return positionId, outerPositionId


def get_online_positions():
    refer_offlinePosition_url = "https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1"
    Position_header = get_code_token(refer_offlinePosition_url)
    myonlinepostions_url = "https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json"
    myonlinepostions_data = {"pageNo": 1}
    remark = "获取下线职位的职位id"
    r = form_post(url=myonlinepostions_url, data=myonlinepostions_data, headers=Position_header, remark=remark)
    positionIds = []
    if r['content']['data']['pageSize'] >= 10:
        for position_info in r['content']['data']['parentPositionVOs']:
            positionId = position_info['positions'][0]['positionId']
            positionIds.append(positionId)
    return positionIds


if __name__ == '__main__':
    login("0086", "19910626899")
    positionIds = get_online_positions()
    print(positionIds)
    # offlinePosition(positionId=positionId)
