# coding:utf-8

from util import form_post, get_code_token, login

username = 20181205
login("00852",username)

userId = 100014642

# 添加子账号
refer_queryAcount_url = "https://easy.lagou.com/subAccount/queryAcount/index.htm"
queryAcount_url = "https://easy.lagou.com/subAccount/addAcount.json"
queryAcount_data = {"userId":userId}
queryAcount_header = get_code_token(refer_queryAcount_url)
form_post(queryAcount_url, queryAcount_data,queryAcount_header)
