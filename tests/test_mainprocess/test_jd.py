# coding:utf-8
# @Time  : 2019-09-24 14:41
# @Author: Xiawang
# Description:

import pytest
import json
from api_script.entry.buser.hr_info import get_hr_info
from api_script.entry.deliver.deliver import deliver_check, get_resume_info, deliver_create, \
    recommend_isExistPositionList, recommend_positionList
from api_script.entry.position.communicatePositions import get_jd
from api_script.zhaopin_app.bUser import quickReply_all
from api_script.zhaopin_app.b_chat import chat_c_lastResume, chat_c_info, chat_position, chat_interview_check
from api_script.zhaopin_app.b_position import get_online_positions, publish_position, positions_offline
from api_script.zhaopin_app.orderResumes import orderResumes_resume_interview, \
    orderResumes_resume_obsolete, orderResumes_detail, orderResumes_read
from api_script.zhaopin_app.talent import talent_recTalent, talent_newTalent, talent_collections, talent_app_search, \
    talent_info_get
from utils.util import assert_equal, assert_in


def test_is_enough_positions(b_login_app):
    global flag, positions_result
    positions_result = get_online_positions(userToken=b_login_app[0], H9=True)
    flag = positions_result['content']['onlinePositionNum']
    assert_equal(1, positions_result['state'], '确认在线职位数是否足够发布职位用例通过')


@pytest.mark.skipif('flag <= 20', reason="发布职位权益足够，无需下线职位")
def test_offline_position(b_login_app):
    positionIds = []
    for position_info in positions_result['content']['positions']['result']:
        positionId = position_info['positionId']
        positionIds.append(positionId)
    for id in positionIds:
        positions_offline(id, userToken=b_login_app[0], H9=True)


def test_publish_position(b_login_app):
    r = publish_position(userToken=b_login_app[0])
    assert_equal(1, r['state'], "校验发布职位成功")
    global positionId, mdsPositionId
    try:
        positionId = r['content']['lagouPositionId']
        mdsPositionId = r['content']['mdsPositionId']
    except:
        positionId = 0


portrait_format = ['jpg', 'png', 'jpeg']


def test_talent_recTalent(b_login_app):
    r = talent_recTalent(userToken=b_login_app[0], positionId=positionId)
    assert_equal(True, bool(len(r['content']['result'])), "推荐人才用例通过")
    for talent in r['content']['result']:
        if bool(talent.get('portrait', False)):
            assert_in(talent['portrait'].split(".")[-1], portrait_format, "推荐人才的头像信息用例通过")


def test_talent_newTalent(b_login_app):
    r = talent_newTalent(userToken=b_login_app[0], positionId=positionId)
    assert_equal(True, bool(len(r['content']['result'])), "最新人才用例通过")
    for talent in r['content']['result']:
        if bool(talent.get('portrait', False)):
            assert_in(talent['portrait'].split(".")[-1], portrait_format, "最新人才的头像信息用例通过")


def test_talent_collections(b_login_app):
    r = talent_collections(userToken=b_login_app[0])
    assert_equal(True, bool(len(r['content']['result'])), "人才收藏用例通过")
    for talent in r['content']['result']:
        if bool(talent.get('portrait', False)):
            portrait = json.loads(talent['portrait'])
            assert_in(portrait['url'].split(".")[-1], portrait_format, "人才收藏的头像信息用例通过")


@pytest.mark.parametrize("city, positionName, pageNo", [("北京", "测试工程师", 1), ("北京", "测试工程师", 2)])
def test_talent_app_search(b_login_app, city, positionName, pageNo):
    r = talent_app_search(userToken=b_login_app[0], city=city, positionName=positionName, pageNo=pageNo)
    assert_equal(True, bool(len(r['content']['bresumeSearchResultVos'])), "人才搜索用例通过")


def test_get_jd(c_login_app):
    r = get_jd(userToken=c_login_app[0], positionId=positionId)
    assert_equal(1, r['state'], "校验获取职位jd信息成功！")


def test_get_hr_info(c_login_app, b_login_app):
    r = get_hr_info(userToken=c_login_app[0], publisherId=b_login_app[1])
    assert_equal(1, r['state'], "校验与职位的HR立即沟通成功！")


def test_deliver_check(c_login_app):
    r = deliver_check(positionId=positionId, H9=True, userToken=c_login_app[0])
    assert_equal(1, r['state'], "校验投递简历的校验成功")


def test_get_resume_info(c_login_app):
    r = get_resume_info(userToken=c_login_app[0])
    global resumeId, resumeType
    resumeId = r['content'][0]['resumeId']
    resumeType = r['content'][0]['resumeType']
    assert_equal(1, r['state'], "校验获取简历信息成功")


