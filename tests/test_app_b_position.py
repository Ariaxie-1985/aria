# coding:utf-8
# @Time  : 2019-01-14 19:38
# @Author: Xiawang
from api_script.positions_app.b_position import post_positions, category_mapping, publish_position_check, \
	positions_details, update_position, get_online_positions
from util.util import assert_equal
from util.read_yaml import get_yaml_test_data

test_data = get_yaml_test_data("test_app_b_position.yaml")
positionName = test_data['positionName']


def test_category_mapping():
	positionInfo = category_mapping(positionName)
	global firstType, positionType, positionThirdType
	firstType = positionInfo['content']['firstCateGory']
	positionType = positionInfo['content']['secCategory']
	positionThirdType = positionInfo['content']['thirdCateGory']
	assert_equal(True, bool(positionThirdType), "职位名称映射职位分类成功", "职位名称映射职位分类无结果")


def test_publish_position_check():
	res = publish_position_check()
	assert_equal(1, res['state'], "可以发布职位", res['message'])


def test_post_positions():
	res = post_positions(firstType,
	                     positionType,
	                     positionThirdType,
	                     positionName)
	global positionId
	positionId = res['content']['mdsPositionId']
	assert_equal(1, res['state'], "发布职位成功,该职位的PositionId: " + str(res['content']['mdsPositionId']),
	             "发布职位失败, 该message: " + res['message'])


def test_get_onlinepositions():
	res = get_online_positions()
	ids = []
	for i in res['content']['positions']['result']:
		ids.append(i['positionId'])
	assert_equal(True, positionId in ids, "职位id: " + str(positionId) + "在在线职位列表里",
	             "职位id:" + str(positionId) + " 不在在线职位列表里")


def test_positions_details():
	res = positions_details(str(positionId))
	assert_equal(1, res['state'], "获取职位详情成功", "获取职位详情失败")


def test_update_position():
	res = update_position(str(positionId))
	assert_equal(1, res['state'], "编辑职位成功", "编辑职位失败")
