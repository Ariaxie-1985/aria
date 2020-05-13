# coding:utf-8
# @Time  : 2020/5/12 14:03
# @Author: Xiawang
# Description:
import re

from utils.util import get_header, json_post, get_requests, form_post


def group_invite_code():
    url = 'https://easy.lagou.com/invitation/groupInviteCode.json'
    header = get_header(url='https://easy.lagou.com/member/all_members.htm?')
    remark = '生成邀请加入公司链接'
    return json_post(url=url, headers=header, remark=remark)


def invitation_join_company(user, invite_code):
    url = f'https://easy.lagou.com/invitation/join.htm?{user}={invite_code}'
    remark = '通过邀请链接加入公司'
    r = get_requests(url=url, headers={}, remark=remark)
    try:
        userIdPasscode = re.findall('"userIdPasscode":"(.*?)"', r.text, re.S)[0]
    except IndexError:
        return ''
    return userIdPasscode


def join_with_user(userIdPasscode, invite_code):
    url = 'https://easy.lagou.com/invitation/joinWithUser.json'
    data = {
        'userIdPasscode': userIdPasscode,
        'c': invite_code
    }
    remark = '确定加入公司'
    r = form_post(url=url, data=data, remark=remark)
    if r.get('state') == 1:
        redirectUrl = r['content']['data']['redirectUrl']
    get_requests(url=redirectUrl)
    if r.get('state') == 1:
        return 1
    else:
        return 0
