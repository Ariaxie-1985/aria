# coding:utf-8
# @Time  : 2019-01-23 18:01
# @Author: Xiawang
from utils.util import get_code_token, form_post, get_requests


def settings_channel_support():
	url = "https://easy.lagou.com/settings/channel/support.json"
	header = get_code_token("https://easy.lagou.com/settings/new/channel/my_channels.htm?")
	remark = "查询当前平台支持的渠道"
	return form_post(url=url, headers=header, remark=remark)


def settings_channel_my_channels():
	'''
	已绑定渠道的接口
	:return:
	'''
	url = "https://easy.lagou.com/settings/channel/my_channels.htm"
	return get_requests(url=url)
