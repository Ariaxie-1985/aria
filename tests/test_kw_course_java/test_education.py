# coding:utf-8
# @Time  : 2020/3/6 17:19
# @Author: Xiawang
# Description:
import pytest

from api_script.education.app import get_homepage_cards, get_all_course_purchased_record
from api_script.education.bigcourse import get_course_info, get_course_outline, get_week_lessons, get_watch_percent
from api_script.education.course import get_course_commentList,get_credit_center_info
from api_script.education.kaiwu import get_course_description, get_distribution_info, check_course_share_status, \
    get_course_lessons, ice_breaking_location
from utils.util import assert_equal



@pytest.mark.parametrize("expect_card_type, expect_title", [(1, "广告banner"), (2, "训练营"), (3, "专栏")])
def test_get_homepage_cards(c_login_education, expect_card_type, expect_title):
    r = get_homepage_cards(userToken=c_login_education[0])
    # for card in r['content']['pageCardList']:
    #     assert_equal(expect_card_type, card['cardType'], "拉勾教育-获取首页卡片信息列表用例通过")
    #     assert_equal(expect_title, card['title'], "拉勾教育-获取首页卡片信息列表用例通过")
    assert_equal(1, r['state'], "拉勾教育-获取首页卡片信息列表用例通过")
    global first_small_course_id, first_small_course_brief,first_small_course_title
    first_small_course_id = r['content']['pageCardList'][2]['smallCourseList'][0]['id']
    first_small_course_brief = r['content']['pageCardList'][2]['smallCourseList'][0]['brief']
    first_small_course_title = r['content']['pageCardList'][2]['smallCourseList'][0]['title']


def test_check_course_share_status(c_login_education):
    r = check_course_share_status(userToken=c_login_education[0], courseId=first_small_course_id)
    assert_equal(1, r['state'], "选课查询课程详情用例通过")


def test_get_course_lessons(c_login_education):
    r = get_course_lessons(userToken=c_login_education[0], courseId=first_small_course_id)
    assert_equal(first_small_course_title, r['content']['courseName'], '查询课程详情用例通过')


def test_get_course_description(c_login_education):
    r = get_course_description(userToken=c_login_education[0], courseId=first_small_course_id)
    assert_equal(first_small_course_id, r['content']['id'], "选课查询课程详情用例通过")


def test_get_distribution_info(c_login_education):
    r = get_distribution_info(userToken=c_login_education[0], courseId=first_small_course_id)
    assert_equal(first_small_course_brief, r['content']['distributionBaseInfoVo']['brief'], "选课查询课程分销信息用例通过")


def test_get_course_commentList(c_login_education):
    r = get_course_commentList(userToken=c_login_education[0], courseId=first_small_course_id)
    assert_equal(1, r['state'], "获取课程的评论用例通过")


def test_get_all_course_purchased_record(c_login_education):
    r = get_all_course_purchased_record(userToken=c_login_education[0])
    assert_equal(1, r['state'], "获取所有已购课程的列表(大课和专栏课程)用例通过")
    global big_course_record_id, small_course_record_id
    big_course_record_id = r['content']['allCoursePurchasedRecord'][0]['bigCourseRecordList'][0]['id']
    small_course_record_id = r['content']['allCoursePurchasedRecord'][1]['courseRecordList'][0]['id']


def test_get_course_info(c_login_education):
    r = get_course_info(userToken=c_login_education[0], courseId=big_course_record_id)
    assert_equal(1, r['state'], "获取大课的课程基本信息用例通过")
    global lastWatchWeekId
    lastWatchWeekId = r['content']['lastWatchWeekId']


def test_get_course_outline(c_login_education):
    r = get_course_outline(userToken=c_login_education[0], courseId=big_course_record_id)
    assert_equal(1, r['state'], "获取大课的课程大纲用例通过")


def test_get_week_lessons(c_login_education):
    r = get_week_lessons(userToken=c_login_education[0], courseId=big_course_record_id, weekId=lastWatchWeekId)
    assert_equal("SUCCESS", r['content']['bigCourseResult'], "获取大课一周下的所有课时用例通过")


def test_get_watch_percent(c_login_education):
    r = get_watch_percent(userToken=c_login_education[0], courseId=big_course_record_id, weekId=lastWatchWeekId)
    assert_equal(1, r['state'], "获取大课一周录播视频观看进度")





def test_get_credit_center_info(c_login_education):
    #r = bool(len(get_credit_center_info(userToken=c_login_education[0])['content']['userGrowthCreditTaskVos']))
    r = get_credit_center_info(userToken=c_login_education[0])
    assert_equal(1,bool(len(r.get('content').get('userGrowthCreditTaskVos'))),"学分中心任务列表")

