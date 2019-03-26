# coding:utf-8
# @Time  : 2019-03-26 10:40
# @Author: Xiawang
import pytest

from api_script.neirong_app.Community import communityMessage_clearRedSpot, communityMessage_userBasicInfo
from utils.util import assert_equal


@pytest.mark.parametrize('userid', [(100014641)])
def test_communityMessage_clearRedSpot(userid):
    r = communityMessage_clearRedSpot(userid)
    assert_equal(1, r['state'], '清除红点成功')


@pytest.mark.parametrize('start, size, userid', [(0, 10, 100014648)])
def test_communityMessage_userBasicInfo_page(start, size, userid):
    r = communityMessage_userBasicInfo(start, size, userid)
    start_one = r['content']['start']
    if start < start_one:
        r = communityMessage_userBasicInfo(start_one, size, userid)
        start_two = r['content']['start']
        if start_two == start_one:
            assert_equal(0, len(r['content']['result']), '偏移分页处理成功')


@pytest.mark.parametrize('start, size, userid', [(0, 10, 100018443)])
def test_communityMessage_userBasicInfo_type1(start, size, userid):
    r = communityMessage_userBasicInfo(start, size, userid)
    for i in r['content']['result']:
        if i['type'] == 1:
            assert_equal(True, bool(i['questionId']), '问题id存在值, 用例通过！')
            assert_equal(bool(i['anonymous']), bool(i['anonymous']), '是否匿名字段存在值, 用例通过！')


@pytest.mark.parametrize('start, size, userid', [(0, 10, 100018443)])
def test_communityMessage_userBasicInfo_type2(start, size, userid):
    r = communityMessage_userBasicInfo(start, size, userid)
    for i in r['content']['result']:
        if i['type'] == 2:
            assert_equal(True, bool(i['questionId']), '问题id存在值, 用例通过！')
            assert_equal(bool(i['anonymous']), bool(i['anonymous']), '是否匿名字段存在值, 用例通过！')
            assert_equal(True, bool(i['summary']), '是否匿名字段存在值, 用例通过！')


@pytest.mark.parametrize('start, size, userid', [(0, 10, 100014641)])
def test_communityMessage_userBasicInfo_type3(start, size, userid):
    r = communityMessage_userBasicInfo(start, size, userid)
    for i in r['content']['result']:
        if i['type'] == 3:
            assert_equal(True, bool(i['questionId']), '问题id存在值, 用例通过！')


@pytest.mark.parametrize('start, size, userid', [(0, 10, 100014641)])
def test_communityMessage_userBasicInfo_type4(start, size, userid):
    r = communityMessage_userBasicInfo(start, size, userid)
    for i in r['content']['result']:
        if i['type'] == 4:
            assert_equal(True, bool(i['answerId']), '回答id存在值, 用例通过！')
            assert_equal(True, bool(i['answerUserId']), '回答用户id存在值, 用例通过！')
            assert_equal(bool(i['anonymous']), bool(i['anonymous']), '是否匿名存在值, 用例通过！')
            assert_equal(True, bool(i['comment']), '评论内容存在值, 用例通过！')
            assert_equal(True, bool(i['replyComment']), '回复的评论的内容存在值, 用例通过！')


@pytest.mark.parametrize('start, size, userid', [(0, 10, 100014648)])
def test_communityMessage_userBasicInfo_type5(start, size, userid):
    r = communityMessage_userBasicInfo(start, size, userid)
    for i in r['content']['result']:
        if i['type'] == 5:
            assert_equal(True, bool(i['answerId']), '回答id存在值, 5-点赞 用例通过！')
            assert_equal(True, bool(i['summary']), '回答摘要存在值, 5-点赞 用例通过！')
            assert_equal(True, bool(i['userIds']), '消息聚合用户id存在值, 5-点赞 用例通过！')
            assert_equal(True, bool(i['userNames']), '消息聚合用户名存在值, 5-点赞 用例通过！')
            assert_equal(True, bool(i['replyComment']), '回复的评论的内容存在值, 5-点赞 用例通过！')
            assert_equal(True, bool(i['portraits']), '消息聚合用户头像存在值, 5-点赞 用例通过！')


@pytest.mark.parametrize('start, size, userid', [(0, 10, 100014641)])
def test_communityMessage_userBasicInfo_type6(start, size, userid):
    r = communityMessage_userBasicInfo(start, size, userid)
    for i in r['content']['result']:
        if i['type'] == 6:
            assert_equal(True, bool(i['reason']), '拒绝原因存在值, 6-提问未通过审核 用例通过！')


@pytest.mark.parametrize('start, size, userid', [(0, 10, 100014641)])
def test_communityMessage_userBasicInfo_type7(start, size, userid):
    r = communityMessage_userBasicInfo(start, size, userid)
    for i in r['content']['result']:
        if i['type'] == 7:
            assert_equal(True, bool(i['reason']), '拒绝原因存在值, 7-回答未通过审核 用例通过！')
            assert_equal(True, bool(i['summary']), '回答摘要存在值, 7-回答未通过审核 用例通过！')