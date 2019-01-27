# coding:utf-8
# @Author: Xiawang
from utils.util import form_post,get_code_token, login,get_requests

'''
简历管理-候选人: 从待沟通移至面试
'''

username = 20181205
login("00852",username)


refer_listofcandidates_url = "https://easy.lagou.com/can/index.htm"
listofcandidates_header = get_code_token(refer_listofcandidates_url)
newlist_url = "https://easy.lagou.com/can/new/list.json"
newlist_data = {"pageNo":0,"stage":"LINK","can":"true","needQueryAmount":"true","newDeliverTime":0}
r = form_post(newlist_url, newlist_data,listofcandidates_header)
positionId = r['content']['rows'][0]['positionId']
resumeOwnerId = r['content']['rows'][0]['id']

url = 'https://easy.lagou.com/settings/template/in_temp.json?positionId='+str(positionId)
r = get_requests(url,listofcandidates_header).json()
templateId = r['content']['rows'][0]['id']

'''
创建面试模板

create_in_temp_url = 'https://easy.lagou.com/settings/template/create_in_temp.json'
create_in_temp_data = {"linkMan":"陌生人", "address":"海置创投大厦4层","linkPhone":"18500000000","templateName":"宇琦"}
r = form_post(create_in_temp_url, create_in_temp_data, listofcandidates_header)

'''

arr_inerview_url = 'https://easy.lagou.com/can/arr_inerview.json'
arr_inerview_data = {"resumeId":resumeOwnerId,"templateId":templateId,"linkMan":"宇琦", "address":"海置创投大厦4层",
                     "linkPhone":"18500000000","templateName":"宇琦","interviewTime":1545193800000, "interviewTimeStr":"2018-12-19 12:30:00",
                     "addInfo":"欢迎来面试！", "sendNotice":1, "forwardEmails":"tester2018@sina.com"}
r = form_post(arr_inerview_url, arr_inerview_data, listofcandidates_header)

