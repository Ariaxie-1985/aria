# coding:utf-8
# @Time  : 2020/7/2 14:21
# @Author: Arayang
# Description:
import pytest
from api_script.education.course import get_credit_center_info, \
    receive_credit, exchange_present
from utils.util import verify_code_message
from api_script.entry.cuser.baseStatus import batchCancel
from api_script.entry.account.passport import register_by_phone, send_verify_code, verifyCode_login
from api_script.entry.account.me import modify_password
import time
from utils.util import assert_equal
import datetime

now_time = datetime.datetime.now()
minute = now_time.minute
minute2 = minute % 2


@pytest.mark.skipif('minute2==0', reason='分钟是偶数跳过执行')
def test_receive_credit1(self, c_login_education_0044, get_edu_h5_token):
    global receive_success
    r = receive_credit(gateLoginToken=get_edu_h5_token)
    receive_success = r.get('content')
    assert_equal(1, r.get('state'), "领取学分接口请求成功", te='杨彦')


@pytest.mark.skipif('minute2==0', reason='分钟是偶数跳过执行')
@pytest.mark.skipif('receive_success!=1', reason="领取失败，跳过此用例")
def test_exchange_present1(self, get_edu_h5_token, c_login_education_0044):
    change1 = exchange_present(gateLoginToken=get_edu_h5_token)
    assert_equal(1, change1.get('state'), "领取登录学分后，兑换成功", te='杨彦')


@pytest.mark.skipif('minute2==0', reason='分钟是偶数跳过执行')
def test_usable_credit(self, c_login_education_0044, get_edu_h5_token):
    global courseCredit
    r = get_credit_center_info(userToken=c_login_education_0044[0])
    courseCredit = r.get('content').get('usableCredit')
    assert_equal(1, r.get('state'), "获取可用学分执行成功", te='杨彦')


@pytest.mark.skipif('minute2==0', reason='分钟是偶数跳过执行')
@pytest.mark.skipif('courseCredit==0', reason="学分为零，不能兑换礼物，跳过此用例")
def test_exchange_present2(self, get_edu_h5_token):
    change2 = exchange_present(gateLoginToken=get_edu_h5_token)
    assert_equal(1, change2.get('state'), "利用现有学分余额兑换成功", te='杨彦')


@pytest.mark.skipif('minute2==0', reason='分钟是偶数跳过执行')
def test_batch_register(self, c_login_education_0044):
    userid = c_login_education_0044[1]
    batch_state = batchCancel(userIds=userid)
    assert_equal(1, batch_state.get('state'), "账号注销成功", te='杨彦')

    countrycode_phone = c_login_education_0044[2]
    countrycode = countrycode_phone[1:5]
    phone = countrycode_phone[5:]
    sendverigycode = send_verify_code(countryCode=countrycode, phone=phone, businessType='PASSPORT_REGISTER',
                                      app_type='LGEdu')
    assert_equal(1, sendverigycode.get('state'), "验证码发送成功", te='杨彦')
    time.sleep(12)

    verify_code = verify_code_message(countryCode=countrycode, phone=phone)
    assert_equal(True, bool(verify_code), "获取验证码成功", te='杨彦')

    verifyCode_login(countryCode=countrycode, phone=phone, verify_code=verify_code, app_type='LGEdu')
    registate = register_by_phone(countryCode=countrycode, phone=phone, verify_code=verify_code, app_type='LGEdu')
    assert_equal(1, registate.get('state'), "账号注册成功", te='杨彦')

    retoken = register_by_phone(countryCode=countrycode, phone=phone, verify_code=verify_code, app_type='LGEdu')
    m = modify_password(userToken=retoken.get('content').get('userToken'))
    assert_equal(1, m['state'], "设置密码成功", te='杨彦')
