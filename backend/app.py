# coding:utf-8
# @Time  : 2019-02-15 15:34
# @Author: Xiawang
import sys

sys.path.append('.')
from flask import Flask, config
from flask_restful import Api

from flask_cors import CORS
from flask_docs import ApiDoc

from backend.resources.b_basic_process import B_Basic_Process
from backend.resources.b_post_position import B_Post_Position
from backend.resources.c_basic_process import C_Basic_Process
from backend.resources.b_add_people_into_company import B_Add_People_Into_Company
from backend.resources.hello import HelloWorld
from backend.resources.run_pytest import run_Pytest
from backend.resources.b_process_resume import b_process_resume
from backend.resources.submit_resume_to_position import submit_Resume_To_Position
from backend.resources.app_process_resume import app_process_resume
from backend.resources.app_post_position import app_post_position

app = Flask(__name__)
app.config.from_object(config)

CORS(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

app.config['API_DOC_MEMBER'] = ['api', 'platform']
ApiDoc(app)

api.add_resource(HelloWorld, '/')
api.add_resource(B_Post_Position, '/jianzhao/position')
api.add_resource(B_Basic_Process, '/jianzhao/company/registration')
api.add_resource(B_Add_People_Into_Company, '/jianzhao/personal/registration')
api.add_resource(submit_Resume_To_Position, '/customer/resume')
api.add_resource(C_Basic_Process, '/customer/registration')
api.add_resource(run_Pytest, '/pytest')
api.add_resource(b_process_resume,'/jianzhao/resume')
api.add_resource(app_process_resume,'/bapp/resume')
api.add_resource(app_post_position,'/bapp/position')

app.run(debug=True, host='0.0.0.0', port=9004)
