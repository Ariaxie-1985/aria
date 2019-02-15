# coding:utf-8
# @Time  : 2019-01-08 18:59
# @Author: Xiawang
from flask import Flask,config

from backend.app.b_end.urls import b_end_app_api
from backend.app.external_interface.urls import external_interface_app_api

from flask_cors import CORS
from flask_docs import ApiDoc
app = Flask(__name__)
app.config.from_object(config)
CORS(app)

app.config['API_DOC_MEMBER'] = ['app_api']

ApiDoc(app)
app.register_blueprint(blueprint=b_end_app_api)
app.register_blueprint(blueprint=external_interface_app_api)
