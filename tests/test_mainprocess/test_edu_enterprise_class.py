import pytest
from utils.util import assert_equal
from api_script.education.enterprise import search_staff, add_user, remove_user, del_user, get_lagou_user_id_study, \
    search_staff_after_remove


@pytest.mark.incremental
class TestEnterprise(object):
    @pytest.mark.parametrize(
        "user_name,code,phone,email,position,enterpriseId,is_show",
        [("自动化测试", "0086", "13093845372", "ariaxie@lagou.com", "test", "2", "false")])
    def test_add_user(self, enterprise_login, user_name, code, phone, email, position, enterpriseId, is_show):
        r = add_user(user_name, code, phone, email, position, enterpriseId, is_show)
        assert_equal(1, r.get('state'), "添加员工成功", te="张红彦")

    def test_get_enterprise_id_from_study(self):
        global enterprise_id
        source = get_lagou_user_id_study()
        assert_equal(1, source.get('state'), "从在学获取数据源成功")
        enterprise_id = source.get('content').get('enterpriseStaffDetailDTOs').get('recordList')[0].get('enterpriseId')
        assert_equal(True, bool(enterprise_id), "获取enterprise_id成功", te="张红彦")

    def test_query_user(self):
        r = search_staff(enterprise_id)
        assert_equal('自动化测试', r.get('content').get('enterpriseStaffDetailDTOs').get('recordList')[0].get('staffName'),
                     "查询员工姓名用例通过", te="张红彦")

    def test_get_staff_id_from_study(self):
        global staff_id_from_study
        source = get_lagou_user_id_study()
        assert_equal(1, source.get('state'), "从在学获取数据源成功")
        lagou_user_id_list = source.get('content').get('enterpriseStaffDetailDTOs').get('recordList')
        for e in lagou_user_id_list:
            lagou_user_id = e.get('lagouUserId')
            if lagou_user_id == 11184681:
                staff_id_from_study = e.get('staffId')
                assert_equal(True, bool(staff_id_from_study), "获取staff_id成功", te="张红彦")
                break

    def test_get_staff_id_from_remove(self):
        global staff_id_from_remove
        source = get_lagou_user_id_study()
        assert_equal(1, source.get('state'), "从在学获取数据源成功")
        lagou_user_id_list = source.get('content').get('enterpriseStaffDetailDTOs').get('recordList')
        for e in lagou_user_id_list:
            lagou_user_id = e.get('lagouUserId')
            if lagou_user_id == 11184681:
                staff_id_from_remove = e.get('staffId')
                assert_equal(True, bool(staff_id_from_remove), "获取staff_id成功", te="张红彦")
                break

    def test_remove_user(self):
        r = remove_user(staff_id_from_remove)
        assert_equal(1, r.get('state'), "移除员工成功", te="张红彦")

    def test_query_user_after_remove(self):
        r = search_staff_after_remove(enterprise_id)
        assert_equal('自动化测试', r.get('content').get('enterpriseStaffDetailDTOs').get('recordList')[0].get('staffName'),
                     "查询员工姓名用例通过", te="张红彦")

    def test_del_user(self):
        r = del_user(staff_id_from_remove)
        assert_equal(1, r.get('state'), "删除员工成功", te="张红彦")
