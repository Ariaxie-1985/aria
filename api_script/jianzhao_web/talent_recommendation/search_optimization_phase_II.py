# coding:utf-8
# @Time  : 2019-01-21 15:45
# @Author: Xiawang
import time

from utils.util import get_requests, login, form_post, get_code_token


def get_talent_index():
	'''
	找人才主页
	:return:
	'''
	url = "https://easy.lagou.com/talent/index.htm?filter=0&pageNo=1&strongly=False&notSeen=False"
	return get_requests(url=url)


def get_talent_hunting():
	'''
	获取猎头数据
	:return:
	'''
	url = "https://easy.lagou.com/talent/hunting.json?keyword=JAVA&city=北京&education=本科及以上&pageNo=1"
	return get_requests(url=url).json()


def get_talent_inspect_pageNo():
	'''
	谁看过我-分页查询
	:return:
	'''
	url = "https://easy.lagou.com/talent/inspect/pageNo.json?pageNo=1"
	return get_requests(url=url).text


def get_talent_newest_pageNo():
	'''
	最新人才
	:return:
	'''
	url = "https://easy.lagou.com/talent/newest/{}.json".format("1")
	return get_requests(url=url).json()


def get_talent_positions():
	'''
	职位列表
	:return:
	'''
	url = "https://easy.lagou.com/talent/positions.json"
	return get_requests(url=url).json()


def get_talent_rec():
	'''
	定时检查职位的推荐人才或最新人才是否有更新
	:return:
	'''
	url = "https://easy.lagou.com/talent/rec/{}.json?pageNo=1&positionld=13845256".format("1")
	return get_requests(url=url).json()


def get_talent_checkNewData():
	'''
	定时检查职位的推荐人才或最新人才是否有更新
	:return:
	'''
	url = "https://easy.lagou.com/talent/checkNewData.json"
	return get_requests(url=url).json()


def get_talent_search_list():
	'''
	单开页-人才搜索接口
	:return:
	'''
	url = "https://easy.lagou.com/talent/search/list.json?pageNo=1&orderWay=0&createTime={}&positionName=python&visible=true&searchVersion=1".format(
		int(round(time.time() * 1000)))
	r = get_requests(url=url).json()
	global cUserId, resumeFetchKey
	cUserId = r['content']['data']['page']['result'][0]['userId']
	resumeFetchKey = r['content']['data']['page']['result'][0]['resumeFetchKey']
	return r


def search_resume_fetchResume():
	'''
	人才预览
	:return:
	'''
	url = "https://easy.lagou.com/search/resume/fetchResume.json?resumeFetchKey={}".format(resumeFetchKey)
	return get_requests(url=url).json()


def get_talent_search_index():
	'''
	人才搜索落地页
	:return:
	'''
	url = "https://easy.lagou.com/talent/search/index.htm"
	return get_requests(url=url)


def get_talent_search_similar():
	'''
	获取相似人才
	:return:
	'''
	url = "https://easy.lagou.com/talent/search/similar.json"
	header = get_code_token("https://easy.lagou.com/talent/search/index.htm")
	data = {
		"cUserId": cUserId
	}
	remark = "获取相似人才"
	return form_post(url=url, data=data, headers=header, remark=remark)


def get_talent_search_deliverInfo():
	'''
	查询c端用户的投递，沟通信息
	:return:
	'''
	url = "https://easy.lagou.com/talent/search/deliverInfo.json"
	data = {
		"cUserIds": "100014476,100015378,100015183,100015193,100015188,100015178,100014967,100015008,100014962,100015003,100015196,100015201,100015186,100014867,100014648"
	}
	header = {}
	remark = "查询c端用户的投递，沟通信息"
	return form_post(url=url, data=data, headers=header, remark=remark)


def get_search_saveFilter():
	'''
	单开页-保存过滤器
	:return:
	'''
	url = "https://easy.lagou.com/search/saveFilter.json"
	data = {
		"orderWay": 0,
		"city": "不限",
		"education": "不限",
		"workYear": "不限",
		"industryField": "不限",
		"expectSalary": "不限",
		"positionName": "python",
		"searchAlias": "python"

	}
	header = {}
	remark = "保存过滤器"
	return form_post(url=url, data=data, headers=header, remark=remark)



