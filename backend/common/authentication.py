# coding:utf-8
# @Time  : 2019-09-09 11:35
# @Author: Xiawang
# Description:
from flask import g
from flask_httpauth import HTTPBasicAuth
# from flask_login import LoginManager
from common.new_models import User
from app import login_manager

auth = HTTPBasicAuth()


@login_manager.user_loader
def load_user(userId):
    g.user = User.get_by_id(userId)
    return g.user


def set_password(password):
    from app import flask_bcrypt
    passwd_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
    return passwd_hash


def check_password(id, password):
    from app import flask_bcrypt
    user = User.get_by_id(id)
    try:
        result = flask_bcrypt.check_password_hash(user.password, password)
    except ValueError:
        return False
    return result


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.get(User.username == username_or_token)
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

