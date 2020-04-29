# coding:utf-8
# @Time  : 2020/4/29 14:12
# @Author: Xiawang
# Description:
import pytest

from api_script.jianzhao_web.task_center import get_newer_task, receive_newer_task_reward, \
    receive_gouyin_weekly_task_points
from api_script.zhaopin_app.shop import get_shop_goods_on_sale_goods, get_shop_goods_sell_goods, create_shop_goodsOrder, \
    pay_shop_goodsOrder, check_shop_goodsOrder
from utils.util import assert_equal


def test_get_newer_task():
    r = get_newer_task()
    assert_equal(1, r.get('state'), '任务中心获取新手任务用例通过')
    global task_reward_info
    task_reward_info = []
    for task in r['data']:
        if task['statusName'] == 'COMPLETE':
            task_reward_info.append((task['id'], task['taskLabelName'], task['taskGroupName']))
    assert_equal(3, len(task_reward_info), '领取积分通过')


def test_receive_newer_task_reward():
    for task in task_reward_info:
        r = receive_newer_task_reward(recordId=task[0], taskLabel=task[1], taskGroup=task[2])
        assert_equal(1, r['state'], '任务中心--新手任务--领取积分用例通过')


def test_receive_gouyin_weekly_task_points():
    r = receive_gouyin_weekly_task_points()
    assert_equal(True, bool(r['data'] >= 300), '任务中心--获取本周积分超过300分成功')


def test_get_shop_goods_on_sale_goods_IM_CHAT_NUMBER():
    r = get_shop_goods_on_sale_goods()
    assert_equal(1, r['state'], '道具商城--招聘道具--获取在售权益及其价格信息用例通过')
    global im_chat_number
    im_chat_number = r['content']['onSaleGoods']['IM_CHAT_NUMBER']


def test_get_shop_goods_sell_goods():
    r = get_shop_goods_sell_goods(on_sale_goods_id=im_chat_number)
    assert_equal(1, r['content']['status'], '购买沟通点数-前置条件用例通过')
    global sellGoodsPriceId
    for sellGoodsPriceRes in r['content']['sellGoodsInfo']['sellGoodsStrategyResList'][0]['sellGoodsPriceResList']:
        if sellGoodsPriceRes['preferentialPolicyCurrencyNum'] == 300:
            sellGoodsPriceId = sellGoodsPriceRes['sellGoodsPriceId']
    assert_equal(True, bool(sellGoodsPriceId), "购买沟通点数的300积分条件通过")


@pytest.mark.parametrize("payLagouBpNum,payLagouCoinNum", [(300, 0)])
def test_create_shop_goodsOrder(payLagouBpNum, payLagouCoinNum):
    r = create_shop_goodsOrder(payLagouBpNum=payLagouBpNum, payLagouCoinNum=payLagouCoinNum,
                               sellGoodsPriceId=sellGoodsPriceId)
    assert_equal(1, r['state'], '购买沟通点数用例通过')
    global orderNo
    if r['content']['orderState'] == 'CREATE':
        orderNo = r['content']['orderNo']


def test_pay_shop_goodsOrder():
    r = pay_shop_goodsOrder(orderNo=orderNo)
    assert_equal(1, r['content']['status'], '道具商城--招聘道具--购买道具--支付订单用例通过')


def test_check_shop_goodsOrder():
    r = check_shop_goodsOrder(orderNo=orderNo)
    assert_equal(1, r['content']['status'], '道具商城--招聘道具--购买道具--检查订单用例通过')
