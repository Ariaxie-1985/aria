# coding:utf-8
import pytest

from api_script.business.B_calling import calling
from utils.util import login
import logging
from utils.read_file import get_yaml_test_data

cUserid = 100012422


@pytest.mark.skip(reason="暂时注掉先不跑")
def test_calling(login_web_k8s_env_b):
    # 暂时注掉先不跑

    s = calling(cUserid)
    logging.getLogger().setLevel(logging.INFO)

    # if s['message'] == u'成功':
    try:
        assert s['message'] == '成功'
        logging.info(u'calling获取成功,虚拟号码：' + str(s['content']['data']['result']['virtualPhone']))

    # print(s['content']['data']['result']['virtualPhone'])
    except:
        logging.info(u'calling获取失败，响应信息：' + str(s))
    # print(s)

# test_calling()
