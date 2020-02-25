# coding:utf-8
# @Time  : 2019-09-24 14:41
# @Author: Xiawang
# Description:
import logging

import pytest
from api_script.entry.account.passport import password_login
from api_script.entry.buser.hr_info import get_hr_info
from api_script.entry.deliver.deliver import deliver_check, get_resume_info, deliver_create
from api_script.entry.position.communicatePositions import get_jd
from api_script.zhaopin_app.b_position import get_online_positions, publish_position, positions_offline
from utils.util import assert_equal

r = password_login("19910626899", "000000")
assert_equal(1, r['state'], '校验登录成功、获取userToken成功！')
try:
    global userToken, positions_result
    userToken = r['content']['userToken']
    positions_result = get_online_positions(userToken=userToken, H9=True)
    flag = positions_result['content']['onlinePositionNum']
    offline_mark = pytest.mark.skipif(flag < 20, reason="发布职位权益足够，无需下线职位")
except Exception as e:
    logging.error(msg="获取在线职位报异常:{},用户\n".format(e))
    offline_mark = pytest.mark.skip(reason="发布职位权益足够，无需下线职位")


@offline_mark
def test_offline_position():
    positionIds = []
    for position_info in positions_result['content']['positions']['result']:
        positionId = position_info['positionId']
        positionIds.append(positionId)
    for id in positionIds:
        positions_offline(id, userToken=userToken, H9=True)


def test_publish_position():
    r = publish_position(userToken)
    assert_equal(1, r['state'], "校验发布职位成功")
    global positionId
    try:
        positionId = r['content']['lagouPositionId']
    except:
        positionId = 0


@pytest.mark.parametrize("accountName,password", [("0085220711424", "123456")])
def test_password_login(accountName, password):
    r = password_login(accountName, password)
    assert_equal(1, r['state'], '校验密码登录成功', '校验密码登录失败')
    global userToken
    userToken = r['content']['userToken']


def test_get_jd():
    r = get_jd(userToken, positionId)
    assert_equal(1, r['state'], "校验获取职位jd信息成功！")


def test_get_hr_info():
    r = get_hr_info(userToken, positionId)
    assert_equal(1, r['state'], "校验与职位的HR立即沟通成功！")


def test_deliver_check():
    r = deliver_check(positionId=positionId, H9=True, userToken=userToken)
    assert_equal(True, bool(r['state']), "校验投递简历的校验成功")


def test_get_resume_info():
    r = get_resume_info(userToken)
    global resumeId, resumeType
    resumeId = r['content'][0]['resumeId']
    resumeType = r['content'][0]['resumeType']
    assert_equal(1, r['state'], "校验获取简历信息成功")


def test_deliver_create():
    r = deliver_create(positionId, resumeId, resumeType, H9=True, isTalk=False, userToken=userToken)
    assert_equal(1, r['state'], "校验投递简历成功！")
