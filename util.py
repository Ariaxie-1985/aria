# coding:utf-8

import requests
import re
from requests import exceptions
from tenacity import retry, stop_after_delay, stop_after_attempt
import json

session = requests.session()

headers ={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3615.0 Safari/537.36"}

# 获取页面的token和code
@retry(stop=(stop_after_delay(2) | stop_after_attempt(3)))
def get_code_token(url):
	try:
		code = session.get(url=url, verify=False,timeout=3)
		token_values = re.findall("X_Anti_Forge_Token = '(.*?)'", code.text, re.S)[0]
		code_values = re.findall("X_Anti_Forge_Code = '(.*?)'", code.text, re.S)[0]
		headers = {"X-Anit-Forge-Code":code_values, "X-Anit-Forge-Token":token_values}
	except exceptions.Timeout as e:
		content= "该请求超时: "+url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	else:
		if code.status_code == 200:
			return headers
		else:
			content = "该请求: "+ url + " 的状态码: "+ str(code.status_code)
			wxsend("Xiawang", content)


# form表单传参的post请求
def form_post(url,data,headers):
	try:
		headers = headers
		response = session.post(url=url, data=data, headers=headers, verify=False,timeout=3)
	except exceptions.Timeout as e:
		content= "该请求超时: "+url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	else:
		if response.status_code == 200:
			return response.json()
		else:
			content = "该请求: "+ url + " 的状态码: "+ str(response.status_code)
			wxsend("Xiawang", content)


# json传参的post请求
def json_post(url,data,headers=headers):
	try:
		response = session.post(url=url, json=data, headers=headers, verify=False,timeout=3)
	except exceptions.Timeout as e:
		content= "该请求超时: "+url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	else:
		if response.status_code == 200:
			return response.json()
		else:
			content = "该请求: "+ url + " 的状态码: "+ str(response.status_code)
			wxsend("Xiawang", content)


# get请求
def get(url):
	try:
		response = session.get(url=url, verify=False,timeout=3)
	except exceptions.Timeout as e:
		content= "该请求超时: "+url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	else:
		if response.status_code == 200:
			return response
		else:
			content = "该请求: "+ url + " 的状态码: "+ str(response.status_code)
			wxsend("Xiawang", content)

# get请求
def get_header(url):
	try:
		response = session.get(url=url, verify=False,timeout=3)
	except exceptions.Timeout as e:
		content= "该请求超时: "+url + str(e)
		wxsend("Xiawang", content)
	except exceptions.HTTPError as e:
		wxsend("Xiawang", "HTTP请求错误: " + str(e))
	else:
		if response.status_code == 200:
			return response.request.headers
		else:
			content = "该请求: "+ url + " 的状态码: "+ str(response.status_code)
			wxsend("Xiawang", content)

# 企业微信报警
@retry
def wxsend(username, content):
	s = {'userids':username, 'msgtype':'text', 'content':content}
	params=json.dumps(s)
	try:
		content=requests.post('http://api.oss.lagou.com/v2/send/wechat/',data=params,timeout=3)
		if content.status_code!=200:
			raise IOError("exception")
	except  Exception as e:
		raise  IOError("exception")


