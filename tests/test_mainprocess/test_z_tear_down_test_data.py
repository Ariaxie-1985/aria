# coding:utf-8
# @Time  : 2020/5/26 10:50
# @Author: Xiawang
# Description:
import time
from api_script.entry.cuser.baseStatus import batchCancel
from api_script.home import forbid
from api_script.home.forbid import query_user_id, query_company_id
from utils.loggers import logers
from utils.util import login_password, assert_equal

loger = logers()


class TestCleanData(object):

    def test_login_home(self):
        # 线上home后台的用户账号和密码, 勿动
        r = login_password('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
        assert_equal(1, r['state'], '校验登录home成功！')

    def test_batch_forbid_user(self, telephone):
        for t in telephone:
            time.sleep(1)
            user_id = query_user_id(t)
            if bool(user_id):
                forbid_result = forbid.forbid_user(user_id)
                assert_equal(True, forbid_result, f'校验用户{user_id}是否封禁成功')
                r = batchCancel(userIds=user_id)
                assert_equal(1, r['state'], f"用户{user_id}注销账号成功")
                loger.info(f'注销用户:手机号:{telephone}, Id:{user_id}成功')

    def test_forbid_company(self, get_company_name):
        company_id = query_company_id(get_company_name)
        if bool(company_id):
            forbid_result = forbid.forbid_company(company_id)
            assert_equal(True, forbid_result, f'校验公司{company_id}是否封禁成功')
            loger.info(f'注销公司{company_id}成功')
        else:
            assert_equal(1, 0, f'校验公司{company_id}封禁失败')
