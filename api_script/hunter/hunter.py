# coding:utf-8

from util.util import get_code_token, form_post, get
import json

hunter_url = 'https://hunter.lagou.com/api/mock/login/325485'
hunter_html = 'https://hunter.lagou.com/'
get(hunter_url)

userIdNamePhoneEmail = str(13220178923)
search_url = 'https://hunter.lagou.com/api/position/discover/allUsers?userIdNamePhoneEmail='+userIdNamePhoneEmail+'&sex=9&resumeFrom=110&namedBrand=0&query.limit=20&query.offset=0'
s=get(search_url)
a=s.content
sdic = json.loads(a)
b = sdic['data']['data']
c = b[0]


userid = c['userId']
refId = c['refId']
add_url = 'https://hunter.lagou.com/api/position/manager/moveToWaitForChat.json'
add_html = 'https://hunter.lagou.com/talent/search'
add_header = get_code_token(add_html)
add_data = {'paiCandidate':'false','candidateId':userid,'refId':refId,'fromSource':'LAGOU'}
form_post(url=add_url,headers=add_header,data=add_data)
