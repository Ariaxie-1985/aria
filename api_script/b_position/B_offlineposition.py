# coding:utf-8

from util.util import form_post,get_code_token, login

'''
职位 - 下线 在线职位列表的第一个职位
'''

username = 20181205
login("00852",username)

# 下线职位
refer_offlinePosition_url = "https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1"
Position_header = get_code_token(refer_offlinePosition_url)
myonlinepostions_url = "https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json"
myonlinepostions_data = {"pageNo":1}
remark = "获取下线职位的职位id"
r = form_post(url=myonlinepostions_url, data=myonlinepostions_data,headers=Position_header,remark=remark)
positionId = r['content']['data']['parentPositionVOs'][0]['positions'][0]['positionId']

Position_header = get_code_token(refer_offlinePosition_url)
offlinePosition_url = "https://easy.lagou.com/position/offlinePosition.json"
offlinePosition_data = {"positionId":positionId}
remark = "下线职位"
form_post(url=offlinePosition_url, data=offlinePosition_data,headers=Position_header,remark=remark)
