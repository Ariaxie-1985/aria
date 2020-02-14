# coding:utf-8
# @Time  : 2019-04-28 14:00
# @Author: Xiawang
from api_script.neirong_app.resumes import resumes_list
from utils.util import assert_equal


def test_resumes_list(login_app):
    res = resumes_list(userToken=login_app)
    assert_equal(1, res['state'], '查询简历列表数据成功')
