# coding:utf-8
# @Author: Xiawang
from utils.util import form_post,get_code_token, login,get_requests

'''
简历管理-候选人: 从新简历移至待沟通
'''
username = 20181205
login("00852",username)

# 移动到待沟通
refer_listofcandidates_url = "https://easy.lagou.com/can/index.htm"
listofcandidates_header = get_code_token(refer_listofcandidates_url)
newresumelist_url = "https://easy.lagou.com/can/new/list.json"
newresumelist_data = {"pageNo":1,"stage":"NEW","can":"true","needQueryAmount":"true","newDeliverTime":0}
r = form_post(newresumelist_url, newresumelist_data,listofcandidates_header)
positionId = r['content']['rows'][0]['positionId']
resumeOwnerId = r['content']['rows'][0]['id']


url = 'https://easy.lagou.com/settings/template/in_temp.json?positionId='+str(positionId)
get_requests(url,listofcandidates_header)

toStageLink_url = 'https://easy.lagou.com/can/batch/toStageLink.json'
toStageLink_data = {"resumeIds":resumeOwnerId}
form_post(toStageLink_url, toStageLink_data, listofcandidates_header)