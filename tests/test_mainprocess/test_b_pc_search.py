# coding:utf-8
# @Time  : 2019-09-24 14:41
# @Author: Foxtang
# Description:
import time

import pytest
import json

from api_script.jianzhao_web.talent.B_looking_for_talent import talent_search_list
from utils.loggers import logers
from utils.util import assert_equal, assert_in, login_password

loger = logers()

class TestPCSearch(object):
    def test_login_pc_user111(self):
        r = login_password('00911111111111', 'c47eeb69fa4e64971fb29cb1e9163a19')
        assert_equal(1, r.get('state', 0), '登录有职位的固定账号成功')

    def test_talent_pc_search(self):
        r = talent_search_list('java')
        assert_equal(True,bool(r['content']['data']['page']['totalCount']>= 100),'搜索java结果大于100')





