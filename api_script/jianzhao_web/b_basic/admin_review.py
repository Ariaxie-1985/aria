# coding:utf-8
# @Time  : 2019-11-28 11:24
# @Author: Xiawang
# Description:
from utils.util import get_header, json_post, get_code_token, form_post


def admin_review(userid):
    url = "https://easy.lagou.com/bstatus/auth/manager/assist.json"
    header = get_header(url="https://easy.lagou.com/im/chat/index.htm")
    data = {'applyUserId': userid, 'confirmButton': 'true'}
    return json_post(url=url, headers=header, data=data, remark="管理员审核通过")
