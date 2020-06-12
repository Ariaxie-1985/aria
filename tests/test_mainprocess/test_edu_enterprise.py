import pytest
from utils.util import assert_equal
from api_script.education.enterprise import search_staff
def test_query_user(enterprise_login):
    r = search_staff()
    print(r)
    assert_equal('bj', r['content']['enterpriseStaffDetailDTOs']['recordList'][0]['staffName'], "查询员工姓名用例通过")

