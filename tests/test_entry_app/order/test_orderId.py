# coding:utf-8
# @Time  : 2019-04-28 11:29
# @Author: Xiawang
import pytest

from api_script.entry.order.orderId import delete_orderId
from utils.util import assert_equal


# todo 需要找orderId
@pytest.importorskip('test_orderId.py', reason="需要等上线后才可在default环境用")
def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_delete_orderId():
    orderId = 1120927027160162304
    res = delete_orderId(orderId)
    assert_equal(1, res['state'], '删除orderId为{}投递记录成功'.format(orderId))
