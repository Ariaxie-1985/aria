# coding:utf-8
# @Time  : 2019-01-22 16:41
# @Author: Xiawang
from api_script.jianzhao_web.talent_recommendation.search_optimization_phase_II import get_talent_index, \
	get_talent_hunting, get_talent_search_list, search_resume_fetchResume, get_talent_search_index, \
	get_talent_search_similar, get_talent_search_deliverInfo, get_search_saveFilter, get_talent_search_list_html
from utils.util import login, assert_equal

def setup_module(module):
	pass

def teardown_module(module):
	pass



def test_get_talent_index(login_web_k8s_default):
	r = get_talent_index()
	assert_equal(200, r.status_code, "获取找人才主页成功")


def test_get_talent_hunting():
	r = get_talent_hunting()
	assert_equal(1, r['state'], "获取猎头数据成功")


def test_get_talent_search_list_html():
	r = get_talent_search_list_html()
	assert_equal(200, r.status_code, "获取人才搜索主页成功")



def test_get_talent_search_list():
	r = get_talent_search_list()
	global cUserId, resumeFetchKey
	cUserId = r['content']['data']['page']['result'][0]['userId']
	resumeFetchKey = r['content']['data']['page']['result'][0]['resumeFetchKey']
	assert_equal(1, r['state'], "单开页-人才搜索成功")


def test_search_resume_fetchResume():
	r = search_resume_fetchResume(resumeFetchKey)
	assert_equal(1, r['state'], "人才预览成功")


def test_get_talent_search_index():
	r = get_talent_search_index()
	assert_equal(200, r.status_code, "人才搜索落地页成功")


def test_get_talent_search_similar():
	r = get_talent_search_similar(cUserId)
	assert_equal(1, r['state'], "获取相似人才成功")


def test_get_talent_search_deliverInfo():
	r = get_talent_search_deliverInfo()
	assert_equal(1, r['state'], "查询c端用户的投递，沟通信息成功")


def test_get_search_saveFilter():
	r = get_search_saveFilter()
	assert_equal(1, r['state'], "单开页-保存过滤器成功")
