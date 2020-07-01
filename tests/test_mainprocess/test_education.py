# coding:utf-8
# @Time  : 2020/3/6 17:19
# @Author: Xiawang
# Description:
import pytest

from api_script.education.app import get_homepage_cards, get_all_course_purchased_record
from api_script.education.bigcourse import get_course_info, get_course_outline, get_week_lessons, get_watch_percent, \
    no_class_dacourse
from api_script.education.course import get_course_commentList, get_distribution_poster_data, get_credit_center_info, \
    get_distribution_course_list, get_my_earing, get_user_earnings_detail, get_wei_xin_user, receive_credit, \
    exchange_present, get_course_credit_info
from api_script.education.kaiwu import get_course_description, get_distribution_info, check_course_share_status, \
    get_course_lessons, ice_breaking_location, ice_breaking_html
from utils.util import assert_equal, assert_in, verify_code_message
from api_script.neirong_app.app import get_user_base_info
from api_script.entry.cuser.baseStatus import batchCancel
from api_script.entry.account.passport import register_by_phone, send_verify_code, verifyCode_login
from api_script.entry.account.me import modify_password
import time
from utils.util import assert_equal, assert_in


@pytest.mark.incremental
class TestEducation01(object):

    @pytest.mark.parametrize("expect_card_type, expect_title", [(1, "广告banner"), (2, "训练营"), (3, "专栏")])
    def test_get_homepage_cards(self, c_login_education, expect_card_type, expect_title):
        r = get_homepage_cards(userToken=c_login_education[0])
        # for card in r['content']['pageCardList']:
        #     assert_equal(expect_card_type, card['cardType'], "拉勾教育-获取首页卡片信息列表用例通过")
        #     assert_equal(expect_title, card['title'], "拉勾教育-获取首页卡片信息列表用例通过")
        assert_equal(1, r.get('state'), "拉勾教育-获取首页卡片信息列表用例通过", te='王霞')
        global first_small_course_id, first_small_course_brief, first_small_course_title, decorate_id
        first_small_course_id = r['content']['pageCardList'][2]['smallCourseList'][0]['id']
        first_small_course_brief = r['content']['pageCardList'][2]['smallCourseList'][0]['brief']
        first_small_course_title = r['content']['pageCardList'][2]['smallCourseList'][0]['title']
        decorate_id = r['content']['pageCardList'][2]['smallCourseList'][0]['decorateId']

    def test_check_course_share_status(self, c_login_education):
        r = check_course_share_status(userToken=c_login_education[0], courseId=first_small_course_id)
        assert_equal(1, r.get('state'), "选课查询课程详情用例通过", te='王霞')

    def test_get_course_lessons(self, c_login_education):
        r = get_course_lessons(userToken=c_login_education[0], courseId=first_small_course_id)
        assert_equal(first_small_course_title, r['content']['courseName'], '查询课程详情用例通过', te='王霞')

    def test_get_course_description(self, c_login_education):
        r = get_course_description(userToken=c_login_education[0], courseId=first_small_course_id)
        assert_equal(first_small_course_id, r['content']['id'], "选课查询课程详情用例通过", te='王霞')

    def test_get_distribution_info(self, c_login_education):
        r = get_distribution_info(userToken=c_login_education[0], courseId=first_small_course_id,
                                  decorateId=decorate_id)
        assert_equal(1, r.get('state'), '言职/开悟/获取分销信息用例通过', te='王霞')
        if r['content']['showDistributionButton'] is True:
            assert_equal(first_small_course_brief, r['content']['distributionBaseInfoVo']['brief'], "该课程有分销信息用例通过",
                         te='王霞')

    def test_get_course_commentList(self, c_login_education):
        r = get_course_commentList(userToken=c_login_education[0], courseId=first_small_course_id)
        assert_equal(1, r.get('state'), "获取课程的评论用例通过", te='王霞')

    def test_get_distribution_poster_data(self, get_h5_token):
        r = get_distribution_poster_data(courseId=first_small_course_id, decorateId=decorate_id,
                                         gateLoginToken=get_h5_token)
        assert_equal(first_small_course_title, r['content']['courseName'], "获取分销海报数据用例通过", te='张红彦')


