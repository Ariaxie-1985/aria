# coding:utf-8
# @Time  : 2020/2/20 18:52
# @Author: Xiawang
# Description:
import pytest

from api_script.entry.position.communicatePositions import get_position_detail, get_position_publisher, \
    get_communicate_positions
from utils.util import assert_equal


def test_get_position_detail(login_app, query_position, ip_port):
    r = get_position_detail(userToken=login_app[0], userId=login_app[1], ip_port=ip_port, positionId=query_position)
    assert_equal(query_position, r['content']['positionId'], '根据职位id查询职位详情用例通过')


@pytest.mark.parametrize("hr_Id", [(15130154)])
def test_get_position_publisher(login_app, hr_Id):
    r = get_position_publisher(userToken=login_app, hr_Id=hr_Id)
    assert_equal(True, bool(r['content']['positions']), 'HR发布职位列表用例通过')


@pytest.mark.parametrize("hr_Id", [(15130154)])
def test_get_communicate_positions(login_app, hr_Id):
    r = get_communicate_positions(userToken=login_app, hr_Id=hr_Id)
    assert_equal(True, bool(r['content']['positions']), '查询沟通职位列表用例通过')
