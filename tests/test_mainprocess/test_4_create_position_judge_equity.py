# coding:utf-8
# @Time  : 2019-11-07 14:44
# @Author: Xiawang
# Description:
import datetime
import random
from api_script.business.new_lagouPlus import open_product
from api_script.home.data_import import import_linkManInfo, import_contacts
from api_script.jianzhao_web.b_position.B_postposition import createPosition_999, get_online_positions, \
    offline_position, www_redirect_easy
from utils.util import assert_equal, login_password


def test_get_admin_user_info(get_user_info):
    global admin_user_id, admin_lg_company_id
    admin_user_id, admin_company_id, admin_lg_company_id = get_user_info[0], get_user_info[1], get_user_info[2]
    assert_equal(True, bool(admin_user_id), '获取用户ID是否成功')


def test_free_company_create_position_person_and_company_enough_equity(get_positionType):
    r = createPosition_999(firstType=get_positionType[0], positionType=get_positionType[1],
                           positionThirdType=get_positionType[2],
                           positionName=get_positionType[3])
    assert_equal(1, r['state'], '免费公司发布一个职位成功')
    global free_positionId
    free_positionId = r['content']['data']['parentPositionInfo']['positionChannelInfoList'][0]['positionId']


def test_free_position_is_in_online_position():
    positions_result = get_online_positions()
    positionIds = []
    for positions in positions_result['content']['data']['parentPositionVOs']:
        actually_positionId = positions['positions'][0]['positionId']
        positionIds.append(actually_positionId)
    assert_equal(True, free_positionId in positionIds, '校验获取发布的职位是否在线职位是否成功！')


def test_login_home():
    # 线上home后台的用户账号和密码, 勿动
    r = login_password('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
    assert_equal(1, r['state'], '校验登录home成功！')


def test_buy_paid_package():
    contractNo = 'lagou-autotest-{}-{}'.format(str(datetime.date.today()), str(random.randint(1, 99)))
    r1 = import_linkManInfo(admin_lg_company_id, contractNo)
    if not r1.get('success', False):
        login_password('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
        r1 = import_linkManInfo(admin_lg_company_id, contractNo)
        assert_equal(True, r1['success'], "导入公司联系人信息成功！")
    r2 = import_contacts(admin_lg_company_id, contractNo)
    assert_equal(True, r2['success'], "导入合同信息成功！")
    r3 = open_product(templateId=79, companyId=admin_lg_company_id, contractNo=contractNo, userId=admin_user_id,
                      startTimeStr=str(datetime.date.today()),
                      endTimeStr=str(datetime.date.today() + datetime.timedelta(days=366)))
    assert_equal(True, r3['success'], "开通付费套餐成功！")


def test_login_admin_user(get_countryCode_phone_admin_user, get_password):
    global admin_countryCode, admin_phone, admin_user_name
    admin_countryCode, admin_phone, admin_user_name = get_countryCode_phone_admin_user[0], \
                                                      get_countryCode_phone_admin_user[1], \
                                                      get_countryCode_phone_admin_user[2]
    login_result = login_password(admin_countryCode + admin_phone, get_password)
    assert_equal(1, login_result['state'], '校验管理员登录是否成功')
    www_redirect_easy()


def test_paid_company_create_position_person_and_company_enough_equity(get_positionType):
    r = createPosition_999(firstType=get_positionType[0], positionType=get_positionType[1],
                           positionThirdType=get_positionType[2],
                           positionName=get_positionType[3])
    assert_equal(1, r['state'], '付费公司发布职位成功')
    global paid_positionId
    paid_positionId = r['content']['data']['parentPositionInfo']['positionChannelInfoList'][0]['positionId']


def test_paid_position_is_in_online_position():
    positions_result = get_online_positions()
    positionIds = []
    for positions in positions_result['content']['data']['parentPositionVOs']:
        actually_positionId = positions['positions'][0]['positionId']
        positionIds.append(actually_positionId)
    assert_equal(True, paid_positionId in positionIds, '校验获取发布的职位是否在线职位是否成功！')


def test_offline_free_position():
    offline_result = offline_position(positionId=free_positionId)
    assert_equal(1, offline_result['state'], '校验下线免费职位是否成功！')


def test_offline_paid_position():
    offline_result = offline_position(positionId=paid_positionId)
    assert_equal(1, offline_result['state'], '校验下线付费职位是否成功！')
