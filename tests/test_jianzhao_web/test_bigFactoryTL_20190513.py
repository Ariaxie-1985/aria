# coding:utf-8
# @Time  : 2019-05-13 20:30
# @Author: Xiawang
import pytest

from api_script.home.lagou_plus import get_contract_No, close_contract, open_product
from api_script.jianzhao_web.b_position.bigFactoryTL_20190513 import recruitcard_pop
from utils.util import assert_equal


@pytest.importorskip('test_bigFactoryTL_20190513.py', reason="等大厂引入TL上线后再执行")
def setup_module(module):
    pass


def teardown_module(module):
    pass


company_lgId = 143228
userId = 100019158


def test_recruitcard_pop_1(login_web_k8s_default):
    res = recruitcard_pop()
    assert_equal(469, res['state'], '非灰度公司不能领取月度卡校验通过')


def test_recruitcard_pop_2(login_web_k8s_143242_TL1):
    res = recruitcard_pop()
    assert_equal(465, res['state'], '北京的免费公司的TL不能领取月度卡校验通过')


def test_recruitcard_pop_3(login_web_k8s_142373_TL1):
    res = recruitcard_pop()
    assert_equal(463, res['state'], '北京的付费公司的HR不能领取月度卡校验通过')


def test_recruitcard_pop_4(login_web_k8s_142373_TL2):
    res = recruitcard_pop()
    assert_equal(1, res['state'], '北京的付费公司的TL可以领取月度卡校验通过')


def test_recruitcard_pop_5(login_web_k8s_142373_TL2):
    res = recruitcard_pop()
    assert_equal(-1, res['state'], '重复领取不会领取成功')


def test_recruitcard_pop_6(login_web_k8s_142373_TL3):
    res = recruitcard_pop()
    assert_equal(1, res['state'], '北京的付费公司的TL可以领取月度卡校验通过')


def test_recruitcard_pop_7(login_web_k8s_143232_TL1):
    res = recruitcard_pop()
    assert_equal(463, res['state'], '太原的免费公司的HR不能领取月度卡校验通过')


def test_recruitcard_pop_8(login_web_k8s_143235_TL1):
    res = recruitcard_pop()
    assert_equal(1, res['state'], '无城市的免费公司的TL可以领取月度卡校验通过')


def test_recruitcard_pop_9(login_web_k8s_143236_TL1):
    res = recruitcard_pop()
    assert_equal(459, res['state'], '未完成招聘者审核的帐号不可领取月度卡校验成功')
