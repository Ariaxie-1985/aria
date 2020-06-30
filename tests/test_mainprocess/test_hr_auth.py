# coding:utf-8
# @Time  : 2020-06-11 16:45
# @Author: Xiawang
# Description:认证前hr可发职位，使用在职证明+手持身份证方式可以成功提交认证,通过后有一个提审前发布的职位是在线状态
#管理员协助通过招聘审核流程

import time

import pytest
import json

from api_script.jianzhao_web.b_basic.admin_review import admin_review
from api_script.jianzhao_web.b_basic.b_upload import upload_incumbency_certification
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import saveHR, add_saveCompany, submit_new, remove_member, \
    close_trial_package, remove_member_has_offline_position
from api_script.jianzhao_web.b_position.B_postposition import createPosition_999, get_online_positions, offline_position
from api_script.jianzhao_web.talent.unauth_positon_talent_rec import talent_rec_unAuth
from api_script.neirong_app.account import upate_user_password
from tests.test_B_enter.conftest import get_positionType

from utils.loggers import logers
from utils.util import assert_equal, assert_in, pc_send_register_verifyCode, verify_code_message, user_register_lagou, \
    login_password

loger = logers()

@pytest.mark.incremental
class TestHRAuth(object):

    def test_send_register_hr1_verify_code(self, get_country_code_phone_user):
        global hr1_countryCode, hr1_phone, hr1_user_name, register_state
        hr1_countryCode, hr1_phone, hr1_user_name = get_country_code_phone_user
        loger.info(f'B端入驻hr1手机号:{hr1_phone}')
        register_state = pc_send_register_verifyCode(hr1_countryCode, hr1_phone)
        assert_equal(1, register_state, '获取验证码成功', f'失败手机号:{hr1_countryCode + hr1_phone}')

    def test_get_hr1_verify_code(self):
        global verify_code
        verify_code = verify_code_message(hr1_countryCode, hr1_phone)
        assert_equal(True, bool(verify_code), '获取验证码成功')

    def test_register_admin_user(self):
        global register_state
        register = user_register_lagou(hr1_countryCode, hr1_phone, verify_code)
        register_state = register.get('state', 0)
        assert_equal(1, register_state, '校验hr1注册成功', '失败手机号:{}'.format(hr1_countryCode + hr1_phone))

    @pytest.mark.parametrize('newPassword', [('990eb670f81e82f546cfaaae1587279a')])
    def test_update_hr1_password(self, newPassword):
        r = upate_user_password(newPassword)
        assert_equal(1, r['state'], 'hr1修改密码成功')

    @pytest.mark.parametrize('companyFullName,resumeReceiveEmail,userPosition',[('拉勾测试自动化公司00911111111111','foxtang01@lagou.com','测试工程师')])
    def test_save_hr1_info(self,companyFullName,resumeReceiveEmail,userPosition):
        personal_info_save = saveHR(companyFullName, hr1_user_name, resumeReceiveEmail,userPosition)
        assert_equal(1, personal_info_save.get('state', 0), '校验hr基本信息是否保存成功')

    def test_hr1_join_company(self):
        join_company = add_saveCompany()
        assert_equal(1, join_company.get('state', 0), '验证hr1加入公司是否成功')

    def test_unAuthhr_create_position(self, get_positionType):
        r = createPosition_999(firstType=get_positionType[0], positionType=get_positionType[1],
                               positionThirdType=get_positionType[2],
                               positionName=get_positionType[3])
        assert_equal(1, r.get('state', 0), '验证未过审hr1发布职位成功')
        global unAuth_positionId
        unAuth_positionId = r['content']['data']['parentPositionInfo']['positionChannelInfoList'][0]['positionId']

    def test_unAuth_position_rec(self):
        r = talent_rec_unAuth(unAuth_positionId)
        #这里不判断人才数量了，由于业务逻辑限制，不适合频繁推真正的人才出来
        assert_equal(1,r.get('state',0),'验证未发布职位推荐人才简历接口访问成功')

    def test_hr1_upload_incumbency_certification(self):
        r = upload_incumbency_certification()
        assert_equal(1,r.get('state',0),'上传在职证明成功')

    def test_hr1_certificate(self):
        personal_certificate_submit = submit_new()
        assert_equal(1, personal_certificate_submit['state'], '验证提交招聘者身份审核是否成功')

    def test_unAuth_position_online(self):
        positions_result = get_online_positions()
        positionIds = []
        for positions in positions_result['content']['data']['parentPositionVOs']:
            actually_positionId = positions['positions'][0]['positionId']
            positionIds.append(actually_positionId)
        assert_equal(True, unAuth_positionId in positionIds, '验证过审前发的职位过审后在线')

    def test_offline_unAuth_position(self):
        r = offline_position(positionId=unAuth_positionId)
        assert_equal(1, r.get('state', 0), '验证过审前发的职位，过审后可以下线成功')
        time.sleep(1)
    
    def test_remove_hr1(self, get_user_info, get_password):
        global hr1Id, easy_company_id, www_company_id
        hr1Id, easy_company_id, www_company_id = get_user_info
        loger.info(f'B端入驻普通用户2用户的id:{hr1Id}, 主站公司id:{www_company_id}')
        remove_result = remove_member_has_offline_position(hr1Id)
        if not remove_result:
            close_trial_package(www_company_id)
            login_password(hr1_countryCode + hr1_phone, get_password)
            remove_result = remove_member_has_offline_position(hr1Id)
        assert_equal(True, remove_result, '验证hr1解除招聘服务成功')

    @pytest.mark.parametrize('companyFullName,resumeReceiveEmail,userPosition',[('拉勾测试自动化公司00911111111112','foxtang01@lagou.com','测试工程师')])
    def test_save_hr1_info02(self,companyFullName,resumeReceiveEmail,userPosition):
        personal_info_save = saveHR(companyFullName, hr1_user_name, resumeReceiveEmail,userPosition)
        assert_equal(1, personal_info_save.get('state', 0), '验证hr基本信息保存成功')

    def test_hr1_join_company02(self):
        join_company = add_saveCompany()
        assert_equal(1, join_company.get('state', 0), '验证加入公司是否成功')

    @pytest.mark.parametrize('companyFullName,resumeReceiveEmail,userPosition',[('拉勾测试自动化公司00911111111111','foxtang01@lagou.com','测试工程师')])
    def test_save_hr1_info03(self,companyFullName,resumeReceiveEmail,userPosition):
        personal_info_save = saveHR(companyFullName, hr1_user_name, resumeReceiveEmail,userPosition)
        assert_equal(1, personal_info_save.get('state', 0), '验证hr1基本信息保存成功')

    def test_hr1_join_company03(self):
        join_company = add_saveCompany()
        assert_equal(1, join_company.get('state', 0), '验证更换公司加入成功')

    def test_manager_assist(self):
        login_password('00911111111111','c47eeb69fa4e64971fb29cb1e9163a19')
        r = admin_review(hr1Id)
        assert_equal(1,r.get('state',0),'验证管理员协助通过审核成功')

    def test_hr1_company(self,get_password,get_user_info):
        login_password(hr1_countryCode + hr1_phone, get_password)
        hr1Id, easy_company_id, www_company_id = get_user_info
        assert_equal(True,bool(easy_company_id == '783664'),'验证当前公司是更换公司之后的所属公司')

    def test_hr1_publish_free_position(self,get_positionType):
        r = createPosition_999(firstType=get_positionType[0], positionType=get_positionType[1],
                               positionThirdType=get_positionType[2],
                               positionName=get_positionType[3])
        assert_equal(1, r.get('state', 0), '免费公司发布一个职位成功')
        global free_positionId, free_parentPositionId
        free_positionId = r['content']['data']['parentPositionInfo']['positionChannelInfoList'][0]['positionId']
        free_parentPositionId = r['content']['data']['parentPositionInfo']['parentPositionId']

    def test_hr1_free_position_is_in_online_position(self):
        positions_result = get_online_positions()
        positionIds = []
        for positions in positions_result['content']['data']['parentPositionVOs']:
            actually_positionId = positions['positions'][0]['positionId']
            positionIds.append(actually_positionId)
        assert_equal(True, free_positionId in positionIds, '验证在线列表里有刚才发布的普通职位')

    def test_hr1_offline_free_position(self):
        offline_result = offline_position(positionId=free_positionId)
        assert_equal(1, offline_result.get('state', 0), '校验下线免费职位是否成功！')







