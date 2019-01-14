# coding:utf-8
# @Time  : 2019-01-08 18:59
# @Author: Xiawang
from flask import Flask, config

from backend.app.b_end.urls import app_api

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(blueprint=app_api)
