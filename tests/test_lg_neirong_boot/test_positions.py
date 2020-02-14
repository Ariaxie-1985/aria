# coding:utf-8
# @Time  : 2019-05-31 11:44
# @Author: Xiawang
from api_script.neirong_app.positions import positions_mark_info
from api_script.zhaopin_app.b_position import get_online_positions
from utils.util import assert_equal


def test_get_online_positions(login_app):
    r = get_online_positions(userToken=login_app, H9=True)
    global positionId
    positionId = r['content']['positions']['result'][0]['positionId']
    assert_equal(1, r['state'], '获取职位id用例成功')


def test_positions_mark_info(login_app):
    r = positions_mark_info(userToken=login_app, positionId=positionId)
    assert_equal(1, r['state'], '职位标记直招用例成功')
