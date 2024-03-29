# coding:utf-8
from utils.util import get_code_token, get_requests, get_header, form_post, login
import json


def get_resumeId(x):
    header_url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
    url = 'https://www.lagou.com/mycenter/resume/getAllResumes.json'
    get_header(header_url)
    t = get_requests(url)
    js = t.content
    jsdic = json.loads(js)
    a = jsdic['content'][0]
    b = jsdic['content'][1]
    if a['type'] == x:
        return a['id']
    elif b['type'] == x:
        return b['id']


'''
login('00853', '12140007')

# positionId = 5375250
positionId = 5375318
0:附件简历，1：在线简历


resumeId = get_resumeId(0)
url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
get_header(url)
sendResume_html = 'https://www.lagou.com/jobs/' + str(positionId) + '.html'
sendResume_url = 'https://www.lagou.com/mycenterDelay/deliverResumeBeforce.json'
sendResume_header = get_code_token(sendResume_html)
sendResume_data = {'positionId': positionId, 'type': 1, 'resumeId': resumeId, 'force': 'true'}
r = form_post(url=sendResume_url, headers=sendResume_header, data=sendResume_data, remark='发简历')
print(r)

'''


def sendResume(positionId):
    resumeId = get_resumeId(0)
    url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
    get_header(url)
    sendResume_html = 'https://www.lagou.com/jobs/{}.html'.format(positionId)
    sendResume_url = 'https://www.lagou.com/mycenterDelay/deliverResumeBeforce.json'
    sendResume_header = get_code_token(sendResume_html)
    sendResume_data = {'positionId': str(positionId), 'type': 1, 'resumeId': resumeId, 'force': 'true'}
    return form_post(url=sendResume_url, headers=sendResume_header, data=sendResume_data, remark='发简历')

# login('00853', '12140007')
# sendResume(13847174)
