# coding:utf-8
# @Time  : 2019-01-14 19:38
# @Author: Xiawang
import pytest
import requests

from api_script.zhaopin_app.b_position import post_positions, category_mapping, publish_position_check, \
    positions_details, update_position, get_online_positions, positions_static_info, get_offline_positions, \
    get_other_positions, apply_privilege_position, refresh_position, up_position_ranking, positions_top_check, \
    positions_is_hot, positions_query_position_type, positions_republish, positions_details_app, \
    positions_red_point_hint, positions_offline, post_myOnlinePositions, publish_guide
# invite_userId_list = test_data['invite_userId_list']
# session = requests.session()
# session.cookies.clear()
from utils.util import assert_equal


def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_positions_static_info():
    res = positions_static_info()
    assert_equal(1, res['state'], "获取职位静态信息成功", "获取职位静态信息失败, 失败信息: " + res['message'])


@pytest.mark.parametrize("positionName", [('新媒体运营')])
def test_category_mapping(positionName):
    positionInfo = category_mapping(positionName)
    global firstType, positionType, positionThirdType
    firstType = positionInfo['content']['firstCateGory']
    positionType = positionInfo['content']['secCategory']
    positionThirdType = positionInfo['content']['thirdCateGory']
    assert_equal(True, bool(positionThirdType), "职位名称映射职位分类成功", "职位名称映射职位分类无结果")


def test_publish_position_check():
    res = publish_position_check()
    assert_equal(1, res['state'], "可以发布职位", res['message'])


@pytest.mark.parametrize("positionName", [('新媒体运营')])
def test_post_positions(positionName):
    res = post_positions()
    global positionId
    positionId = res['content']['mdsPositionId']
    assert_equal(1, res['state'], "发布职位成功", "发布职位失败")


def test_get_online_positions():
    res = get_online_positions()
    # ids = [i['positionId'] for i in res['content']['positions']['result']]
    ids = [v['positionId'] for v in res['content']['positions']['result'] if v['isSoonOffline'] == False]
    # for i in res['content']['positions']['result']:
    #     ids.append(i['positionId'])
    assert_equal(True, positionId == ids[0], "职位id: " + str(positionId) + "在在线职位列表里",
                 "职位id:" + str(positionId) + " 不在在线职位列表里")


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


@pytest.mark.parametrize("apply_privilege_position_userId", [(100014643)])
def test_apply_privilege_position(apply_privilege_position_userId):
    res = apply_privilege_position(apply_privilege_position_userId)
    assert_equal(1, res['state'], "获取其他职位列表成功", "获取其他职位列表失败")


def test_refresh_position():
    res = refresh_position(str(positionId))
    assert_equal(1, res['state'], "刷新职位成功", "刷新职位失败")


def test_up_position_ranking():
    res = up_position_ranking(str(positionId))
    assert_equal(1, res['state'], "提升职位排名成功", "提升职位排名失败")


def test_positions_top_check():
    res = positions_top_check(str(positionId))
    assert_equal(1, res['state'], "职位置顶卡校验成功", "职位置顶卡校验失败")


@pytest.mark.parametrize("positionName", [('新媒体运营')])
def test_positions_is_hot(positionName):
    res = positions_is_hot(positionName)
    assert_equal(True, res['content']['isHot'], "是热门职位", "非热门职位")


# yqzhang新增

def test_positions_query_position_type():
    res = positions_query_position_type()
    assert_equal(1, res['state'], '获取成功', '获取失败')


'''

def test_positions_republish():
	res = positions_republish(str(positionId))
	assert_equal(1, res['state'], '获取重新发布提示信息成功', '获取重新发布提示信息失败')


def test_positions_details_app():
	res = positions_details_app(str(positionId))
	assert_equal(1, res['state'], "获取职位详情成功", "获取职位详情失败")
'''

