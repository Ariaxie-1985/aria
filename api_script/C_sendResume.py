# coding:utf-8
from util import get_code_token, get, get_header ,form_post ,login 
import json

def get_resumeId(x):
 	header_url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
	url='https://www.lagou.com/mycenter/resume/getAllResumes.json'
	get_header(header_url)
	t=get(url)
	js = t.content
	jsdic = json.loads(js)
	a= jsdic['content'][0]
	b= jsdic['content'][1]
	if a['type']==x:
		return a['id']
	elif b['type']==x:
		return b['id']

login('00853','12140007')

positionId = 5375250
'''
0:附件简历，1：在线简历
'''
resumeId = get_resumeId(0)    
url='https://passport.lagou.com/grantServiceTicket/grant.html'
get_header(url)
sendResume_html = 'https://www.lagou.com/jobs/'+str(positionId)+'.html'
sendResume_url = 'https://www.lagou.com/mycenterDelay/deliverResumeBeforce.json'
sendResume_header = get_code_token(sendResume_html)
sendResume_data = {'positionId':positionId,'type':1,'resumeId':resumeId,'force':'true'}
form_post(url=sendResume_url,headers=sendResume_header,data=sendResume_data)

