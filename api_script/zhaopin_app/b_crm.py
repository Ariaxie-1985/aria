# coding:utf-8
# @Time  : 2019-01-17 11:43
# @Author: Xiawang
from utils.util import get_app_header, json_post

host = "https://gate.lagou.com/v1/zhaopin"
headers = get_app_header(84)


def crm_positions_tag_report(type):
	'''
	:param type: str,
	消息类型： POSITION_REFRESH_POINT_NEW_MESSAGE购买职位刷新数
	POSITION_ENERGY_CARD_MESSAGE表示购买职位赋能卡 = ['CONTRACT_WARING_MESSAGE', 'RENEWAL_CONSTRACT_MESSAGE', 'POSITION_WARING_MESSAGE',
												   'CONTACT_SALES_MANAGER', 'POSITION_REFRESH_POINT_MESSAGE', 'POSITION_ENERGY_CARD_MESSAGE',
												   'POSITION_REFRESH_POINT_NEW_MESSAGE']
	:return:
	'''
	url = host + "/crm/crm_report"
	data = {
		"type": type
	}
	remark = "crm上报销售线索"
	return json_post(url=url, headers=headers, data=data, remark=remark)
