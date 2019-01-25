# coding:utf-8
# @Time  : 2019-01-14 14:41
# @Author: Xiawang

from util.util import get_app_header, get_requests, json_post, json_put

host = "https://gate.lagou.com/v1/zhaopin"
headers = get_app_header(100014641)


def positions_static_info():
	url = host + "/positions/static_info"
	remark = "查看职位详情"
	return get_requests(url=url, headers=headers, remark=remark).json()


def category_mapping(positionName):
	'''
	职位名称映射职位分类
	:param positionName: str, 职位名称
	:return:
	'''
	url = host + "/positions/category_mapping?positionName=" + positionName
	remark = "职位名称映射职位分类"
	return get_requests(url=url, headers=headers, remark=remark).json()


def positions_tag_report(firstCateGory, secCategory, tagName):
	url = host + "/positions/tag_report"
	data = {
		"secCategory": secCategory,
		"firstCateGory": firstCateGory,
		"tagName": tagName
	}
	remark = "职位标签上报"
	return json_post(url=url, headers=headers, data=data, remark=remark)


def publish_position_check():
	'''
	发布职位前校验
	:return:
	'''
	url = host + "/positions/publish_position_check"
	remark = "发布职位前校验"
	return get_requests(url=url, headers=headers, remark=remark).json()


def post_positions(firstType, positionType, positionThirdType, positionName):
	'''
	发布职位
	:return:
	'''
	url = host + "/positions/publish"
	data = {
		"isConfirm": True,
		"recommend": True,
		"labels": [{
			"name": "旅游",
			"id": 9
		}, {
			"name": "本地生活",
			"id": 5
		}],
		"positionType": positionType,
		"positionDesc": "<p>11111111111111111111111111111</p>",
		"workYear": "3-5年",
		"salaryMin": 20,
		"firstType": firstType,
		"positionName": positionName,
		"positionBrightPoint": "20薪",
		"positionThirdType": positionThirdType,
		"jobNature": "全职",
		"education": "本科",
		# "workAddressId": 191880,
		"workAddressId": 191882,
		"department": "技术部",
		"salaryMax": 30
	}
	remark = "发布职位"
	return json_post(url=url, headers=headers, data=data, remark=remark)


def positions_details(positionId):
	'''
	查看职位详情
	:param positionId: int
	:return:
	'''
	url = host + "/positions/" + positionId + "/details"
	remark = "查看职位详情"
	return get_requests(url=url, headers=headers, remark=remark).json()


def update_position(positionId):
	'''
	编辑职位
	:param positionId:
	:return:
	'''
	url = host + "/positions/update"
	data = {
		"education": "本科",
		"positionId": positionId,
		"workAddressId": 191880,
		"jobNature": "全职",
		"positionDesc": "22222222222222222222",
		"workYear": "3-5年",
		"department": "技术工程部",
		"positionBrightPoint": "50薪",
		"salaryMin": 25,
		"labels": [{
			"name": "旅游",
			"id": 9
		}, {
			"name": "本地生活",
			"id": 5
		}],
		"salaryMax": 30
	}
	remark = "发布职位"
	return json_put(url=url, headers=headers, data=data, remark=remark)


def get_online_positions():
	'''
	获取在线职位列表
	:return:
	'''
	url = host + "/positions/online/pages?pageNo=1&pageSize=20"
	remark = "获取在线职位列表"
	return get_requests(url=url, headers=headers, remark=remark).json()


def get_offline_positions():
	url = host + "/positions/offline/pages"
	remark = "获取已下线列表"
	return get_requests(url=url, headers=headers, remark=remark).json()


def get_other_positions():
	url = host + "/positions/company/other/pages"
	remark = "获取其他职位列表"
	return get_requests(url=url, headers=headers, remark=remark).json()


def refresh_position(positionId):
	url = host + "/positions/" + positionId + "/refresh_position"
	data = {
		"isConfirm": False
	}
	remark = "刷新职位"
	return json_put(url=url, data=data, headers=headers, remark=remark)


def up_position_ranking(positionId):
	url = host + "/positions/" + positionId + "/up_position_ranking"
	data = {
		"isConfirm": False
	}
	remark = "提升职位排名"
	return json_put(url=url, data=data, headers=headers, remark=remark)


def positions_top_check(positionId):
	url = host + "/positions/top/" + positionId + "/check"
	remark = "职位置顶卡校验信息"
	return get_requests(url=url, headers=headers, remark=remark).json()


def apply_privilege_position(userId):
	'''
	Args:
	userId: int, 没有被分特权职位的有子账号的分账号的userId
	:return:
	'''
	url = host + "/positions/apply_privilege_position"
	headers = get_app_header(userId)
	remark = "申请特权职位权益"
	return get_requests(url=url, headers=headers, remark=remark).json()


def positions_is_hot(positionName):
	url = host + "/positions/is_hot?positionName=" + positionName
	remark = "是否热门职位"
	return json_post(url=url, headers=headers, remark=remark)


def positions_invite(positionId, userId):
	'''
	批量邀约候选人
	:param positionId: int, 职位id
	:param userId: list, 候选人的userId
	:return:
	'''
	url = host + "/positions/invite"
	data = {
		"positionId": positionId,
		"userIds": [userId]
	}
	remark = "批量邀约候选人"
	return json_post(url=url, data=data, headers=headers, remark=remark)


def positions_recommend(positionId):
	'''
	职位推荐
	:param positionId: int, 职位id
	:return:
	'''
	url = host + "/positions/recommend?positionId="+positionId
	remark = "获取职位推荐"
	return json_post(url=url, headers=headers, remark=remark)


def positions_red_point_hint():
	url = host + "/positions/red_point_hint"
	remark = "首页导航职位红点"
	return get_requests(url=url, remark=remark, headers=headers).json()

def positions_details_app(positionId):
	url = host + '/positions/'+positionId+'/details/app'
	remark = '获取职位详情新'
	return get_requests(url=url,remark=remark,headers=headers)

def positions_query_position_type():
	url = host + '/positions/query_position_type'
	remark = '查询可选择的职位分类'
	return get_requests(url=url,remark=remark,headers=headers)

def positions_republish(positionId,typeId):
	url = host + "/positions/" + positionId + "/republish"
	data = {
		"isConfirm": False,
		"typeId":typeId

	}
	remark = "重新发布"
	return json_put(url=url, data=data, headers=headers, remark=remark)



# category_mapping("Java开发")
# post_positions('开发|测试|运维类','后端开发','Java','Java开发工程师1')

# get_online_positions()
# positions_republish(str(13845002),0)
# positions_query_position_type()
# get_other_positions()
# get_offline_positions()
# positions_details(str(13845259))
# positions_details_app(str(13845370))
