# coding:utf-8
# @Time  : 2020/4/28 16:14
# @Author: Xiawang
# Description:
import json

from utils.util import get_requests, get_code_token, json_post


def get_shop_goods_on_sale_goods():
    url = 'https://gate.lagou.com/v1/zhaopin/shop/goods/onSaleGoods'
    header = get_code_token(url='https://easy.lagou.com/shop/onSaleGoods.htm?')
    header.update({'X-L-REQ-HEADER': json.dumps({'deviceType': 1})})
    remark = '道具商城--招聘道具--获取在售权益及其价格信息'
    return get_requests(url=url, headers=header, remark=remark, rd='杨振宇')


def get_shop_goods_account_info():
    url = 'https://gate.lagou.com/v1/zhaopin/shop/account/get'
    header = get_code_token(url='https://easy.lagou.com/shop/onSaleGoods.htm?')
    header.update({'X-L-REQ-HEADER': json.dumps({'deviceType': 1})})
    remark = '道具商城--招聘道具--获取当前用户的钱包信息'
    return get_requests(url=url, headers=header, remark=remark, rd='杨振宇')


def get_shop_goods_sell_goods(on_sale_goods_id):
    url = f'https://gate.lagou.com/v1/zhaopin/shop/goods/sellGoods/{on_sale_goods_id}'
    header = get_code_token(url='https://easy.lagou.com/shop/onSaleGoods.htm?')
    header.update({'X-L-REQ-HEADER': json.dumps({'deviceType': 1})})
    remark = '道具商城--招聘道具--购买道具'
    return json_post(url=url, headers=header, remark=remark, rd='杨振宇')


def create_shop_goodsOrder(payLagouBpNum, payLagouCoinNum, sellGoodsPriceId, shopOrderToken):
    url = 'https://gate.lagou.com/v1/zhaopin/shop/goodsOrder/create'
    header = get_code_token(url='https://easy.lagou.com/shop/onSaleGoods.htm?')
    header.update({'X-L-REQ-HEADER': json.dumps({'deviceType': 1}), 'shop-order-token': shopOrderToken})
    data = {
        "payLagouBpNum": payLagouBpNum,
        "payLagouCoinNum": payLagouCoinNum,
        "sellGoodsPriceId": sellGoodsPriceId,
        "expandInfo": "https://easy.lagou.com/shop/onSaleGoods.htm?"
    }
    remark = '购买招聘道具'
    return json_post(url=url, headers=header, data=data, remark=remark, rd='杨振宇')


def pay_shop_goodsOrder(orderNo):
    url = f'https://gate.lagou.com/v1/zhaopin/shop/goodsOrder/pay/{orderNo}'
    header = get_code_token(url='https://easy.lagou.com/shop/onSaleGoods.htm?')
    header.update({'X-L-REQ-HEADER': json.dumps({'deviceType': 1})})
    remark = '道具商城--招聘道具--购买道具--支付订单'
    return json_post(url=url, headers=header, remark=remark, rd='杨振宇')


def check_shop_goodsOrder(orderNo):
    url = f'https://gate.lagou.com/v1/zhaopin/shop/goodsOrder/check/{orderNo}'
    header = get_code_token(url='https://easy.lagou.com/shop/onSaleGoods.htm?')
    header.update({'X-L-REQ-HEADER': json.dumps({'deviceType': 1})})
    remark = '道具商城--招聘道具--购买道具--检查订单'
    return json_post(url=url, headers=header, remark=remark, rd='杨振宇')