def test_deliver_create(c_login_app):
    r = deliver_create(positionId=positionId, resumeId=resumeId, resumeType=resumeType, H9=True, isTalk=False,
                       userToken=c_login_app[0])
    assert_equal(1, r['state'], "校验投递简历成功！")
    global orderId
    orderId = r['content']['orderId']


def test_recommend_isExistPositionList(c_login_app):
    r = recommend_isExistPositionList(userToken=c_login_app[0], positionId=positionId)
    assert_equal(1, r['state'], '投递后推荐的职位 （投了又投），是否有数据用例通过')


def test_recommend_positionList(c_login_app):
    r = recommend_positionList(userToken=c_login_app[0], orderId=orderId, positionId=positionId)
    assert_equal(True, bool(r['content']['positionList']), '投递后推荐的职位 （投了又投)用例通过')


def test_talent_info_get(b_login_app, c_login_app):
    r = talent_info_get(userToken=b_login_app[0], userId=c_login_app[1])
    global long_resumeId
    long_resumeId = r['content']['resumeId']
    assert_equal(True, bool(r['content']['resumeCoreInfo']['resumeCoreInfo']['resumeId']),
                 "获取人才信息用例通过")


def test_quickReply_all(b_login_app):
    r = quickReply_all(userToken=b_login_app[0])
    assert_equal(1, r['state'], "获取IM的快捷回复用例通过")


def test_chat_c_lastResume(b_login_app, c_login_app):
    r = chat_c_lastResume(userToken=b_login_app[0], cUserId=c_login_app[1])
    # assert_equal(4, actualvalue=r['content']['resumeStageCode'], success_message="获取候选人最近一次投递状态用例通过")
    assert_equal(1, r['state'], '查询面试安排记录-新简历用例通过')


def test_chat_c_info(b_login_app, c_login_app):
    r = chat_c_info(userToken=b_login_app[0], cUserId=c_login_app[1])
    assert_equal(1, r['state'], "获取候选人的详情信息用例通过")


def test_chat_c_position(b_login_app, c_login_app):
    r = chat_position(userToken=b_login_app[0], cUserId=c_login_app[1], positionId=positionId)
    assert_equal(False, r['content']['positionDelivered'], "获取IM在沟通的职位用例通过")


def test_chat_interview_check(b_login_app):
    r = chat_interview_check(userToken=b_login_app[0], resumeId=long_resumeId)
    assert_equal(1, r['state'], "检查IM是否能邀约面试用例通过")


def test_chat_c_lastResume_1(b_login_app, c_login_app):
    r = chat_c_lastResume(userToken=b_login_app[0], cUserId=c_login_app[1])
    # assert_equal(4, r['content']['resumeStageCode'], "查询面试安排记录-新简历用例通过")
    assert_equal(1, r['state'], '查询面试安排记录-新简历用例通过')


def test_orderResumes_resume_interview(b_login_app):
    r = orderResumes_resume_interview(userToken=b_login_app[0], resumeId=long_resumeId,
                                      positionId=mdsPositionId)
    assert_equal(1, r['state'], '邀约面试用例通过')


def test_chat_c_lastResume_4(b_login_app, c_login_app):
    r = chat_c_lastResume(userToken=b_login_app[0], cUserId=c_login_app[1])
    # assert_equal(4, r['content']['resumeStageCode'], "查询面试安排记录-面试用例通过")
    assert_equal(1, r['state'], '查询面试安排记录-新简历用例通过')


def test_orderResumes_resume_obsolete(b_login_app):
    r = orderResumes_resume_obsolete(userToken=b_login_app[0], resumeId=long_resumeId)
    assert_equal(1, r['state'], '候选人状态调整为不合适用例通过')


def test_chat_c_lastResume_64(b_login_app, c_login_app):
    r = chat_c_lastResume(userToken=b_login_app[0], cUserId=c_login_app[1])
    # assert_equal(4, r['content']['resumeStageCode'], "查询面试安排记录-淘汰用例通过")
    assert_equal(1, r['state'], '查询面试安排记录-新简历用例通过')


def test_orderResumes_detail(b_login_app):
    r = orderResumes_detail(userToken=b_login_app[0], resumeId=long_resumeId)
    assert_equal(expectvalue=long_resumeId, actualvalue=int(r['content']['orderResumeId']),
                 success_message="查询简历详情用例通过")


def test_orderResumes_read(b_login_app):
    r = orderResumes_read(userToken=b_login_app[0], resumeId=long_resumeId)
    assert_equal(1, r['state'], '设置简历已读用例通过')
