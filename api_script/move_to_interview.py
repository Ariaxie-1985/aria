# coding:utf-8

from util import form_post,get_code_token, login,get

username = 20181205
login("00852",username)

# 移动到待沟通
refer_listofcandidates_url = "https://easy.lagou.com/can/index.htm"
listofcandidates_header = get_code_token(refer_listofcandidates_url)
newlist_url = "https://easy.lagou.com/can/new/list.json"
newlist_data = {"pageNo":0,"stage":"LINK","can":"true","needQueryAmount":"true","newDeliverTime":0}
r = form_post(newlist_url, newlist_data,listofcandidates_header)
positionId = r['content']['rows'][0]['positionId']
resumeOwnerId = r['content']['rows'][0]['resumeOwnerId']

url = 'https://easy.lagou.com/settings/template/in_temp.json?positionId='+str(positionId)
get(url,listofcandidates_header)

create_in_temp_url = 'https://easy.lagou.com/settings/template/create_in_temp.json'
create_in_temp_data = {"linkMan":"陌生人", "address":"海置创投大厦4层","linkPhone":"18500000000","templateName":"宇琦"}
r = form_post(create_in_temp_url, create_in_temp_data, listofcandidates_header)
templateId = r['content']['data']['template']['id']

arr_inerview_url = 'https://easy.lagou.com/can/arr_inerview.json'
arr_inerview_data = {"resumeId":resumeOwnerId,"templateId":templateId,"linkMan":"陌生人", "address":"海置创投大厦4层",
                       "linkPhone":"18500000000","templateName":"宇琦","interviewTime":1546511580000, "interviewTimeStr":"2019-01-03 18:33:00",
                       "addInfo":"欢迎来面试！", "sendNotice":1, "forwardEmails":"tester2018@sina.com"}
r = form_post(arr_inerview_url, arr_inerview_data, listofcandidates_header)
print(r)

