# coding:utf-8
# @Time  : 2019-11-07 14:44
# @Author: Xiawang
# Description:
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import get_b_index_Id
from api_script.jianzhao_web.b_position.B_postposition import createPosition_999, get_online_positions, \
    offline_position, www_redirect_easy
from utils.util import assert_equal


def test_login_admin_user(b_login_web,ip_port):
    assert_equal(1, b_login_web, '校验B端用户登录是否成功')
    www_redirect_easy(ip_port=ip_port)


def test_get_admin_user_info(ip_port):
    global admin_user_id, admin_lg_company_id
    admin_user_id, admin_company_id, admin_lg_company_id = get_b_index_Id()
    assert_equal(True, bool(admin_user_id), '获取用户ID是否成功')


def test_free_company_create_position_person_and_company_enough_equity(get_positionType, ip_port):
    r = createPosition_999(firstType=get_positionType[0], positionType=get_positionType[1],
                           positionThirdType=get_positionType[2],
                           positionName=get_positionType[3], ip_port=ip_port)
    assert_equal(1, r.get('state', 0), '公司发布一个职位成功')
    global free_positionId
    free_positionId = r['content']['data']['parentPositionInfo']['positionChannelInfoList'][0]['positionId']


def test_free_position_is_in_online_position(ip_port):
    positions_result = get_online_positions(ip_port=ip_port)
    positionIds = []
    for positions in positions_result['content']['data']['parentPositionVOs']:
        actually_positionId = positions['positions'][0]['positionId']
        positionIds.append(actually_positionId)
    assert_equal(True, free_positionId in positionIds, '校验获取发布的职位是否在线职位是否成功！')


def test_offline_free_position(ip_port):
    offline_result = offline_position(positionId=free_positionId, ip_port=ip_port)
    assert_equal(1, offline_result.get('state', 0), '校验下线免费职位是否成功！')
