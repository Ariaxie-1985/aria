# coding:utf-8
import pytest

from api_script.business.B_calling import calling
from utils.util import login ,assert_equal
import logging
from utils.read_file import get_yaml_test_data

# cUserid = 100012422
def setup_module(module):
    pass
def teardown_module(module):
    pass

# @pytest.mark.skip(reason="暂时注掉先不跑")
def test_calling(login_web_k8s_env_b):
    s = calling(80)
    logging.getLogger().setLevel(logging.INFO)
    # assert s['message'] == '成功'
    assert_equal( '成功',s['message'],'calling获取成功,虚拟号码：' + str(s['content']['data']['result']['virtualPhone']),'calling获取失败，响应信息：' + str(s))



# test_calling()
