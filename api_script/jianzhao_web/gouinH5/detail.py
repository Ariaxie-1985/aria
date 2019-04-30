# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_requests, form_post,login,get_code_token


def detail(gooids):
    login('0086','18810432995')
    url='https://jf.lagou.com/integral/mall/goods/detail.json'
    data={'goodsId':gooids}
    return get_requests(url=url,remark='商品详情',data=data)
# detail()