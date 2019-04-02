# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from api_script.jianzhao_web.gouinH5.exchange import exchange
from utils.util import login, assert_equal
from api_script.jianzhao_web.gouinH5.list import list
import pytest
def setup_module(module):
    pass


def teardown_module(module):
    pass
@pytest.mark.skip(reason="勾印不足, 先跳过")
def test_exchange():
    s=list().json()
    goodsid=s['content']['data']['allGoods']['data']['goodsList'][0]['goodsId']
    r=exchange(goodsid)
    assert_equal(1, r['state'], "兑换积分成功成功")
# test_exchange()