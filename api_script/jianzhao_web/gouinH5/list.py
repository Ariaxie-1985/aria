# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_requests, form_post,login,get_code_token
# login('0086','18810432995')
# login('00852','20181205')
def list():
    url='https://jf.lagou.com/integral/mall/goods/list.json'
    data={'pageNo':1,'pageSize':10,'isShowAd':0}
    return get_requests(url=url,data=data,remark='商品列表')

# list()