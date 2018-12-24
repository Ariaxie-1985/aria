# coding:utf-8

import requests
import re
from requests import exceptions
from tenacity import *
import json

session = requests.session()

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

# 获取页面的token和code
@retry(stop=(stop_after_delay(2) | stop_after_attempt(3)))
def get_code_token(url):
	try:
		code = session.get(url=url, headers=header,verify=False,timeout=3)
		token_values = re.findall("X_Anti_Forge_Token = '(.*?)'", code.text, re.S)[0]
		code_values = re.findall("X_Anti_Forge_Code = '(.*?)'", code.text, re.S)[0]
		headers= {"X-Anit-Forge-Code":code_values, "X-Anit-Forge-Token":token_values, "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3615.0 Safari/537.36"}
	except exceptions.Timeout as e:
		content= "该请求超时: "+url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	except Exception as e:
		wxsend("Xiawang", "该请求: "+url+" 重试后依然有异常: " + str(e))
	else:
		if code.status_code == 200:
			return headers

		else:
			content = "该请求: "+ url + " 的状态码: "+ str(code.status_code)
			wxsend("Xiawang", content)


# form表单传参的post请求
def form_post(url,data=None,headers=None):
	try:
		headers = {**headers, **header}
		response = session.post(url=url, data=data, headers=headers, verify=False,timeout=3)
	except exceptions.Timeout as e:
		content= "该请求超时: "+url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	except Exception as e:
		wxsend("Xiawang", "该请求: "+url+" 重试后依然有异常: " + str(e))
	else:
		if response.status_code == 200:
			return response.json()
		else:
			content = "该请求: "+ url + " 的状态码: "+ str(response.status_code)
			wxsend("Xiawang", content)


# json传参的post请求
def json_post(url,data=None,headers=None):
	try:
		headers = {**headers, **header}
		response = session.post(url=url, json=data, headers=headers, verify=False,timeout=3)
	except exceptions.Timeout as e:
		content= "该请求超时: "+url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	except Exception as e:
		wxsend("Xiawang", "该请求: "+url+" 重试后依然有异常: " + str(e))
	else:
		if response.status_code == 200:
			return response.json()
		else:
			content = "该请求: "+ url + " 的状态码: "+ str(response.status_code)
			wxsend("Xiawang", content)


# get请求
def get(url,headers=None):
	try:
		response = session.get(url=url, headers=headers, verify=False,timeout=3)
	except exceptions.Timeout as e:
		content= "该请求超时: "+url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	except Exception as e:
		wxsend("Xiawang", "该请求: "+url+" 重试后依然有异常: " + str(e))
	else:
		if response.status_code == 200:
			return response
		else:
			content = "该请求: "+ url + " 的状态码: "+ str(response.status_code)
			wxsend("Xiawang", content)

# get请求
def get_header(url):
	try:
		response = session.get(url=url, headers=header, verify=False,timeout=3)
	except exceptions.Timeout as e:
		content= "该请求超时: "+url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	except Exception as e:
		wxsend("Xiawang", "该请求: "+url+" 重试后依然有异常: " + str(e))
	else:
		if response.status_code == 200:
			return response.request.headers
		else:
			content = "该请求: "+ url + " 的状态码: "+ str(response.status_code)
			wxsend("Xiawang", content)

# 企业微信报警
@retry
def wxsend(username,content):
	s = {'userids':username, 'msgtype':'text', 'content':content}
	params=json.dumps(s)
	try:
		content=requests.post('http://api.oss.lagou.com/v2/send/wechat/',data=params,timeout=3)
		if content.status_code!=200:
			raise IOError("exception")
	except  Exception as e:
		raise  IOError("exception")


def login(countryCode,username):
	'''
	从www.lagou.com登录，验证码登录
	:param countryCode: str, 地区编号
	:param username: str, 用户名
	'''
	login_url = 'https://passport.lagou.com/login/login.json'
	login_data = {'isValidate': 'true', 'username': username, 'phoneVerificationCode': '049281',
	              'countryCode': countryCode,'challenge': 111}
	referer_login_html = 'https://www.lagou.com/frontLogin.do'
	login_header = get_code_token(referer_login_html)
	form_post(url=login_url, data=login_data, headers=login_header)

def login_home(username, password):
	'''
	从home.lagou.com登录，密码登录
	:param username: str, 用户名
	:param password: str, 密码
	'''
	referer_login_home_url = "https://home.lagou.com/"
	login_url = 'https://passport.lagou.com/login/login.json'
	login_data = {'isValidate': 'true', 'username': username, 'password':password}
	login_home_header = get_code_token(referer_login_home_url)
	form_post(url=login_url, data=login_data, headers=login_home_header)

