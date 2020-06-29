import pytest
from utils.util import assert_equal
from api_script.education.enterprise import search_staff


def test_query_user(enterprise_login):
    r = search_staff()
    assert_equal('bj', r.get('content').get('enterpriseStaffDetailDTOs').get('recordList')[0].get('staffName'),
                 "查询员工姓名用例通过", te='谢梦')
