# coding:utf-8
# @Time  : 2020/2/26 18:17
# @Author: Xiawang
# Description:
from api_script.zhaopin_app.notification import notification_query, notification_unread_count, notification_read, \
    notification_read_all
from utils.util import assert_equal


def test_notification_query(b_login_app, ip_port):
    r = notification_query(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port)
    global notificationId
    notificationId = r['content']['result'][0]['id']
    assert_equal(True, bool(r['content']['result']), "获取简历状态消息列表用例通过")


def test_notification_unread_count(b_login_app,ip_port):
    r = notification_unread_count(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port)
    assert_equal(1, r['state'], "统计未读简历状态消息数用例通过")


def test_notification_read(b_login_app,ip_port):
    r = notification_read(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port, notificationId=notificationId)
    assert_equal(1, r['state'], "标记已读用例通过")


def test_notification_read_all(b_login_app,ip_port):
    r = notification_read_all(userToken=b_login_app[0], userId=b_login_app[1], ip_port=ip_port)
    assert_equal(1, r['state'], "全部标记已读用例通过")
