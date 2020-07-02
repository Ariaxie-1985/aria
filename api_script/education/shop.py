# coding:utf-8
# @Time  : 2019-07-09 14:39
# @Author: Sunnyzhang
import json

from utils.util import get_requests, get_code_token, json_post


def create_shop_goodsOrder_course(payLagouCoinNum, sellGoodsPriceId, gateLoginToken, shopOrderToken):
    url = 'https://gate.lagou.com/v1/zhaopin/shop/goodsOrder/create'
    header = get_code_token(url='https://easy.lagou.com/shop/onSaleGoods.htm?')
    header.add({'X-L-REQ-HEADER': json.dumps({'deviceType': 1}), "Cookie": f"gate_login_token ={gateLoginToken};",
                'shop-order-token': shopOrderToken})
    data = {
        "payLagouCoinNum": payLagouCoinNum,
        "sellGoodsPriceId": sellGoodsPriceId,
        "expandInfo": "https://kaiwu.lagou.com/course/courseInfo.htm?"
    }
    remark = '课程订单创建'
    return json_post(url=url, headers=header, data=data, remark=remark, rd='Mrpro Liu')
