# coding:utf-8
# @Time  : 2019-03-08 10:56
# @Author: Xiawang
import pytest

from api_script.zhaopin_app.c_user import baseStatus_get
from api_script.zhaopin_app.configure import positionCategories
from api_script.zhaopin_app.positionsearch import getPromotionPositions, hr_getHRCard, searchPosition
from utils.util import assert_equal


# @pytest.mark.skip(reason="暂不执行")
@pytest.mark.parametrize('keyword, city,lastShowCompanyId', [('销售', '天津', None)])
def test_getPromotionPositions(keyword, city, lastShowCompanyId):
    r = getPromotionPositions(keyword, city, lastShowCompanyId).json()
    assert_equal(1, r['state'], "获取全民升职季成功")


@pytest.mark.parametrize('id, tagType', [('100014641', ''), ('100014641', '0'), ('100014641', '1'), ('100014641', '2')])
def test_hr_getHRCard(id, tagType):
    r = hr_getHRCard(id, tagType).json()
    assert_equal(1, r['state'], "HR信息获取成功")


@pytest.mark.parametrize('keyword,sort', [("java", 1)])
def test_searchPosition(keyword, sort):
    r = searchPosition(keyword, sort)
    assert_equal(1, r['state'], "搜索java职位信息成功")


@pytest.mark.parametrize('type', [(None), (1), (2), (3)])
def test_positionCategories(type):
    r = positionCategories(type).json()

    if type == None:
        assert_equal(1, r['state'], "查询职位分类配置信息获取成功")
        assert_equal(18, len(r['content']), "全部职业分类的长度获取一致")
    elif type == 1:
        assert_equal(1, r['state'], "查询互联网的职位分类配置信息获取成功")
        assert_equal(7, len(r['content']), "互联网职业分类的长度获取一致")
    elif type == 2:
        assert_equal(1, r['state'], "查询非互联网的职位分类配置信息获取成功")
        assert_equal(11, len(r['content']), "非互联网职业分类的长度获取一致")
    else:
        assert_equal(0, len(r['content']), "对职位分类级别字段的异常处理正确")


def test_baseStatus_get():
    r = baseStatus_get().json()
    assert_equal(1, r['state'], "获取C端用户信息成功")
    assert_equal(6198138, r['content']['resumeId'], "获取C端用户的简历id成功")
