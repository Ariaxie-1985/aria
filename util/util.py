# coding:utf-8

import requests
import re
from requests import exceptions
from tenacity import *
import json
import logging

logging.getLogger().setLevel(logging.INFO)

requests.packages.urllib3.disable_warnings()
session = requests.session()

header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


# 获取页面的token和code
@retry(stop=(stop_after_delay(2) | stop_after_attempt(3)))
def get_code_token(url):
	try:
		code = session.get(url=url, headers=header, verify=False, timeout=3)
		token_values = re.findall("X_Anti_Forge_Token = '(.*?)'", code.text, re.S)[0]
		code_values = re.findall("X_Anti_Forge_Code = '(.*?)'", code.text, re.S)[0]
		headers = {"X-Anit-Forge-Code": code_values, "X-Anit-Forge-Token": token_values,
		           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3615.0 Safari/537.36"}
		if code.status_code == 200:
			return headers
	except exceptions.Timeout as e:
		content = "该请求超时: " + url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	except Exception as e:
		wxsend("Xiawang", "该请求: " + url + " 重试后依然有异常: " + str(e))


def form_post(url, remark, data=None, headers=None):
	"""
	form表单传参的post请求
	:param url: 请求url
	:param remark: str, 备注
	:param data: dict, 请求数据
	:param headers: dict, 请求header
	:return: json格式化的响应结果
	"""
	try:
		headers = {**headers, **header}
		response = session.post(url=url, data=data, headers=headers, verify=False, timeout=3)
		logging.info(
			"\n请求目的: {},\n 请求url: {},\n 请求数据: {},\n 响应结果: {}\n".format(remark, url, data, str(response.json())))
		if response.status_code == 200:
			return response.json()
		else:
			content = "该请求: " + url + " 的状态码: " + str(response.status_code)
			wxsend("Xiawang", content)
	except exceptions.Timeout as e:
		content = "该请求超时: " + url + str(e)
		logging.ERROR("异常日志: " + content)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		logging.ERROR("异常日志: " + "HTTP请求错误: " + str(e))
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	except Exception as e:
		logging.ERROR("异常日志: " + "该请求: " + url + " 重试后依然有异常: " + str(e))
		wxsend("Xiawang", "该请求: " + url + " 重试后依然有异常: " + str(e))


def json_post(url, remark, data=None, headers=None):
	"""
	json传参的post请求
	:param url: 请求url
	:param remark: str, 备注
	:param data: dict, 请求数据
	:param headers: dict, 请求header
	:return: json格式化的响应结果
	"""
	try:
		headers = {**headers, **header}
		response = session.post(url=url, json=data, headers=headers, verify=False, timeout=3)
		logging.info(
			"\n请求目的: {},\n 请求url: {},\n 请求数据: {},\n 响应结果: {}\n".format(remark, url, data, str(response.json())))
		if response.status_code == 200:
			return response.json()
		else:
			content = "该请求: " + url + " 的状态码: " + str(response.status_code)
			wxsend("Xiawang", content)
	except exceptions.Timeout as e:
		content = "该请求超时: " + url + str(e)
		wxsend("Xiawang", content)
		logging.ERROR("异常日志: " + content)
	except exceptions.HTTPError as e:
		logging.ERROR("异常日志: " + "HTTP请求错误: " + str(e))
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	except Exception as e:
		logging.ERROR("异常日志: " + "该请求: " + url + " 重试后依然有异常: " + str(e))
		wxsend("Xiawang", "该请求: " + url + " 重试后依然有异常: " + str(e))


def get_requests(url, headers=None, remark=None):
	"""
	get请求
	:param url: str, 接口地址
	:param remark: str, 备注
	:param headers: dict, requests header
	:return: object, 响应对象
	"""
	try:
		response = session.get(url=url, headers=headers, verify=False, timeout=3)
		if "application/json" in response.headers['content-type']:
			logging.info(
				"\n请求目的: {},\n 请求url: {},\n 响应结果: {}\n".format(remark, url, str(response.json())))
		else:
			logging.info(
				"\n请求目的: {},\n 请求url: {}".format(remark, url))

		if response.status_code == 200 or response.status_code == 302:
			return response
		else:
			content = "该请求: " + url + " 的状态码: " + str(response.status_code)
			logging.ERROR("异常日志: " + content)
			wxsend("Xiawang", content)
	except exceptions.Timeout as e:

		content = "该请求超时: " + url + str(e)
		logging.ERROR("异常日志: " + content)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
		logging.ERROR("异常日志: " + "HTTP请求错误: " + str(e))
	except Exception as e:
		wxsend("Xiawang", "该请求: " + url + " 重试后依然有异常: " + str(e))
		logging.ERROR("异常日志: " + "该请求: " + url + " 重试后依然有异常: " + str(e))


# get请求---获取header
def get_header(url):
	try:
		response = session.get(url=url, headers=header, verify=False, timeout=3)
	except exceptions.Timeout as e:
		content = "该请求超时: " + url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	except Exception as e:
		wxsend("Xiawang", "该请求: " + url + " 重试后依然有异常: " + str(e))
	else:
		if response.status_code == 200:
			return response.request.headers
		else:
			content = "该请求: " + url + " 的状态码: " + str(response.status_code)
			logging.ERROR("异常日志: " + content)
			wxsend("Xiawang", content)


# 企业微信报警
@retry
def wxsend(username, content):
	s = {'userids': username, 'msgtype': 'text', 'content': content}
	params = json.dumps(s)
	try:
		content = requests.post('http://api.oss.lagou.com/v2/send/wechat/', data=params, timeout=3)
		if content.status_code != 200:
			raise IOError("exception")
	except  Exception as e:
		raise IOError("exception")


def login(countryCode, username):
	'''
	从www.lagou.com登录，验证码登录
	:param countryCode: str, 地区编号
	:param username: str, 用户名
	'''
	session.cookies.clear()
	login_url = 'https://passport.lagou.com/login/login.json'
	login_data = {'isValidate': 'true', 'username': username, 'phoneVerificationCode': '049281',
	              'countryCode': countryCode, 'challenge': 111}
	referer_login_html = 'https://www.lagou.com/frontLogin.do'
	login_header = get_code_token(referer_login_html)
	remark = str(username) + "在登录拉勾"
	r = form_post(url=login_url, data=login_data, headers=login_header, remark=remark)
	if r['message'] == "操作成功":
		logging.info("用户名: " + str(username) + " 登录成功")
	return r


def login_home(username, password):
	'''
	从home.lagou.com登录，密码登录
	:param username: str, 用户名
	:param password: str, 密码
	:param remark: str, 备注
	'''
	session.cookies.clear()
	referer_login_home_url = "https://home.lagou.com/"
	login_url = 'https://passport.lagou.com/login/login.json'
	login_data = {'isValidate': 'true', 'username': username, 'password': password}
	login_home_header = get_code_token(referer_login_home_url)
	remark = "用户 " + str(username) + " 在登录拉勾home后台"
	r = form_post(url=login_url, data=login_data, headers=login_home_header, remark=remark)
	if r['message'] == "操作成功":
		logging.info("用户名: " + str(username) + " 登录成功")
	return r


def assert_equal(expectvalue, actualvalue, success_message, fail_message=None):
	'''
	断言两个值是否相等, 并对结果打印日志
	:param expectvalue: 期望结果
	:param actualvalue: 实际结果
	:param success_message: str, 断言成功打印的日志
	:param fail_message:str, 断言失败打印的日志
	'''
	assert expectvalue == actualvalue
	if expectvalue == actualvalue:
		logging.info(success_message)
	else:
		logging.error(fail_message)


# 获取url的html源码
def gethtml(url):
	'''

	:param url:
	:return:
	'''
	html = session.get(url)
	return html.text


def wait(time):
	'''
	设置等待时间
	:param time:
	:return:
	'''


def get_app_header(userId):
	header = {"X-L-REQ-HEADER": {"deviceType": 10}, "X-L-USER-ID": str(userId)}
	header["X-L-REQ-HEADER"] = json.dumps(header["X-L-REQ-HEADER"])
	return header


def json_put(url, remark, data=None, headers=None):
	"""
	json传参的put请求
	:param url: 请求url
	:param remark: str, 备注
	:param data: dict, 请求数据
	:param headers: dict, 请求header
	:return: json格式化的响应结果
	"""
	try:
		headers = {**headers, **header}
		response = session.put(url=url, json=data, headers=headers, verify=False, timeout=3)
		logging.info(
			"\n请求目的: {},\n 请求url: {},\n 请求数据: {},\n 响应结果: {}\n".format(remark, url, data, str(response.json())))
		if response.status_code == 200:
			return response.json()
		else:
			content = "该请求: " + url + " 的状态码: " + str(response.status_code)
			wxsend("Xiawang", content)
	except exceptions.Timeout as e:
		content = "该请求超时: " + url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		("Xiawang", "HTTP请求错误: " + str(e))
	except Exception as e:
		wxsend("Xiawang", "该请求: " + url + " 重试后依然有异常: " + str(e))


def put_requests(url, headers=None, remark=None):
	"""
	put请求
	:param url: str, 接口地址
	:param remark: str, 备注
	:param headers: dict, requests header
	:return: object, 响应对象
	"""
	try:
		response = session.put(url=url, headers=headers, verify=False, timeout=3)
		if "application/json" in response.headers['content-type']:
			logging.info(
				"\n请求目的: {},\n 请求url: {},\n 响应结果: {}\n".format(remark, url, str(response.json())))
		else:
			logging.info(
				"\n请求目的: {},\n 请求url: {}".format(remark, url))

		if response.status_code == 200 or response.status_code == 302:
			return response
		else:
			content = "该请求: " + url + " 的状态码: " + str(response.status_code)
			logging.ERROR("异常日志: " + content)
			wxsend("Xiawang", content)
	except exceptions.Timeout as e:

		content = "该请求超时: " + url + str(e)
		logging.ERROR("异常日志: " + content)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
		logging.ERROR("异常日志: " + "HTTP请求错误: " + str(e))
	except Exception as e:
		wxsend("Xiawang", "该请求: " + url + " 重试后依然有异常: " + str(e))
		logging.ERROR("异常日志: " + "该请求: " + url + " 重试后依然有异常: " + str(e))


