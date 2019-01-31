# coding:utf-8
# @Time  : 2019-01-23 18:15
# @Author: Xiawang
from api_script.jianzhao_web.open_channel.open_channel import settings_channel_support, settings_channel_my_channels
from utils.util import assert_equal, login

login("00852", 20181205)


def test_settings_channel_support():
	r = settings_channel_support()
	assert_equal(1, r['state'], "查询当前平台支持的渠道成功")


def test_settings_channel_my_channels():
	r = settings_channel_my_channels()
	assert_equal(200, r.status_code, "已绑定渠道返回成功")
