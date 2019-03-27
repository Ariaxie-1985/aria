# coding:utf-8
# @Time  : 2019-03-27 15:25
# @Author: Xiawang
import pytest
from utils.convert_pytest import read_json, parser, run_case
from utils.util import assert_equal


@pytest.mark.parametrize(
    'file', [
        ('言职社区通知页优化需求.postman_collection.json')])
def test_postman_script(file):
    data = read_json(file)
    for url, method, content_type, header, body, remark, expect_res, actual_res in parser(
            data):
        jsonData = run_case(url, method, content_type, header, body, remark)
        assert_equal(expect_res, eval(actual_res), ''.join(
            [remark, ' 用例通过']), ''.join([remark, ' 用例失败']))


