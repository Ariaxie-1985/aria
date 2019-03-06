# coding:utf-8
from utils.util import get_code_token, get_requests, get_header ,form_post ,login ,json_post


# login('00852','20181205')

# rf_url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
# get_header(rf_url)
cUserid = 80

def calling(cUserid):
	calling_url = 'https://easy.lagou.com/phonecall/getVirtualNum.json'
	calling_header = get_code_token('https://easy.lagou.com/talent/index.htm')
	calling_data = {'cUserId':cUserid}
	s = form_post(url=calling_url,headers=calling_header,data=calling_data,remark=u'直call大咖')
	# if s['message'] == u'成功':
	# print (u'virtualPhone:' ,s['content']['data']['result']['virtualPhone'])
	return s

# print(calling(cUserid))