import datetime
import random
import time
import pytest
from api_script.business.new_lagouPlus import open_product

from api_script.home.audit import query_risk_labels, add_risk_labels_by_company, queryRiskLabelsByCompany
from api_script.home.data_import import import_linkManInfo, import_contacts
from api_script.home.lagou_plus import get_contract_list, close_contract
from api_script.is_debug_login import debugSelfCheck
from api_script.jianzhao_web.b_basic.company import jump_html
from api_script.jianzhao_web.b_basic.toB_comleteInfo_3 import completeInfo, company_auth
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import saveHR, saveCompany, \
    submit_new, add_saveCompany, remove_member, recruiter_members
from api_script.jianzhao_web.b_basic.b_upload import upload_permit
from api_script.jianzhao_web.b_position.B_postposition import createPosition_999, get_online_positions, \
    www_redirect_easy, offline_position, update_Position_pc, republish_position_pc
from api_script.jianzhao_web.im import im_session_list, greeting_list, multiChannel_default_invite, \
    session_batchCreate_cUserIds
from api_script.jianzhao_web.index import hr_jump_easy_index_html, jump_easy_index_html
from api_script.jianzhao_web.invitation import group_invite_code, join_with_user, invitation_join_company
from api_script.jianzhao_web.task_center import get_newer_task, receive_newer_task_reward, \
    receive_gouyin_weekly_task_points
from api_script.neirong_app.account import upate_user_password
from api_script.zhaopin_app.rights import get_rights_info_list
from api_script.zhaopin_app.shop import get_shop_goods_on_sale_goods, get_shop_goods_sell_goods, create_shop_goodsOrder, \
    pay_shop_goodsOrder, check_shop_goodsOrder
from utils.loggers import logers
from utils.util import assert_equal, pc_send_register_verifyCode, verify_code_message, user_register_lagou, \
    login_password, assert_in, login_home

loger = logers()


