# coding:utf-8
from api_script.business.B_calling import calling
from api_script.util import login
import logging

login('00852','20181205')
cUserid = 100012422

def test_calling():
	s = calling(cUserid)
	logging.getLogger().setLevel(logging.INFO)

	if s['message'] == u'成功':
		logging.info(u'calling获取成功,虚拟号码：'+str(s['content']['data']['result']['virtualPhone']))
		assert s['message'] == '成功'
			# print(s['content']['data']['result']['virtualPhone'])
	else:
		logging.info(u'calling获取失败，响应信息：'+str(s))
			# print(s)

# test_calling()