# -*- coding: utf8 -*-
__author__ = 'yqzhang'
import logging
from api_script.business.B_refresh import refrech,getpositionId,getrefreshpoint
from util.util import login

second = 3600
login('00853','05180001')
def test_refresh():
    logging.getLogger().setLevel(logging.INFO)
    a = getrefreshpoint()
    logging.info('刷新前的点数:'+str(a))
    # 免费刷新后，需过一段时间才可以付费刷新，单位秒,正常配置3600s
    s = refrech(getpositionId(),second)
    if s['message'] == '操作成功':
        b = getrefreshpoint()
        logging.info('刷新后的刷新点数：'+str(b))
        try:
            assert a != b
            logging.info('刷新成功')
        except:
            logging.info('未花费刷新点数:'+str(s))
    else:
        logging.info('刷新异常'+str(s))






# test_refresh()