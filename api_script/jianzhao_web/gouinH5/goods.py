# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_requests, form_post,login,get_code_token
login('0086','18810432995')

def goods():
    url='https://jf.lagou.com/integral/mall/my/goods.json'
    return get_requests(url,remark='我兑换的商品')

# goods()