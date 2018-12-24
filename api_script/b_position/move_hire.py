# coding:utf-8

from api_script.util import form_post,get_code_token, login,get

'''
简历管理-候选人: 从面试移至录用
'''

username = 20181205
login("00852",username)


refer_listofcandidates_url = "https://easy.lagou.com/can/index.htm"
listofcandidates_header = get_code_token(refer_listofcandidates_url)
newlist_url = "https://easy.lagou.com/can/new/list.json"
newlist_data = {"pageNo":0,"stage":"INTERVIEW","can":"true","needQueryAmount":"true","newDeliverTime":0}
r = form_post(newlist_url, newlist_data,listofcandidates_header)
positionId = r['content']['rows'][0]['positionId']
resumeOwnerId = r['content']['rows'][0]['id']

url = 'https://easy.lagou.com/settings/template/in_temp.json?positionId='+str(positionId)
get(url,listofcandidates_header)


toStageOffer_url = 'https://easy.lagou.com/can/batch/toStageOffer.json'
toStageOffer_data = {"resumeIds":resumeOwnerId}
r = form_post(toStageOffer_url, toStageOffer_data, listofcandidates_header)

