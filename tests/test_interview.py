# coding:utf-8
# @Time  : 2019-01-23 17:37
# @Author: Xiawang
from api_script.jianzhao_web.interview.interview import interview_index, interview_list, interview_sign, \
	interview_setting_save, interview_get_code, interview_resetCode
from utils.util import assert_equal, login

login("00852", 20181205)

def test_interview_index():
	r = interview_index()
	assert_equal(200, r.status_code, "简历管理-面试日程页面成功")


def test_interview_list():
	r = interview_list()
	assert_equal(1, r['state'], "面试签到列表获取成功")


def test_interview_sign():
	r = interview_sign()
	assert_equal(200, r.status_code, "简历管理-面试日程-面试签到设置主页面成功")


def test_interview_setting_save():
	r = interview_setting_save()
	assert_equal(1, r['state'], "保存面试签到设置成功")


def test_interview_get_code():
	r = interview_get_code()
	assert_equal(1, r['state'], "获取公开码和二维码成功")


def test_interview_resetCode():
	r = interview_resetCode()
	assert_equal(1, r['state'], "重置公开链接码")