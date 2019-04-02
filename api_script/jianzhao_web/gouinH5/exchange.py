# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_requests, form_post,login,get_code_token,json_post
# login('0086','18810432995')
# login('00852','20181205')

def exchange(goodsid):
    url='https://jf.lagou.com/integral/mall/goods/exchange.json'
    data={'goodsId':goodsid,'deviceType':'web'}
    header=get_code_token('https://jf.lagou.com/task/center/index.htm')
    return json_post(url=url,data=data,remark='h5兑换积分商品',headers=header)

# exchange()