# coding:utf-8
from api_script.business.B_calling import calling
from utils.util import login
import logging
from utils.read_file import get_yaml_test_data

test_data = get_yaml_test_data('logininfo.yaml')
countrycode = test_data['countrycode']
username = test_data['username']

login(countrycode,username)

cUserid = 100012422

def test_calling():
	s = calling(cUserid)
	logging.getLogger().setLevel(logging.INFO)

	# if s['message'] == u'成功':
	try:
		assert s['message'] == '成功'
		logging.info(u'calling获取成功,虚拟号码：'+str(s['content']['data']['result']['virtualPhone']))

			# print(s['content']['data']['result']['virtualPhone'])
	except:
		logging.info(u'calling获取失败，响应信息：'+str(s))
			# print(s)

# test_calling()