# coding:utf-8
# @Time  : 2020/4/17 13:09
# @Author: Xiawang
# Description:
import logging
import os
import sys
import time

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import requests

from utils.read_file import read_cancel_account, rewrite_cancel_account, record_cancel_account
from api_script.entry.cuser.baseStatus import batchCancel
from api_script.home.forbid import verify_user_is_forbid, forbid_user
from utils.util import login_password, assert_equal

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('/home/test/cancel_account_output.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def send_cancel_result(message, result):
    url = 'https://open.feishu.cn/open-apis/bot/hook/882babeafa3e4f0b839d6ff41efa2b84'
    data = {
        "title": "自动注销账号结果:",
        "text": f'{message}: {",".join(result)}'
    }
    requests.post(url=url, json=data, verify=False).json()


# 每隔300秒执行一次任务
def regular_batch_cancel_account():
    result = read_cancel_account()
    if not bool(result):
        logger.info(f'无需注销的数据\n')
        return
    logger.info(f'开始注销用户id:{",".join(result)}\n')
    r = login_password('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
    assert_equal(1, r.get('state'), '校验登录home成功！', te='王霞')

    fail_user_ids = ''
    success_user_ids = ''
    for user_id in result:
        time.sleep(1)
        forbid_result = verify_user_is_forbid(user_id)
        if forbid_result == False:
            forbid_result = forbid_user(user_id)
            if forbid_result == False:
                fail_user_ids += f'{user_id},'
                record_cancel_account(user_id)
            else:
                success_user_ids += f'{user_id},'

        r = batchCancel(userIds=user_id)
        if r.get('state') != 1:
            fail_user_ids += f'{user_id},'
        else:
            success_user_ids += f'{user_id},'

    rewrite_cancel_account()
    if success_user_ids != '':
        result = list(set(success_user_ids.split(',')))
        send_cancel_result(message='注销封禁用户Id成功', result=result)

    if fail_user_ids != '':
        record_cancel_account(fail_user_ids)


if __name__ == "__main__":
    regular_batch_cancel_account()
