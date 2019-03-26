# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_app_header, get_requests, json_post
import random
header=get_app_header(100018375)
alist = random.sample(range(1,10000000),50)
def hasDelivered():
    url='https://gate.lagou.com/v1/entry/order/hasDelivered'
    data={'positionIds':5378018}
    return get_requests(url=url,headers=header,data=data,remark='职位是否已投递')


# print (alist)
# hasDelivered()