@pytest.mark.incremental
class TestCompanyBusiness(object):
    im_chat_number = 15
    im_chat_number_gray_scale = 50
    contractNo = f'LAGOU-AUTOTEST-{int(time.time())}-{random.randint(1, 99999)}'

    def test_is_debug_api(self):
        r = debugSelfCheck()
        assert_equal('成功', r.get('message'), '极光DeBug_API校验成功', '极光DeBug_API失败', te='foxtang')

    def test_send_register_admin_verify_code(self, get_country_code_phone_user):
        global admin_countryCode, admin_phone, admin_user_name
        admin_countryCode, admin_phone, admin_user_name = get_country_code_phone_user
        loger.info(f'B端入驻管理员手机号:{admin_phone},B端入驻管理name:{admin_user_name}')
        register_state = pc_send_register_verifyCode(admin_countryCode, admin_phone)
        assert_equal(expect_value=1, actual_value=register_state, success_message='获取验证码成功',
                     fail_message=f'失败手机号:{admin_countryCode + admin_phone}', te='王洋')

    def test_get_admin_verify_code(self):
        global verify_code
        verify_code = verify_code_message(admin_countryCode, admin_phone)
        assert_equal(True, bool(verify_code), '获取验证码成功', te='王洋')

    def test_register_admin_user(self):
        global register_state
        register = user_register_lagou(admin_countryCode, admin_phone, verify_code)
        register_state = register.get('state', 0)
        assert_equal(1, register_state, '校验管理员注册是否成功！', te='王洋',
                     fail_message='失败手机号:{}'.format(admin_countryCode + admin_phone))

    def test_save_admin_user_info(self, get_company_name):
        personal_msg_save = saveHR(get_company_name, admin_user_name, 'foxtang@lagou.com')
        assert_equal(1, personal_msg_save.get('state', 0), "校验HR信息是否保存成功", te='foxtang')

    def test_timewait(self):
        time.sleep(5)

    def test_create_company_info(self, get_company_name):
        company_msg_save = saveCompany(get_company_name)
        assert_equal(1, company_msg_save.get('state', 0), "校验公司是否新建成功", te='foxtang')

    #线上此需求已下线，注销无用的用例
    # def test_admin_jump_html(self):
    #     save_result = jump_html()
    #     assert_equal(1, save_result.get('state', 0), '校验是否跳过选择优质简历', te='foxtang')

    def test_admin_upload_permit(self):
        upload_p = upload_permit()
        assert_equal(1, upload_p.get('state', 0), "校验提交身份信息是否成功", te='foxtang')

    def test_admin_personal_certificate(self):
        personal_certificate_submit = submit_new()
        assert_equal(1, personal_certificate_submit.get('state', 0), "校验提交招聘者身份审核是否成功", te='foxtang')

    def test_(self):
        time.sleep(1)

    def test_get_admin_user_info(self, get_user_info):
        global admin_user_id, www_company_id, easy_company_id, admin_user_name
        admin_user_id, easy_company_id, www_company_id, admin_user_name = get_user_info
        loger.info(f'B端入驻管理员用户id:{admin_user_id}, 简招公司id:{easy_company_id}, 主站公司id:{www_company_id}, 管理员name:{admin_user_name}')
        assert_equal(True, bool(admin_user_id), '获取用户ID是否成功', te='foxtang')

    def test_get_admin_rights_info_list(self):
        r = get_rights_info_list()
        for base_detail in r['content']['baseDetailResList']:
            if www_company_id[-1] not in ('0', '1', '2'):
                if base_detail['baseGoodsId'] == 623:
                    assert_equal(1, base_detail['totalNum'], '验证普通职位总数1个通过', te='安菁宵')
                if base_detail['baseGoodsId'] == 201:
                    assert_equal(self.im_chat_number, base_detail['totalNum'], '验证沟通点数总数15个通过', te='安菁宵')
            else:
                if base_detail['baseGoodsId'] == 623:
                    assert_equal(3, base_detail['totalNum'], '验证木桶计划灰度公司主站ID尾号为0,1,2的免费用户的普通职位总数3个通过', te='安菁宵')
                if base_detail['baseGoodsId'] == 201:
                    assert_equal(self.im_chat_number_gray_scale, base_detail['totalNum'], '验证沟通点数总数50个通过', te='安菁宵')
        assert_equal(True, bool(r['content']['baseDetailResList']), '验证免费账号的普通权益通过', te='安菁宵')

    def test_group_invite_code(self):
        r = group_invite_code()
        loger.info(f'获取邀请码:{r.get("content")}')
        assert_equal(1, r.get('state', 0), '获取邀请码成功', te='foxtang')
        global user, invite_code
        for k, v in r['content']['data'].items():
            user = k
            invite_code = v

    @pytest.mark.parametrize('newPassword', [('990eb670f81e82f546cfaaae1587279a')])
    def test_update_admin_user(self, newPassword):
        r = upate_user_password(newPassword)
        assert_equal(1, r['state'], '管理员修改密码成功', te='王洋')

    def test_send_general_user_register_verify_code_01(self, get_country_code_phone_user):
        global general_country_code_01, general_phone_01
        general_country_code_01, general_phone_01, general_user_name_01 = get_country_code_phone_user
        loger.info(f'B端入驻普通用户手机号:{general_phone_01},B端入驻普通用户name:{admin_user_name}')
        general_user_register_state = pc_send_register_verifyCode(general_country_code_01, general_phone_01)
        assert_equal(expect_value=1, actual_value=general_user_register_state, success_message='获取验证码成功',
                     fail_message=f'失败手机号:{general_country_code_01 + general_phone_01}',
                     te='王洋')

    def test_get_verify_general_user_code_01(self):
        global general_user_verify_code_01
        general_user_verify_code_01 = verify_code_message(general_country_code_01, general_phone_01)
        assert_equal(True, bool(general_user_verify_code_01), '获取验证码成功', te='王洋')

    def test_register_general_user_01(self):
        global general_user_register_state
        register = user_register_lagou(general_country_code_01, general_phone_01, general_user_verify_code_01)
        general_user_register_state = register.get('state', 0)
        assert_equal(expect_value=1, actual_value=general_user_register_state, success_message='校验普通用户注册是否成功！',
                     fail_message='失败手机号:{}'.format(general_country_code_01 + general_phone_01), te='王洋')

    def test_hr_jump_easy_index_html(self):
        time.sleep(1)
        hr_jump_easy_index_html()

    def test_invitation_join_company(self):
        global userIdPasscode
        userIdPasscode = invitation_join_company(user=user, invite_code=invite_code)
        assert_equal(True, bool(userIdPasscode), '加入公司页面页面加载成功用例通过', te='foxtang')

    def test_join_with_user(self):
        r = join_with_user(userIdPasscode=userIdPasscode, invite_code=invite_code)
        assert_equal(True, bool(r), '确定加入公司用例通过', te='foxtang')

    def test_get_general_user_01(self, get_easy_user_info):
        userId, UserCompanyId, lagou_company_id = get_easy_user_info
        loger.info(f'普通用户1的用户id:{userId}, 简招公司id:{UserCompanyId}, 拉勾公司id:{lagou_company_id}', te='foxtang')

    def test_get_online_position(self):
        positions_result = get_online_positions()
        assert_equal(1, positions_result.get('state'), '在线职位接口调用用例通过', te='foxtang')

    def test_get_general_user_rights_info_list(self):
        r = get_rights_info_list()
        assert_equal(False, bool(r.get('content', True)), '验证免费账号的普通权益通过', te='安菁宵')

    def test_general_user_im_session_list_check_15(self):
        r = im_session_list(createBy=0)
        assert_equal(self.im_chat_number, r['content']['data']['remainConversationTimes'],
                     f'沟通点数计算{self.im_chat_number}用例通过', te='foxtang')

    @pytest.mark.parametrize('newPassword', [('990eb670f81e82f546cfaaae1587279a')])
    def test_update_general_user_password(self, newPassword):
        r = upate_user_password(newPassword)
        assert_equal(1, r['state'], '普通用户修改密码成功', te='王洋')

    def test_login_admin_user_01(self, get_password):
        login_result = login_password(admin_countryCode + admin_phone, get_password)
        assert_equal(1, login_result['state'], '校验管理员登录是否成功', te='王洋')

    def test_company_auth(self):
        company_auth_result = company_auth()
        assert_equal(1, company_auth_result.get('state'), "校验申请认证公司是否成功", te='foxtang')

    def test_company_certification(self):
        complete_info = completeInfo()
        assert_equal(1, complete_info['state'], "校验公司认证是否成功", te='foxtang')

    def test_1(self):
        time.sleep(1)

    def test_free_company_create_position_person_and_company_enough_equity(self, get_positionType):
        r = createPosition_999(firstType=get_positionType[0], positionType=get_positionType[1],
                               positionThirdType=get_positionType[2],
                               positionName=get_positionType[3])
        assert_equal(1, r.get('state', 0), '免费公司发布一个职位成功', te='foxtang')
        global free_positionId, free_parentPositionId
        free_positionId = r['content']['data']['parentPositionInfo']['positionChannelInfoList'][0]['positionId']
        free_parentPositionId = r['content']['data']['parentPositionInfo']['parentPositionId']

    def test_free_position_is_in_online_position(self):
        positions_result = get_online_positions()
        positionIds = []
        for positions in positions_result['content']['data']['parentPositionVOs']:
            actually_positionId = positions['positions'][0]['positionId']
            positionIds.append(actually_positionId)
        assert_equal(True, free_positionId in positionIds, '校验获取发布的职位是否在线职位是否成功！', te='foxtang')

    def test_get_newer_task(self):
        r = get_newer_task()
        assert_equal(1, r.get('state'), '任务中心获取新手任务用例通过', te='安菁宵')
        global task_reward_info
        task_reward_info = []
        for task in r['data']:
            if task['statusName'] == 'COMPLETED':
                task_reward_info.append((task['id'], task['taskLabelName'], task['taskGroupName']))
        assert_equal(3, len(task_reward_info), '领取积分通过', te='安菁宵')

    def test_receive_newer_task_reward(self):
        for task in task_reward_info:
            r = receive_newer_task_reward(recordId=task[0], taskLabel=task[1], taskGroup=task[2])
            assert_equal(1, r['state'], '任务中心--新手任务--领取积分用例通过', te='安菁宵')

    def test_receive_gouyin_weekly_task_points(self):
        r = receive_gouyin_weekly_task_points()
        assert_equal(True, bool(r['data'] >= 300), '任务中心--获取本周积分超过300分成功', te='安菁宵')

    def test_get_shop_goods_on_sale_goods_IM_CHAT_NUMBER(self):
        r = get_shop_goods_on_sale_goods()
        assert_equal(1, r['state'], '道具商城--招聘道具--获取在售权益及其价格信息用例通过', te='安菁宵')
        global im_chat_number_sale
        im_chat_number_sale = r['content']['onSaleGoods']['IM_CHAT_NUMBER']

    def test_get_shop_goods_sell_goods(self):
        r = get_shop_goods_sell_goods(on_sale_goods_id=im_chat_number_sale)
        assert_equal(1, r['content']['status'], '购买沟通点数-前置条件用例通过', te='安菁宵')
        global sellGoodsPriceId, shopOrderToken
        shopOrderToken = r['content']['shopOrderToken']
        for sellGoodsPriceRes in r['content']['sellGoodsInfo']['sellGoodsStrategyResList'][0]['sellGoodsPriceResList']:
            if sellGoodsPriceRes['preferentialPolicyCurrencyNum'] == 300:
                sellGoodsPriceId = sellGoodsPriceRes['sellGoodsPriceId']
        assert_equal(True, bool(sellGoodsPriceId), "购买沟通点数的300积分条件通过", te='安菁宵')

    @pytest.mark.parametrize("payLagouBpNum,payLagouCoinNum", [(300, 0)])
    def test_create_shop_goodsOrder(self, payLagouBpNum, payLagouCoinNum):
        r = create_shop_goodsOrder(payLagouBpNum=payLagouBpNum, payLagouCoinNum=payLagouCoinNum,
                                   sellGoodsPriceId=sellGoodsPriceId, shopOrderToken=shopOrderToken)
        assert_equal(1, r['state'], '购买沟通点数用例通过', te='安菁宵')
        global orderNo
        if r['content']['orderState'] == 'CREATE':
            orderNo = r['content']['orderNo']

    def test_pay_shop_goodsOrder(self):
        time.sleep(2)
        r = pay_shop_goodsOrder(orderNo=orderNo)
        assert_equal(1, r['content']['status'], '道具商城--招聘道具--购买道具--支付订单用例通过', te='安菁宵')

    def test_check_shop_goodsOrder(self):
        time.sleep(2)
        r = check_shop_goodsOrder(orderNo=orderNo)
        assert_equal(1, r['content']['status'], '道具商城--招聘道具--购买道具--检查订单用例通过', te='安菁宵')

    def test_greeting_list(self, c_userId_0085220180917):
        r = greeting_list(cUserIds=c_userId_0085220180917, positionId=free_positionId)
        assert_equal(1, r['state'], '找人才-打招呼用例通过', te='foxtang')

    def test_multiChannel_default_invite(self):
        r = multiChannel_default_invite(free_positionId)
        assert_equal(1, r['state'], '职位邀请人才用例通过', te='foxtang')

    def test_im_session_list_check_20(self):
        r = im_session_list(createBy=0)
        self.im_chat_number += 5
        self.im_chat_number_gray_scale += 5
        if www_company_id[-1] not in ('0', '1', '2'):
            assert_equal(self.im_chat_number, r['content']['data']['remainConversationTimes'],
                         f'沟通点数计算{self.im_chat_number}用例通过', te='安菁宵')
        else:
            assert_equal(self.im_chat_number_gray_scale, r['content']['data']['remainConversationTimes'],
                         f'处于灰度计划的沟通点数计算{self.im_chat_number_gray_scale}用例通过', te='安菁宵')

    def test_session_batchCreate_cUserIds(self, c_userId_0085220180917):
        r = session_batchCreate_cUserIds(cUserIds=c_userId_0085220180917, positionId=free_positionId)
        try:
            sessionId_key = list(r['content']['data']['sessionIds'].keys())[0]
            sessionId_value = list(r['content']['data']['sessionIds'].values())[0]
        except IndexError:
            sessionId_key = 1
            sessionId_value = 0
        assert_equal(sessionId_key, sessionId_value, '创建会话用例通过', te='foxtang')

    def test_im_session_list_check_19(self):
        r = im_session_list(createBy=0)
        self.im_chat_number += 4
        self.im_chat_number_gray_scale += 4
        if www_company_id[-1] not in ('0', '1', '2'):
            assert_equal(self.im_chat_number, r['content']['data']['remainConversationTimes'],
                         f'沟通点数计算{self.im_chat_number}用例通过', te='安菁宵')
        else:
            assert_equal(self.im_chat_number_gray_scale, r['content']['data']['remainConversationTimes'],
                         f'处于灰度计划的沟通点数计算{self.im_chat_number_gray_scale}用例通过', te='安菁宵')

    def test_offline_free_position(self):
        offline_result = offline_position(positionId=free_positionId)
        assert_equal(1, offline_result.get('state', 0), '校验下线免费职位是否成功！', te='foxtang')

    def test_republish_free_position(self):
        r1 = republish_position_pc(free_parentPositionId)
        state = r1.get('state', 0)
        assert_equal(1, state, '验证普通职位再发布成功', te='唐欣洁')

    def test_offline_free_position02(self):
        offline_result = offline_position(positionId=free_positionId)
        assert_equal(1, offline_result.get('state', 0), '验证再发布成功的职位再次下线成功', te='foxtang')

    def test_login_home(self):
        # 线上home后台的用户账号和密码, 勿动
        r = login_password('autotest@lagou.com', 'a52f33ba89bd7af92982da737cafc8d0')
        assert_equal(1, r.get('state', 0), '校验登录home成功！', te='foxtang')


    def test_import_linkManInfo(self):
        r = import_linkManInfo(www_company_id, self.contractNo)
        assert_equal(expect_value=True, actual_value=r.get('success', False), success_message='导入公司联系人信息成功！',
                     fail_message=f'导入公司联系人信息失败,合同编号:{self.contractNo}', te='foxtang')

    def test_import_contacts(self):
        r = import_contacts(www_company_id, self.contractNo)
        assert_equal(expect_value=True, actual_value=r.get('success', False), success_message="导入合同信息成功！",
                     fail_message=f'导入公司合同信息失败,合同编号:{self.contractNo}', te='foxtang')

    def test_buy_paid_package(self):
        r = open_product(templateId=79, companyId=www_company_id, contractNo=self.contractNo, userId=admin_user_id,
                         startTimeStr=str(datetime.date.today()),
                         endTimeStr=str(datetime.date.today() + datetime.timedelta(days=366)))
        assert_equal(expect_value=True, actual_value=r.get('success', False), success_message="开通付费套餐成功！",
                     fail_message="公司主站id:{},用户id:{},合同编号:{}".format(www_company_id, admin_user_id, self.contractNo),
                     te='foxtang')

    def test_login_admin_user_02(self, get_password):
        login_result = login_password(admin_countryCode + admin_phone, get_password)
        assert_equal(1, login_result.get('state', 0), '校验管理员登录是否成功', te='王洋')
        www_redirect_easy()

    def test_paid_company_create_position_person_and_company_enough_equity(self, get_positionType):
        r = createPosition_999(firstType=get_positionType[0], positionType=get_positionType[1],
                               positionThirdType=get_positionType[2],
                               positionName=get_positionType[3])
        assert_equal(1, r.get('state', 0), '付费公司发布职位成功', te='foxtang')
        global paid_positionId
        global paid_parentPositionId
        paid_positionId = r['content']['data']['parentPositionInfo']['positionChannelInfoList'][0]['positionId']
        paid_parentPositionId = r['content']['data']['parentPositionInfo']['parentPositionId']

    def test_paid_position_is_in_online_position(self):
        positions_result = get_online_positions()
        positionIds = []
        for positions in positions_result['content']['data']['parentPositionVOs']:
            actually_positionId = positions['positions'][0]['positionId']
            positionIds.append(actually_positionId)
        assert_equal(True, paid_positionId in positionIds, '校验获取发布的职位是否在线职位是否成功！', te='foxtang')

    def test_update_position(self, get_positionType):
        r = update_Position_pc(firstType=get_positionType[0], positionType=get_positionType[1],
                               positionThirdType=get_positionType[2],
                               positionName=get_positionType[3], parentPositionId=paid_parentPositionId)
        assert_equal(1, r.get('state', 0), '编辑职位成功', te='foxtang')

    def test_update_positon_details(self):
        r = get_online_positions()
        salary = r['content']['data']['parentPositionVOs'][0]['parentPositionInfo']['salary']
        assert_equal('30k-50k', salary, '验证职位薪资更新成功', te='foxtang')

    def test_offline_paid_position(self):
        offline_result = offline_position(positionId=paid_positionId)
        assert_equal(1, offline_result.get('state', 0), '校验下线付费职位是否成功！', te='foxtang')

    def test_republish_paid_position(self):
        r1 = republish_position_pc(paid_parentPositionId)
        state = r1.get('state', 0)
        if state == 800:
            attachParam = r1['content']['data']['popUpTipsInfoVO']['buttons'][0]['attachParam']
            r2 = republish_position_pc(free_parentPositionId, attachParam)
            assert_equal(1, r2.get('state', 0), '非普通职位再发布成功', te='唐欣洁')
        else:
            assert_equal(1, state, '验证普通职位再发布成功', te='唐欣洁')

    def test_offline_paid_position02(self):
        offline_result = offline_position(positionId=paid_positionId)
        assert_equal(1, offline_result.get('state', 0), '验证再发布成功的职位再次下线成功！', te='foxtang')

    def test_jump_home(self):
        time.sleep(1)
        login_home('autotest@lagou.com', 'a52f33ba89bd7af92982da737cafc8d0')

    def test_query_risk_labels(self):
        r = query_risk_labels()
        assert_equal(True, r['success'], '查询风险标签用例通过', te='foxtang')
        global risk_label_id
        for risk_labels in r['data']:
            if risk_labels['type'] == 'A':
                risk_label_id = risk_labels['id']
                break

    def test_add_risk_labels_by_company(self):
        r = add_risk_labels_by_company(companyId=www_company_id, labelIds=risk_label_id)
        loger.info(f'{www_company_id}公司打风险标签是否成功:{r["success"]}')
        assert_equal(True, r['success'], '添加风险标签用例通过', te='foxtang')

    def test_queryRiskLabelsByCompany(self):
        time.sleep(5)
        r = queryRiskLabelsByCompany(companyId=www_company_id)
        loger.info(f'{www_company_id}公司的风险标签:{r["data"]}')
        risk_label = ['外包公司', '保险公司', '招聘公司']
        for label in r['data']:
            assert_in(label, risk_label, '公司获取风险标签用例通过', te='foxtang')

    def test_send_general_user_register_verify_code_02(self, get_country_code_phone_user):
        global general_country_code_02, general_phone_02, general_user_name_02
        general_country_code_02, general_phone_02, general_user_name_02 = get_country_code_phone_user
        loger.info(f'B端入驻普通用户2手机号:{general_phone_02}')
        general_user_register_state = pc_send_register_verifyCode(general_country_code_02, general_phone_02)
        assert_equal(expect_value=1, actual_value=general_user_register_state, success_message='获取验证码成功',
                     fail_message=f'失败手机号:{general_country_code_02 + general_phone_02}',
                     te='王洋')

    def test_get_verify_general_user_code_02(self):
        global general_user_verify_code_02
        general_user_verify_code_02 = verify_code_message(general_country_code_02, general_phone_02, )
        assert_equal(True, bool(general_user_verify_code_01), '获取验证码成功', te='王洋')

    def test_register_general_user_02(self):
        register = user_register_lagou(general_country_code_02, general_phone_02, general_user_verify_code_02)
        assert_equal(expect_value=1, actual_value=register.get('state', 0), success_message='校验普通用户注册是否成功！',
                     fail_message=f'失败手机号:{general_country_code_02 + general_phone_02}', te='王洋')

    def test_hr_jump_easy_index_html_02(self):
        time.sleep(1)
        hr_jump_easy_index_html()

    def test_save_general_user_02_info(self, get_company_name):
        personal_msg_save = saveHR(get_company_name, general_user_name_02, 'foxtang@lagou.com', '技术总监')
        assert_equal(1, personal_msg_save.get('state', 0), "校验技术总监信息是否保存成功", te='foxtang')

    def test_general_user_02_join_company(self):
        join_company = add_saveCompany()
        assert_equal(1, join_company.get('state', 0), "校验加入公司是否成功", te='foxtang')

    def test_general_user_02_jump_html(self):
        save_result = jump_html()
        assert_equal(1, save_result.get('state', 0), '校验是否跳过选择优质简历', te='foxtang')

    def test_general_user_02_upload_permit(self):
        upload_p = upload_permit()
        assert_equal(1, upload_p.get('state', 0), "校验提交身份信息是否成功", te='foxtang')

    def test_general_02_personal_certificate(self):
        personal_certificate_submit = submit_new()
        assert_equal(1, personal_certificate_submit.get('state', 0), "校验提交招聘者身份审核是否成功", te='foxtang')

    def test_jump_easy_index_html(self):
        jump_easy_index_html()

    def test_get_general_user_02(self, get_easy_user_info):
        userId, UserCompanyId, lagou_company_id = get_easy_user_info
        loger.info(f'普通用户2的用户id:{userId}, 简招公司id:{UserCompanyId}, 拉勾公司id:{lagou_company_id}')

    def test_get_general_user_02_rights_info_list(self):
        r = get_rights_info_list()
        assert_equal(1, r.get('state'), '获取用户的基础权益成功', '获取用户的基础权益失败', '安菁宵')
        for base_good in r['content']['baseDetailResList']:
            if base_good['baseGoodsId'] == 623:
                assert_equal(0, int(base_good['totalNum']), '验证特殊行业（一类）公司免费账号的普通职位数为0用例通过', te='安菁宵')

    def test_general_user_02_im_session_list_check_15(self):
        r = im_session_list(createBy=0)
        im_chat_num = r['content']['data']['remainConversationTimes']
        if www_company_id[-1] in ('0', '1', '2'):
            loger.info(f'主站公司id:{www_company_id},其沟通点数:{im_chat_num}')
        assert_equal(self.im_chat_number, im_chat_num,
                     f'沟通点数计算{self.im_chat_number}用例通过', te='安菁宵')

    def test_recruiter_members_general_user_02(self, get_user_info):
        global general_userId_02, www_company_id, general_user_name
        general_userId_02, easy_company_id, www_company_id, general_user_name = get_user_info
        r = recruiter_members()
        loger.info(f'flag:{r},当前用户:{general_userId_02}, 当前用户name: {general_user_name}')
        result = r.get('content', {}).get('data', {}).get('members', {}).get('result', [])
        assert_equal(2, len(result), '当前公司有两个开通招聘者服务的成员', te='foxtang')
        userIds = [str(user_info.get('userId')) for user_info in result]
        assert_in(general_userId_02, userIds, '普通用户在当前公司完成招聘者审核的员工里', '普通用户不在当前公司完成招聘者审核的员工里', 'foxtang')

    def test_remove_general_user_02(self):
        loger.info(f'flag:解除招聘者认证--普通用户2的用户id:{general_userId_02}, 主站公司id:{www_company_id}')
        remove_result = remove_member()
        assert_equal(1, remove_result.get('state'), '校验移除普通用户2的招聘者服务成功！', te='foxtang')

    def test_jump_home_01(self):
        time.sleep(1)
        login_home('autotest@lagou.com', 'a52f33ba89bd7af92982da737cafc8d0')

    def test_get_contract_list(self):
        time.sleep(1)
        r = get_contract_list(www_company_id)
        assert_equal(True, len(r.get('data').get('pageData')), '获取公司合同列表通过', f'未获取到公司{www_company_id}的合同', 'foxtang')
        contract_no = r.get('data').get('pageData')[0].get('number')
        assert_equal(self.contractNo, contract_no, '合同导入成功，在列表已查到', f'导入成功的合同{self.contractNo}未在列表查到', 'foxtang')

    def test_close_contract(self):
        time.sleep(1)
        r = close_contract(self.contractNo)
        assert_equal(True, r.get('success'), '关闭合同成功', f'关闭失败{self.contractNo}', 'foxtang')

    def test_login_admin_user_03(self, get_password):
        login_result = login_password(admin_countryCode + admin_phone, get_password)
        assert_equal(1, login_result['state'], '校验管理员登录是否成功', te='王洋')

    def test_recruiter_members_admin(self):
        r = recruiter_members()
        loger.info(f'flag:{r},当前用户:{admin_user_id}')
        result = r.get('content', {}).get('data', {}).get('members', {}).get('result', [])
        assert_equal(1, len(result), '公司仅有管理员在开通招聘者', te='foxtang')
        userIds = [str(user_info.get('userId')) for user_info in result]
        assert_in(admin_user_id, userIds, '管理员在当前公司完成招聘者审核的员工里', '管理员不在当前公司完成招聘者审核的员工里', 'foxtang')

    def test_remove_admin_user(self):
        loger.info(f'flag:解除招聘者认证--管理员的用户id:{admin_user_id}, 主站公司id:{www_company_id}')
        remove_result = remove_member()
        if remove_result.get('state') == 40309:
            loger.info(f"解除管理员的招聘者服务报错40309: 主站id:{www_company_id},管理员用户id:{admin_user_id},合同编号:{self.contractNo}")
        assert_equal(1, remove_result.get('state'), '校验移除管理员用户的招聘者服务成功！', te='foxtang')
