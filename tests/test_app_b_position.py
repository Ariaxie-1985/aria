# coding:utf-8
# @Time  : 2019-01-14 19:38
# @Author: Xiawang
from api_script.positions_app.b_position import post_positions, category_mapping, publish_position_check, \
	positions_details, update_position, get_online_positions, positions_static_info, get_offline_positions, \
	get_other_positions, apply_privilege_position, refresh_position, up_position_ranking, positions_top_check, \
	positions_is_hot, positions_invite, positions_recommend, positions_red_point_hint
from util.util import assert_equal
from util.read_yaml import get_yaml_test_data

test_data = get_yaml_test_data("test_app_b_position.yaml")
positionName = test_data['positionName']
apply_privilege_position_userId = test_data['apply_userId']
# invite_userId_list = test_data['invite_userId_list']


def test_positions_static_info():
	res = positions_static_info()
	assert_equal(1, res['state'], "获取职位静态信息成功", "获取职位静态信息失败, 失败信息: " + res['message'])


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
	positionId = str(res['content']['mdsPositionId'])
	assert_equal(1, res['state'], "发布职位成功,该职位的PositionId: " + str(res['content']['mdsPositionId']),
	             "发布职位失败, 该message: " + res['message'])


def test_get_online_positions():
	res = get_online_positions()
	ids = []
	for i in res['content']['positions']['result']:
		ids.append(i['positionId'])
	assert_equal(True, int(positionId) in ids, "职位id: " + positionId + "在在线职位列表里",
	             "职位id:" + positionId + " 不在在线职位列表里")


def test_positions_details():
	res = positions_details(str(positionId))
	assert_equal(1, res['state'], "获取职位详情成功", "获取职位详情失败")


def test_update_position():
	res = update_position(str(positionId))
	assert_equal(1, res['state'], "编辑职位成功", "编辑职位失败")


def test_get_offline_positions():
	res = get_offline_positions()
	assert_equal(1, res['state'], "获取下线职位列表成功", "获取下线职位列表失败")


def test_get_other_positions():
	res = get_other_positions()
	assert_equal(1, res['state'], "获取其他职位列表成功", "获取其他职位列表失败")


def test_apply_privilege_position():
	res = apply_privilege_position(apply_privilege_position_userId)
	assert_equal(1, res['state'], "获取其他职位列表成功", "获取其他职位列表失败")


def test_refresh_position():
	res = refresh_position(positionId)
	assert_equal(1, res['state'], "刷新职位成功", "刷新职位失败")


def test_up_position_ranking():
	res = up_position_ranking(positionId)
	assert_equal(1, res['state'], "提升职位排名成功", "提升职位排名失败")


def test_positions_top_check():
	res = positions_top_check(positionId)
	assert_equal(1, res['state'], "职位置顶卡校验成功", "职位置顶卡校验失败")


def test_positions_is_hot():
	res = positions_is_hot(positionName)
	assert_equal(True, res['content']['isHot'], "是热门职位", "非热门职位")

'''
因测试环境无法构造需要的测试数据故不执行此用例

def test_positions_invite():
	res = positions_invite(positionId, invite_userId_list)
	assert_equal(1, res['state'], "批量邀约候选人成功", "批量邀约候选人失败")


def test_positions_recommend():
	res = positions_recommend(positionId)
	assert_equal("邀约人数不足", res['message'], "职位推荐没成功, 因为邀约失败")

'''



def test_positions_red_point_hint():
	res = positions_red_point_hint()
	assert_equal(False, res['content']['isShowRedPointHint'], "首页导航职位有红点", "首页导航职位无红点")
