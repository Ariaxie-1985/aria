# coding:utf-8
# @Time  : 2019-04-28 17:48
# @Author: Xiawang
import pytest

from api_script.zhaopin_app.notification import notification_read, notification_query, notification_read_all
from utils.util import assert_equal



@pytest.importorskip('test_notification.py', reason="等上线后才可在default环境根据数据来写具体断言，预计15号上线")
def test_notification_query():
    res = notification_query()
    global notificationId
    notificationId = res['content']['result'][0]['id']
    assert_equal(1, res['state'], "查询简历动态通知成功")


def test_notification_read():
    res = notification_read(notificationId)
    assert_equal(1, res['state'], "查询简历动态通知成功")


def test_notification_read_all():
    res = notification_read_all()
    assert_equal(1, res['state'], "查询简历动态通知成功")
