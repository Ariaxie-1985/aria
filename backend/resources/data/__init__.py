# coding:utf-8
# @Time  : 2019-09-16 10:51
# @Author: Xiawang
# Description:


from flask import Blueprint

data = Blueprint('data', __name__, url_prefix='/data')

import backend.resources.data.urls
