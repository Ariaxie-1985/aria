# coding:utf-8
# @Time  : 2019-05-14 16:29
# @Author: Xiawang
import pytest

from api_script.home.lagou_plus import get_contract_No, close_contract, open_product
from api_script.zhaopin_app.integral import integral_recruitcard_pop
from utils.util import assert_equal

@pytest.importorskip('test_integral', reason="需要等上线后才可在default环境用")
def setup_module(module):
    pass


def teardown_module(module):
    pass


company_lgId = 143228
userId = 100019158


def test_recruitcard_pop_1():
    res = integral_recruitcard_pop(100014641)
    assert_equal(1014, res['state'], '非灰度公司不能领取直招卡校验通过')


def test_close_contract(login_home_k8s_default):
    global contractNo
    contractNo = get_contract_No(company_lgId)
    res = close_contract(contractNo)
    assert_equal(True, res, '关闭合同成功')


def test_recruitcard_pop_2():
    res = integral_recruitcard_pop(100019166)
    assert_equal(1008, res['state'], '北京的免费公司不能领取直招卡校验通过')


def test_home_contract_product(login_home_k8s_default):
    res = open_product(company_lgId, userId, contractNo)
    assert_equal(True, res, '新建产品成功')


def test_recruitcard_pop_3():
    res = integral_recruitcard_pop(100019166)
    assert_equal(1, res['state'], '北京的付费公司HR能领取直招卡校验通过')


def test_recruitcard_pop_4():
    res = integral_recruitcard_pop(100019166)
    assert_equal(1008, res['state'], '北京的付费公司HR再次领取，无法领取直招卡失败校验通过')


def test_recruitcard_pop_5():
    res = integral_recruitcard_pop(100019165)
    assert_equal(1008, res['state'], '北京的付费公司非HR不能领取直招卡校验通过')
