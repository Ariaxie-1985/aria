# coding:utf-8
# @Time  : 2020/4/29 14:12
# @Author: Xiawang
# Description:
import time

import pytest

from api_script.jianzhao_web.dashboard import getEasyPlusPrivilegeCount
from api_script.jianzhao_web.im import greeting_list, multiChannel_default_invite, im_session_list, \
    session_batchCreate_cUserIds
from api_script.jianzhao_web.index import hr_jump_easy_index_html
from api_script.jianzhao_web.invitation import group_invite_code, invitation_join_company, join_with_user
from api_script.jianzhao_web.task_center import get_newer_task, receive_newer_task_reward, \
    receive_gouyin_weekly_task_points
from api_script.zhaopin_app.rights import get_rights_info_list
from api_script.zhaopin_app.shop import get_shop_goods_on_sale_goods, get_shop_goods_sell_goods, create_shop_goodsOrder, \
    pay_shop_goodsOrder, check_shop_goodsOrder
from utils.util import assert_equal, login_password, user_register_lagou, pc_send_register_verifyCode, \
    verify_code_message

im_chat_number = 15
im_chat_number_gray_scale = 50


def test_login_admin_user_01():
    login_result = login_password('19910626899', '9062e77da243687c68bf9665727b5c01')
    assert_equal(1, login_result['state'], '校验管理员登录是否成功')


def test_get_admin_user_info(get_user_info):
    global admin_user_id, admin_lg_company_id
    admin_user_id, admin_company_id, admin_lg_company_id = get_user_info
    assert_equal(True, bool(admin_user_id), '获取用户ID是否成功')


def test_group_invite_code():
    r = group_invite_code()
    global user, invite_code
    for k, v in r['content']['data'].items():
        user = k
        invite_code = v


def test_send_general_user_register_verify_code(get_countryCode_phone_general_user):
    global general_countryCode, general_phone, general_user_name, general_user_register_state
    general_countryCode, general_phone, general_user_name = get_countryCode_phone_general_user
    general_user_register_state = pc_send_register_verifyCode(general_countryCode, general_phone)
    assert_equal(1, general_user_register_state, '获取验证码成功', f'失败手机号:{general_countryCode + general_phone}')


def test_get_verify_general_user_code():
    global general_user_verify_code
    general_user_verify_code = verify_code_message(general_countryCode, general_phone)
    assert_equal(True, bool(general_user_verify_code), '获取验证码用例通过')


def test_register_general_user():
    global general_user_register_state
    register = user_register_lagou(general_countryCode, general_phone, general_user_verify_code)
    general_user_register_state = register.get('state', 0)
    assert_equal(1, general_user_register_state, '普通用户注册成功用例通过！',
                 '失败手机号:{}'.format(general_countryCode + general_phone))


def test_hr_jump_easy_index_html():
    time.sleep(1)
    hr_jump_easy_index_html()


def test_invitation_join_company():
    global userIdPasscode
    userIdPasscode = invitation_join_company(user=user, invite_code=invite_code)
    assert_equal(True, bool(userIdPasscode), '加入公司页面页面加载成功用例通过')


def test_join_with_user():
    r = join_with_user(userIdPasscode=userIdPasscode, invite_code=invite_code)
    assert_equal(True, bool(r), '确定加入公司用例通过')


def test_getEasyPlusPrivilegeCount():
    r = getEasyPlusPrivilegeCount()
    managerId = r['content']['data']['managerId']
    assert_equal(managerId, admin_user_id, f'用户{general_phone}加入公司成功')


def test_get_rights_info_list():
    r = get_rights_info_list()
    assert_equal(False, bool(r.get('content', True)), '验证免费账号的普通权益通过')


def test_im_session_list_check_15():
    r = im_session_list(createBy=0)
    assert_equal(15, r['content']['data']['remainConversationTimes'], '沟通点数计算15用例通过')
