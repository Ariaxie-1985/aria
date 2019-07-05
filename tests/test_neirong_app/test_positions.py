# coding:utf-8
# @Time  : 2019-05-31 11:44
# @Author: Xiawang
import pytest

from api_script.neirong_app.positions import mark_info
from utils.util import assert_equal


@pytest.importorskip('test_positions.py', reason='大厂一期接口新增标记直招接口，待上线后再执行')
@pytest.mark.parametrize('positionIds, expect_result, assert_info',
                         [(5378764, "r['content']['positionMarks'][0]['directRecruitment']", '非HR岗标记直招成功 断言成功'),
                          (5379071, "not bool(r['content']['positionMarks'])", 'HR岗标记失败 断言成功')])
def test_mark_info(positionIds, expect_result, assert_info):
    r = mark_info(positionIds)
    assert_equal(True, eval(expect_result), assert_info)
