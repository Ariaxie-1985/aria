# coding:utf-8

from utils.util import get_code_token, form_post, get_requests
import json

hunter_url = 'https://hunter.lagou.com/api/mock/login/325485'
hunter_html = 'https://hunter.lagou.com/'
get_requests(hunter_url)

userIdNamePhoneEmail = str(13220178923)
search_url = 'https://hunter.lagou.com/api/position/discover/allUsers?userIdNamePhoneEmail='+userIdNamePhoneEmail+'&sex=9&resumeFrom=110&namedBrand=0&query.limit=20&query.offset=0'
s=get_requests(search_url)
a=s.content
sdic = json.loads(a)
b = sdic['data']['data']
c = b[0]


userid = c['userId']
refId = c['refId']
add_url = 'https://hunter.lagou.com/api/position/manager/moveToWaitForChat.json'
# add_html = 'https://hunter.lagou.com/'
# add_header = get_code_token(add_html)
add_header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3615.0 Safari/537.36"}
add_data = {'paiCandidate':'false','candidateId':userid,'refId':refId,'fromSource':'LAGOU','resumeClassify':''}
form_post(url=add_url,headers=add_header,data=add_data,remark='加入人才库')