@pytest.mark.incremental
class TestEducation02(object):
    def test_get_all_course_purchased_record(self, c_login_education):
        r = get_all_course_purchased_record(userToken=c_login_education[0])
        assert_equal(1, r.get('state'), "获取所有已购课程的列表(大课和专栏课程)用例通过", te='王霞')
        global big_course_record_id, small_course_record_id
        big_course_record_id = r['content']['allCoursePurchasedRecord'][0]['bigCourseRecordList'][0]['id']
        small_course_record_id = r['content']['allCoursePurchasedRecord'][1]['courseRecordList'][0]['id']

    def test_get_course_info(self, c_login_education):
        r = get_course_info(userToken=c_login_education[0], courseId=big_course_record_id)
        assert_equal(1, r.get('state'), "获取大课的课程基本信息用例通过", te='王霞')
        global lastWatchWeekId
        lastWatchWeekId = r['content']['lastWatchWeekId']

    def test_get_course_outline(self, c_login_education):
        r = get_course_outline(userToken=c_login_education[0], courseId=big_course_record_id)
        assert_equal(1, r.get('state'), "获取大课的课程大纲用例通过", te='王霞')

    def test_get_week_lessons(self, c_login_education):
        r = get_week_lessons(userToken=c_login_education[0], courseId=big_course_record_id, weekId=lastWatchWeekId)
        assert_equal("SUCCESS", r['content']['bigCourseResult'], "获取大课一周下的所有课时用例通过", te='王霞')

    def test_get_watch_percent(self, c_login_education):
        r = get_watch_percent(userToken=c_login_education[0], courseId=big_course_record_id, weekId=lastWatchWeekId)
        assert_equal(1, r.get('state'), "获取大课一周录播视频观看进度", te='王霞')


def test_get_credit_center_info(c_login_education):
    r = get_credit_center_info(userToken=c_login_education[0])
    assert_equal(1, bool(len(r.get('content').get('userGrowthCreditTaskVos'))), "学分中心任务列表", te='杨彦')


def test_get_course_credit_info(c_login_education):
    x = TestEducation02()
    x.test_get_all_course_purchased_record(c_login_education)
    r = get_course_credit_info(userToken=c_login_education[0], courseId=small_course_record_id)
    assert_equal(1, bool(len(r.get('content').get('userGrowthCreditTaskVos'))), "个人成就的任务列表", te='杨彦')


def test_ice_breaking_location():
    r = ice_breaking_location()
    assert_equal("限时1元抢>", r['content']['text'], "显示1元购入口", te='betty')


def test_ice_breaking_html():
    r = ice_breaking_html()
    assert_in("拉勾教育·1元抢好课", r, "进入到1元购的界面", te='betty')


def test_get_distribution_course_list(get_h5_token):
    r = get_distribution_course_list(gateLoginToken=get_h5_token)
    assert_equal(1, bool(r.get('content').get('distributionCourseList')), "获取分销列表用例通过", te='张红彦')


def test_get_my_earing(get_h5_token):
    r = get_my_earing(gateLoginToken=get_h5_token)
    assert_equal(1, bool(r['content']['availableEarning']), "获取我的收益用例通过", te='张红彦')


def test_get_user_earnings_detail(get_h5_token):
    r = get_user_earnings_detail(gateLoginToken=get_h5_token)
    assert_equal(1, bool(r['content']['unavailableEarning']), "获取收益详情用例通过", te='张红彦')


def test_get_wei_xin_user(get_h5_token):
    r = get_wei_xin_user(gateLoginToken=get_h5_token)
    assert_equal(True, r['content']['hasBind'], "获取微信用户信息用例通过", te='张红彦')


