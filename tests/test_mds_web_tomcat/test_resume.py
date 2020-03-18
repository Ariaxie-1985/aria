# coding:utf-8
# @Time  : 2020/3/18 19:25
# @Author: Xiawang
# Description:
from api_script.jianzhao_web.resume_manage.resume import get_not_read_resume_count
from utils.util import assert_equal


def test_get_not_read_resume_count():
    r = get_not_read_resume_count()
    assert_equal(True, bool(r['content']['data']['resumeCount']), '统计未读简历数用例通过')
