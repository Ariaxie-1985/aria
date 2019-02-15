# coding:utf-8
# @Time  : 2019-01-08 18:59
# @Author: Xiawang
from flask import Flask, config
from flask_docs import ApiDoc

from backend.app.b_end.urls import app_api

app = Flask(__name__)
app.config.from_object(config)

app.config['API_DOC_MEMBER'] = ['app_api']

ApiDoc(app)

app.register_blueprint(blueprint=app_api)
