# coding:utf-8
# @Author: Xiawang

from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')

import backend.resources.user.urls
