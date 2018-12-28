# -*- coding: utf8 -*-
__author__ = 'yqzhang'
import logging
from api_script.business.B_position_limit import position_limit,position,getrefreshpoint,getpositionlimit
from api_script.util import login

login('00853','05180001')


def test_position_limit():
    logging.getLogger().setLevel(logging.INFO)
    a,b = getpositionlimit()
    s,d = position_limit()
    # print(a - b, d)
    try:
        assert a-b==d

        logging.info('职位限制正确,'+'已发职位：'+str(d)+'.特权职位上限：'+str(a)+'.执行本用例前已存在的职位：'+str(b))
    except:
        logging.info('职位限制异常或发布职位错误'+str(s))
# test_position_limit()