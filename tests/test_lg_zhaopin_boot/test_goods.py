# coding:utf-8
# @Time  : 2020/2/26 18:29
# @Author: Xiawang
# Description:
from api_script.zhaopin_app.b_goods import goods_product_version
from utils.util import assert_equal


def test_goods_product_version(b_login_app):
    r = goods_product_version(userToken=b_login_app[0])
    assert_equal(True, bool(r['content']['version']), "获取当前用户商业产品版本号用例通过")
