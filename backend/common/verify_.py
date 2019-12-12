# coding:utf-8
# @Time  : 2019-08-27 11:45
# @Author: Xiawang
# Description:
from backend.common.new_models import User


def verify_user(username):
    if username == "" or username is None:
        return None
    try:
        user = User.get(User.username == username)
        return user.id
    except:
        return 0


def verify_remark(remark):
    if remark == "" or remark is None:
        remark = ""
    else:
        remark = remark
    return remark


def verify_negative_number(number, expect):
    if str(number)[0] != '-':
        return number
    else:
        return expect


def verify_title(title):
    if title == "" or title is None:
        title = ""
    else:
        title = title
    return title
