# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_requests, form_post,login,get_code_token
login('0086','18810432995')
# login('00852','20181205')
def flow():
    url='https://jf.lagou.com/integral/mall/gouyin/flow.json'
    # header=get_code_token('')
    data={'queryFlowType':0,'pageNo':1,'pageSize':10}
    return get_requests(url=url,data=data,remark='勾印流水')

# flow()