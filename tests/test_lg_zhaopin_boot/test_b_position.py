# coding:utf-8
# @Time  : 2020/3/3 16:02
# @Author: Xiawang
# Description:
import pytest

from api_script.zhaopin_app.b_position import positions_category, category_mapping
from utils.util import assert_equal


def test_positions_category(b_login_app):
    r = positions_category(userToken=b_login_app[0])
    try:
        actual_result = r['content']['positionTypeTreeVO']['itPositionFirstCategorys'][0]['name']
    except (IndexError, KeyError):
        actual_result = ""
    assert_equal('开发|测试|运维类', actual_result, '获取职业静态信息用例通过')

@pytest.mark.parametrize("positionName,expect",[("java",'后端开发'),('测试','测试')])
def test_category_mapping(b_login_app, positionName,expect):
    r = category_mapping(userToken=b_login_app[0], positionName=positionName)
    assert_equal(expect, r['content']['secCategory'],'职位名称映射职位分类用例通过')
