# coding:utf-8
# @Time  : 2019-04-28 14:00
# @Author: Xiawang
from api_script.neirong_app.resumes import resumes_list
from utils.util import assert_equal


def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_resumes_list():
    res = resumes_list()
    assert_equal(1, res['state'], '查询简历列表数据成功')
