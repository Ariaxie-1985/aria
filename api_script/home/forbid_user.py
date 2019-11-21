# coding:utf-8
# @Time  : 2019-11-21 15:26
# @Author: Xiawang
# Description:
from utils.util import get_header, form_post, login_home


def forbid_user(userId):
    url = 'http://home.lagou.com/forbid/user/forbidUser.json'
    header = get_header(url='http://home.lagou.com/index.html')
    data = {'forbidAccount': '删除已投递简历,', 'reason': '冒用他人信息,', 'forbidAccountReason': '冒用他人信息,', 'userId': userId}
    return form_post(url=url, headers=header, data=data, remark="封禁账号")


if __name__ == '__main__':
    login_home(username='betty@lagou.com', password='ldb521jiayou')
    forbid_user(15670495)