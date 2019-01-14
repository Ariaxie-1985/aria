# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from util.util import get_code_token, form_post, get_header ,login,get_requests
import math
import json
def getpositionidfromcompanyid(companyId):
    page = 1
    positioblist=[]
    url = 'https://www.lagou.com/gongsi/searchPosition.json'
    header = get_code_token('https://www.lagou.com/gongsi.html')
    data = {'companyId':companyId,'positionFirstType':'全部','schoolJob':'false','pageNo':page,'pageSize':10}
    s = form_post(url=url,data=data,headers=header,remark='获取该公司下所有职位')
    position=s['content']['data']['hrInfoMap']
    total=s['content']['data']['page']['totalCount']
    i = math.ceil(int(total)/10)
    while i-1 > 0:
        page = page+1
        data = {'companyId':companyId,'positionFirstType':'全部','schoolJob':'false','pageNo':page,'pageSize':10}
        r = form_post(url=url,data=data,headers=header,remark='获取该公司下所有职位')
        position1=r['content']['data']['hrInfoMap']
        position=dict(position ,**position1)
        i = i-1
    for key in position:
        # print (key)
        positioblist.append(key)
    return(positioblist)

def get_resumeId(x):
    # 0:附件简历，1：在线简历
    header_url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
    url='https://www.lagou.com/mycenter/resume/getAllResumes.json'
    get_header(header_url)
    t=get_requests(url)
    js = t.content
    jsdic = json.loads(js)
    a= jsdic['content'][0]
    b= jsdic['content'][1]
    if a['type']==x:
        return a['id']
    elif b['type']==x:
        return b['id']

def batch_sendresume(resumeid,positionlist):
    # resumeId = get_resumeId(1)

    for i in positionlist:
        sendResume_html = 'https://www.lagou.com/jobs/' + str(i) + '.html'
        sendResume_url = 'https://www.lagou.com/mycenterDelay/deliverResumeBeforce.json'
        sendResume_header = get_code_token(sendResume_html)
        sendResume_data = {'positionId': i, 'type': 1, 'resumeId': resumeid, 'force': 'true'}
        form_post(url=sendResume_url, headers=sendResume_header, data=sendResume_data,remark='发简历')
login('0086','18211111111')
batch_sendresume(get_resumeId(1),getpositionidfromcompanyid(142128))