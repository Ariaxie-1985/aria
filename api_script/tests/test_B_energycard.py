# -*- coding: utf8 -*-
__author__ = 'yqzhang'
import logging
import datetime
from api_script.business.B_energycard import energycard,getpositionId
from util.util import login


login('00853','05180001')

def test_energycard():
    logging.getLogger().setLevel(logging.INFO)
    s = energycard(getpositionId())
    if s['message'] == '操作成功':
        a = s['content']['data']['info']['startTime']
        b = s['content']['data']['info']['endTime']
        d=datetime.datetime.strptime(b,'%Y-%m-%d %H:%M:%S')-datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
        try:
            assert d.days==7
            logging.info('赋能卡使用成功' + '结束时间' + a + '开始时间' + b)
        except:
            logging.info('赋能卡使用成功，但时间异常'+str(s))
    else:
        logging.info('赋能卡使用失败'+str(s))


# test_energycard()