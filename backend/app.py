# coding:utf-8
# @Time  : 2019-02-15 15:34
# @Author: Xiawang

from flask import Flask, config
from flask_restful import Api

from backend.app.b_end.urls import b_end_app_api
from backend.app.external_interface.urls import external_interface_app_api

from flask_cors import CORS
from flask_docs import ApiDoc

from backend.resources.b_basic_process import B_Basic_Process
from backend.resources.b_post_position import B_Post_Position
from backend.resources.c_basic_process import C_Basic_Process
from backend.resources.hello import HelloWorld
from backend.resources.run_pytest import run_Pytest

app = Flask(__name__)
app.config.from_object(config)

CORS(app)

api = Api(app)

app.config['API_DOC_MEMBER'] = ['app_api']
ApiDoc(app)

api.add_resource(HelloWorld, '/')
api.add_resource(B_Post_Position, '/postposition')
api.add_resource(B_Basic_Process, '/bbasicprocess')
api.add_resource(C_Basic_Process, '/cbasicprocess')
api.add_resource(run_Pytest, '/runpytest')

app.run(debug=True, host='0.0.0.0', port=9000)