class TestUserGrowth(object):
    def test_receive_credit1(self, c_login_education_0044, get_edu_h5_token):
        global receive_success
        r = receive_credit(gateLoginToken=get_edu_h5_token)
        receive_success = r['content']
        assert_equal(True, bool(receive_success), "登录学分领取成功", te='杨彦')

    @pytest.mark.skipif('receive_success!=1', reason="领取失败，跳过此用例")
    def test_exchange_present1(self, get_edu_h5_token, c_login_education_0044):
        change1 = exchange_present(gateLoginToken=get_edu_h5_token)
        assert_equal(1, change1.get('state'), "领取登录学分后，兑换成功", te='杨彦')

    def test_usable_credit(self, c_login_education_0044, get_edu_h5_token):
        global courseCredit
        r = get_credit_center_info(userToken=c_login_education_0044[0])
        courseCredit = r.get('content').get('usableCredit')
        print(courseCredit)
        assert_equal(1, r.get('state'), "获取可用学分执行成功", te='杨彦')

    @pytest.mark.skipif('courseCredit==0', reason="学分为零，不能兑换礼物，跳过此用例")
    def test_exchange_present2(self, get_edu_h5_token):
        change2 = exchange_present(gateLoginToken=get_edu_h5_token)
        assert_equal(1, change2.get('state'), "利用现有学分余额兑换成功", te='杨彦')

    def test_batch_register(self, c_login_education_0044):
        userid = c_login_education_0044[1]
        batch_state = batchCancel(userIds=userid)
        assert_equal(1, batch_state.get('state'), "账号注销成功", te='杨彦')

        countrycode_phone = c_login_education_0044[2]
        countrycode = countrycode_phone[1:5]
        phone = countrycode_phone[5:]
        sendverigycode = send_verify_code(countryCode=countrycode, phone=phone, businessType='PASSPORT_REGISTER',
                                          app_type='LGEdu')
        print("*************")
        print(sendverigycode)
        assert_equal(1,sendverigycode.get('state'),"验证码发送成功", te='杨彦')
        time.sleep(12)

        verify_code = verify_code_message(countryCode=countrycode, phone=phone)
        assert_equal(True, bool(verify_code), "获取验证码成功", te='杨彦')

        verifyCode_login(countryCode=countrycode, phone=phone, verify_code=verify_code, app_type='LGEdu')
        registate = register_by_phone(countryCode=countrycode, phone=phone, verify_code=verify_code, app_type='LGEdu')
        assert_equal(1, registate.get('state'), "账号注册成功", te='杨彦')

        retoken = register_by_phone(countryCode=countrycode, phone=phone, verify_code=verify_code, app_type='LGEdu')
        m = modify_password(userToken=retoken.get('content').get('userToken'))
        assert_equal(1, m['state'], "设置密码成功", te='杨彦')


"""def test_exchange_present(c_login_education_0044, get_edu_h5_token):
    r = receive_credit(gateLoginToken=get_edu_h5_token)
    # json.loads(r)
    receive_success = r['content']
    if receive_success == 1:
        change1 = exchange_present(gateLoginToken=get_edu_h5_token)
        assert_equal(1, change1.get('state'), "领取登录学分后，兑换成功", te='杨彦')
    elif receive_success == None:
        r = get_user_base_info(userToken=c_login_education_0044[0])
        courseCredit = r.get('content').get('courseCredit')
        if courseCredit != 0:
            change2 = exchange_present(gateLoginToken=get_edu_h5_token)
            assert_equal(1, change2.get('state'), "利用现有学分余额兑换成功", te='杨彦')
        else:
            pass
    userid = c_login_education_0044[1]
    batchCancel(userIds=userid)
    countrycode_phone = c_login_education_0044[2]
    countrycode = countrycode_phone[1:5]
    phone = countrycode_phone[5:]
    sendverigycode = send_verify_code(countryCode=countrycode, phone=phone, businessType='PASSPORT_REGISTER',
                                      app_type='LGEdu')
    time.sleep(12)
    verify_code = verify_code_message(countryCode=countrycode, phone=phone)
    verifyCode_login(countryCode=countrycode, phone=phone, verify_code=verify_code, app_type='LGEdu')
    retoken = register_by_phone(countryCode=countrycode, phone=phone, verify_code=verify_code, app_type='LGEdu')
    modify_password(userToken=retoken.get('content').get('userToken'))"""


def test_dake_no_class(dake_no_class):
    r = no_class_dacourse()
    assert_equal("联系课程顾问加入班级", r['content']['allCoursePurchasedRecord'][0]['bigCourseRecordList'][0]['prepayTip'],
                 "暂未进班", te='betty')
