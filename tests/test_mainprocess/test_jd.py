# coding:utf-8
# @Time  : 2019-09-24 14:41
# @Author: Xiawang
# Description:
import pytest
import random

from api_script.entry.account.passport import password_login
from api_script.entry.buser.hrinfo import get_hr_info
from api_script.entry.deliver.deliver import deliver_check, get_resume_info, deliver_create
from api_script.entry.position.jd import get_jd
from api_script.zhaopin_app.b_position import get_online_positions, publish_position
from utils.util import assert_equal



@pytest.mark.parametrize("accountName,password", [("19910626899", "000000")])
def test_publish_position(accountName, password):
    r = password_login(accountName, password)
    global userToken
    userToken = r['content']['userToken']
    r = publish_position(userToken)
    assert_equal(1, r['state'], "校验发布职位成功")
    global positionId
    try:
        positionId = r['content']['lagouPositionId']
    except:
        positionId = 0


@pytest.mark.skip(reason="无需获取在线职位id")
def test_get_online_positions():
    r = get_online_positions(userToken, H9=True)
    global positionId
    try:
        positionId = r['content']['positions']['result'][random.randint(0, 5)]['outerPositionId']
    except:
        positionId = r['content']['positions']['result'][0]['outerPositionId']
    assert_equal(1, r['state'], "校验获取在线职位成功！")


# @pytest.mark.parametrize("accountName,password", [("0085220181205", "0085220181205")])
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
