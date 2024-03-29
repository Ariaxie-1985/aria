# coding:utf-8
# @Time  : 2020/5/26 10:50
# @Author: Xiawang
# Description:
import time
from api_script.entry.cuser.baseStatus import batchCancel
from api_script.home import forbid
from api_script.home.forbid import query_user_id, query_company_id
from utils.loggers import logers
from utils.read_file import record_cancel_account
from utils.util import login_password, assert_equal

loger = logers()


class TestCleanData(object):

    def test_login_home(self):
        # 线上home后台的用户账号和密码, 勿动
        r = login_password('autotest@lagou.com', 'a52f33ba89bd7af92982da737cafc8d0')
        assert_equal(1, r['state'], '校验登录home成功！', te='foxtang')

    def test_batch_forbid_user(self, telephone):
        userIds = []
        for t in telephone:
            time.sleep(1)
            r = query_user_id(t)
            if r.get('success', False) == False:
                continue
            if len(r['data']['pageData']) > 0:
                user_id = r['data']['pageData'][0]['id']
                userIds.append(user_id)

        for user_id in userIds:
            forbid_result = forbid.forbid_user(user_id)
            if forbid_result == False:
                record_cancel_account(user_id)
                loger.info(f'封禁用户:手机号:{t}, Id:{user_id}失败')
            else:
                loger.info(f'封禁用户:手机号:{t}, Id:{user_id}成功')

            r = batchCancel(userIds=user_id)
            if r.get('state') != 1:
                record_cancel_account(user_id)
                loger.info(f'注销用户:手机号:{t}, Id:{user_id}失败')
            else:
                loger.info(f'注销用户:手机号:{t}, Id:{user_id}成功')

    def test_forbid_company(self, get_company_name):
        company_id = query_company_id(get_company_name)
        if bool(company_id):
            forbid_result = forbid.forbid_company(company_id)
            assert_equal(True, forbid_result, f'校验公司{company_id}是否封禁成功', te='foxtang')
            loger.info(f'注销公司{company_id}成功')
        else:
            assert_equal(1, 0, f'校验公司{company_id}封禁失败', te='foxtang')
