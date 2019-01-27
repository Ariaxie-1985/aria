# coding:utf-8
# @Time  : 2019-01-23 18:24
# @Author: Xiawang
from api_script.jianzhao_web.resume_manage.resume_clean import can_new_index, can_new_clean
from utils.util import assert_equal, login

login("00852", 20181205)


def test_can_new_index():
	r = can_new_index()
	assert_equal(200, r.status_code, "候选人首页获取成功")


def test_can_new_clean():
	r = can_new_clean()
	assert_equal(1, r['state'], "清理30天内的新简历成功")
