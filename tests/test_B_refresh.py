# -*- coding: utf8 -*-
__author__ = 'yqzhang'
import logging
from api_script.business.B_refresh import refrech,getpositionId,getrefreshpoint
from utils.util import login
from utils.read_file import get_yaml_test_data

test_data = get_yaml_test_data('logininfo.yaml')
countrycode = test_data['countrycode']
username = test_data['username']

login(countrycode,username)


# login('00853','05180001')
def test_refresh():
    logging.getLogger().setLevel(logging.INFO)
    a = getrefreshpoint()
    logging.info('刷新前的点数:'+str(a))
    # 免费刷新后，需过一段时间才可以付费刷新，单位秒,正常配置3600s
    s = refrech(getpositionId())
    if s['message'] == '操作成功':
        b = getrefreshpoint()
        logging.info('刷新后的刷新点数：'+str(b))
        try:
            assert a != b
            logging.info('刷新成功')
        except:
            logging.info('刷新点数未发生变化:'+str(s))
    else:
        logging.info('刷新异常'+str(s))






# test_refresh()