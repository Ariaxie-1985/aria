# coding:utf-8
# @Time  : 2019-11-29 11:42
# @Author: Xiawang
# Description:
import json

from utils.util import get_code_token, json_put, login_password, get_header, get_requests


def upate_user_password(newPassword):
    code, token = get_submit_token_code()
    url = 'https://gate.lagou.com/v1/neirong/account/users/0/password'
    header = {'X-Anit-Forge-Code': code, 'X-Anit-Forge-Token': token, 'X-L-REQ-HEADER': json.dumps({'deviceType': 1})}
    data = {'newPassword': newPassword, 'newPassword2': newPassword}
    return json_put(url=url, data=data, headers=header, remark='PC端修改密码')


def get_submit_token_code():
    url = 'https://gate.lagou.com/v1/neirong/account/users/0/'
    header = {'X-L-REQ-HEADER': json.dumps({'deviceType': 1}),
              'Referer': 'https://account.lagou.com/v2/account/modifyPwd.html',
              'Sec-Fetch-Mode': 'cors'}
    r = get_requests(url=url, headers=header, remark="获取token、code")
    return r['submitCode'], r['submitToken']


if __name__ == '__main__':
    login_password('0085220131723', "990eb670f81e82f546cfaaae1587279a")
    upate_user_password()
