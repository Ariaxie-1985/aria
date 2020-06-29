# coding:utf-8
# @Time  : 2020-06-11 16:45
# @Author: Xiawang
# Description:认证前hr可发职位，使用在职证明+手持身份证方式可以成功提交认证,通过后有一个提审前发布的职位是在线状态

import time

import pytest
import json

from api_script.jianzhao_web.b_basic.b_upload import upload_incumbency_certification
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import saveHR, add_saveCompany, submit_new
from api_script.jianzhao_web.b_position.B_postposition import createPosition_999, get_online_positions

from utils.loggers import logers
from utils.util import assert_equal, assert_in, pc_send_register_verifyCode, verify_code_message, user_register_lagou

loger = logers()


@pytest.mark.incremental
class TestHRAuth(object):

    def test_send_register_hr1_verify_code(self, get_country_code_phone_user):
        global hr1_countryCode, hr1_phone, hr1_user_name, register_state
        hr1_countryCode, hr1_phone, hr1_user_name = get_country_code_phone_user
        loger.info(f'B端入驻hr1手机号:{hr1_phone}')
        register_state = pc_send_register_verifyCode(hr1_countryCode, hr1_phone)
        assert_equal(1, register_state, '获取验证码成功', f'失败手机号:{hr1_countryCode + hr1_phone}', te='唐欣洁')

    def test_get_hr1_verify_code(self):
        global verify_code
        verify_code = verify_code_message(hr1_countryCode, hr1_phone)
        assert_equal(True, bool(verify_code), '获取验证码成功', te='唐欣洁')

    def test_register_admin_user(self):
        global register_state
        register = user_register_lagou(hr1_countryCode, hr1_phone, verify_code)
        register_state = register.get('state', 0)
        assert_equal(1, register_state, '校验hr1注册成功', '失败手机号:{}'.format(hr1_countryCode + hr1_phone), te='唐欣洁')

    def test_save_general_hr1_info(self):
        personal_info_save = saveHR('拉勾测试自动化公司00911111111111', hr1_user_name, 'foxtang01@lagou.com', '测试工程师')
        assert_equal(1, personal_info_save.get('state', 0), '校验hr基本信息是否保存成功', te='唐欣洁')

    def test_general_user_1_join_company(self):
        join_company = add_saveCompany()
        assert_equal(1, join_company.get('state', 0), '验证加入公司是否成功', te='唐欣洁')

    def test_unAuthhr_create_position(self, get_positionType):
        r = createPosition_999(firstType=get_positionType[0], positionType=get_positionType[1],
                               positionThirdType=get_positionType[2],
                               positionName=get_positionType[3])
        assert_equal(1, r.get('state', 0), '验证未过审hr1发布职位成功', te='唐欣洁')
        global unAuth_positionId
        unAuth_positionId = r['content']['data']['parentPositionInfo']['positionChannelInfoList'][0]['positionId']

    def test_hr1_upload_incumbency_certification(self):
        r = upload_incumbency_certification()
        assert_equal(1, r.get('state', 0), '上传在职证明成功', te='唐欣洁')

    def test_hr1_certificate(self):
        personal_certificate_submit = submit_new()
        assert_equal(1, personal_certificate_submit['state'], '验证提交招聘者身份审核是否成功', te='唐欣洁')

    def test_unAuth_position_online(self):
        positions_result = get_online_positions()
        positionIds = []
        for positions in positions_result['content']['data']['parentPositionVOs']:
            actually_positionId = positions['positions'][0]['positionId']
            positionIds.append(actually_positionId)
        assert_equal(True, unAuth_positionId in positionIds, '验证过审前发的职位过审后在线', te='唐欣洁')