'''
因测试环境无法构造需要的测试数据故不执行此用例

def test_positions_invite():
	res = positions_invite(positionId, invite_userId_list)
	assert_equal(1, res['state'], "批量邀约候选人成功", "批量邀约候选人失败")


def test_positions_recommend():
	res = positions_recommend(positionId)
	assert_equal("邀约人数不足", res['message'], "职位推荐没成功, 因为邀约失败")

'''


@pytest.mark.xfail(reason="首页导航职位无红点")
def test_positions_red_point_hint():
    res = positions_red_point_hint()
    assert_equal(True, res['content']['isShowRedPointHint'], "首页导航职位无红点", "首页导航职位有红点")


mdsPositionId = 0


@pytest.mark.skip(reason="等大厂引入TL上线后再执行")
@pytest.mark.monthly_position
def test_query_monthly_position_type():
    res = positions_query_position_type(userId=100019158, reqVersion=71600).json()
    name_list = [i['name'] for i in res['content']['positionTypes']]
    assert_equal(True, '月度职位' in name_list, '获取成功', '获取失败')


@pytest.mark.skip(reason="等大厂引入TL上线后再执行")
@pytest.mark.monthly_position
def test_post_monthly_position():
    res = post_myOnlinePositions(userid=100019158, workAddressId=192378, typeid=5)
    global mdsPositionId
    try:
        mdsPositionId = res['content']['mdsPositionId']
    except KeyError:
        mdsPositionId = 0
    assert_equal(1, res['state'], '发布月度职位成功！')


@pytest.mark.skip(reason="等大厂引入TL上线后再执行")
@pytest.mark.monthly_position
def test_get_online_monthly_position():
    res = get_online_positions(userId=100019158)
    try:
        positions_typeTag_list = [(i['positionId'], i['typeTag']) for i in res['content']['positions']['result']]
        for value in positions_typeTag_list:
            if value[0] == mdsPositionId:
                typeTag = value[1]
    except KeyError:
        typeTag = '非月度'
    assert_equal('月度', typeTag, '在线职位列表包含刚发布的月度职位')


@pytest.mark.skip(reason="等大厂引入TL上线后再执行")
@pytest.mark.monthly_position
def test_refresh_monthly_position():
    res = refresh_position(mdsPositionId, userId=100019158)
    assert_equal(107036, res['state'], "月度职位不能刷新校验通过")


@pytest.mark.skip(reason="等大厂引入TL上线后再执行")
@pytest.mark.monthly_position
def test_up_monthly_position_ranking():
    res = up_position_ranking(mdsPositionId, userId=100019158)
    assert_equal(107037, res['state'], "月度职位不能提升排名校验通过")


@pytest.mark.skip(reason="等大厂引入TL上线后再执行")
@pytest.mark.monthly_position
def test_monthly_positions_offline():
    res = positions_offline(mdsPositionId, userId=100019158)
    desc = res['content']['tipsInfo']['popUpTipsInfo']['desc']
    assert_equal(True, '月度职位' in desc, '下线月度职位成功')


@pytest.mark.skip(reason="等大厂引入TL上线后再执行")
@pytest.mark.monthly_position
def test_monthly_positions_republish():
    res = positions_republish(mdsPositionId, userId=100019158)
    assert_equal(107039, res['state'], '月度职位不能再发布的校验通过')


@pytest.mark.skip(reason="等大厂引入TL上线后再执行")
@pytest.mark.parametrize('userId, assert_info',
                         [(100014641, '非灰度公司无法开启邀请好友领取月度职位卡的启动页'), (100019165, '灰度公司的HR岗无法开启邀请好友领取月度职位卡的启动页')])
def test_publish_guide_0(userId, assert_info):
    res = publish_guide(userId)
    assert_equal(False, res['content']['guide'], assert_info)


@pytest.mark.skip(reason="等大厂引入TL上线后再执行")
@pytest.mark.parametrize('userId, assert_info',
                         [(100019158, '灰度公司的非HR岗可开启邀请好友领取月度职位卡的启动页')])
def test_publish_guide_1(userId, assert_info):
    res = publish_guide(userId)
    assert_equal(True, res['content']['guide'], assert_info)
