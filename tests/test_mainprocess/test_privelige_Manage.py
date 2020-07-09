import time
import pytest

from api_script.business.priveligeManage import queryPriveligeAcount, reAssignRole, queryManagerPriveligeInfo, \
    reAssignPrivelige, queryPriveligeAssignInfo
from api_script.business.colleague import addColleague
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import remove_member_company, recruiter_members
from utils.util import login, assert_not_in, loger, assert_equal, assert_in, wait, assert_not_equal, login_password


@pytest.mark.incremental
class TestPriveligeManage(object):

    # 添加同事为普通账号
    def test_add_free_colleague(self, login_0012020010425, get_add_colleague_user, get_user_id):
        global add_result, managerId
        managerId = get_user_id
        r = addColleague(phone=get_add_colleague_user, managerId=managerId, accountType='NORMAL')
        add_result = r.get('content').get('data').get('info')
        assert_equal(1, r.get('state'), '校验添加同事接口返回状态通过', te='Anan')
        assert_not_in('errorCode', add_result, '校验添加同事为普通账号通过', te='Anan')

    # 将上面添加的普通账号从公司移出
    def test_add_free_colleague_remove(self):
        global remove_userid
        remove_userid = add_result.get('userId')
        loger.info(f'添加同事的普通用户的用户id:{remove_userid}')
        remove_result = remove_member_company(removeUserId=remove_userid)
        '''print(remove_state)'''
        assert_equal(1, remove_result.get('state'), '校验移除添加的普通账号接口调用通过', te='Anan')
        assert_equal("操作成功", remove_result.get('message'), '校验移除添加的普通账号通过', te='Anan')

    # 验证移除普通帐号后，不在公司成员的已开通招聘服务列表中
    def test_free_not_in_members(self):
        result = recruiter_members().get('content').get('data').get('members').get('result')
        userIds = [str(user_info.get('userId')) for user_info in result]
        assert_not_in(remove_userid, userIds, '添加的普通帐号不在当前公司完成招聘者审核的员工里', te='Anan')

    # 添加同事为特权账号
    def test_add_pay_colleague(self, get_add_colleague_user_pay):
        global add_pay_result
        '''add_managerId = admin_user_id'''
        r = addColleague(phone=get_add_colleague_user_pay, managerId=managerId, accountType='PAY_PRIVILEGE')
        '''print(add_result)'''
        add_pay_result = r.get('content').get('data').get('info')
        assert_equal(1, r.get('state'), '校验添加同事接口返回状态通过', te='Anan')
        assert_not_in('errorCode', add_pay_result, '校验添加同事为特权账号通过', te='Anan')
        loger.info(f'添加的特权账号的用户id:{add_pay_result.get("userId")}')

    # 查找特权账号列表中是否有刚才添加的特权账号
    def test_search_pay_colleague(self, get_add_colleague_user_pay):
        global pay_userid
        pay_userid = add_pay_result.get('userId')
        for i in range(5):
            time.sleep(2)
            search_result = queryPriveligeAcount(keyword=get_add_colleague_user_pay)
            if search_result != []:
                break
        assert_not_equal([], search_result, '校验特权账号列表返回数据不为空通过', te='Anan')
        assert_equal(pay_userid, search_result[0].get('userid'), '校验特权账号列表返回了刚才添加的特权账号通过', te='Anan')

    # 调整刚才添加的特权账号为高级管理员
    def test_change_pay_role(self):
        message = reAssignRole(userId=pay_userid, accountRole='PAY_SENIOR')
        assert_equal('调整成功', message, '校验特权账号调整为高级管理员通过', te='Anan')

    # 验证调整弹框中数据返回成功
    def test_assign_correct(self):
        global assign_response
        assign_response = queryPriveligeAssignInfo(userid=pay_userid)
        assert_equal('查询成功', assign_response.get('message'), '校验调整弹框数据返回通过', te='Anan')

    # 分配给高级管理员所有特权账号
    def test_assign_subaccount_num(self):
        ManagerPriveligeInfo = queryManagerPriveligeInfo().get('content').get('data').get('managerPriveligeInfo')
        assert_equal('查询成功', queryManagerPriveligeInfo().get('message'), '校验获取管理员剩余特权账号通过', te='Anan')

        message = reAssignPrivelige(baseGoodsId=614,
                                    reAssignNum=ManagerPriveligeInfo.get('remainSubAccountNum'),
                                    userid=pay_userid,
                                    username=assign_response.get('content').get('data').get('userName'),
                                    info=assign_response.get('content').get('data').get('info'))
        assert_equal('调整成功', message, '校验分配给高级管理员所有特权账号通过', te='Anan')

        new_remainSubAccountNum = queryManagerPriveligeInfo().get('content').get('data').get(
            'managerPriveligeInfo').get('remainSubAccountNum')
        assert_equal(0, new_remainSubAccountNum, '校验超级管理员剩余特权账号为0，分配给高级管理员所有特权账号通过', te='Anan')

    # 无特权账号剩余情况下，添加同事为特权账号应该是不成功
    def test_add_pay_colleague_false(self, get_add_colleague_user):
        '''add_managerId = admin_user_id'''
        r = addColleague(phone=get_add_colleague_user, managerId=managerId, accountType='PAY_PRIVILEGE')
        '''print(add_result)'''
        assert_equal(1, r.get('state'), '校验无特权账号剩余，添加同事接口返回状态通过', te='Anan')
        assert_in('errorCode', r.get('content').get('data').get('info'), '校验无特权账号剩余，添加同事为特权账号失败通过', te='Anan')

    # 将上面添加特权账号从公司移出
    def test_add_pay_colleague_remove(self):
        loger.info(f'添加同事的特权用户的用户id:{pay_userid}')
        remove_pay_result = remove_member_company(removeUserId=pay_userid)
        '''print(remove_state)'''
        assert_equal(1, remove_pay_result.get('state'), '校验移除添加的特权账号通过', te='Anan')
        assert_equal("操作成功", remove_pay_result.get('message'), '校验移除添加的特权账号接口调用通过', te='Anan')

    # 验证移除特权帐号后，不在公司成员的已开通招聘服务列表中
    def test_pay_not_in_members(self):
        result = recruiter_members().get('content').get('data').get('members').get('result')
        userIds = [str(user_info.get('userId')) for user_info in result]
        assert_not_in(pay_userid, userIds, '添加的特权帐号不在当前公司完成招聘者审核的员工里', te='Anan')
