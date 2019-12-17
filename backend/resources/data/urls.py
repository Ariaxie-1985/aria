# coding:utf-8
# @Time  : 2019-09-16 10:53
# @Author: Xiawang
# Description:


from flask_restful import Api

from backend.resources.data import data
from backend.resources.data.app_post_position import app_post_position
from backend.resources.data.app_process_resume import app_process_resume
from backend.resources.data.b_add_people_into_company import B_Add_People_Into_Company
from backend.resources.data.b_basic_process import B_Basic_Process
from backend.resources.data.b_post_position import B_Post_Position
from backend.resources.data.b_process_resume import b_process_resume
from backend.resources.data.c_basic_process import C_Basic_Process
from backend.resources.data.channel_build import channel_build
from backend.resources.data.company_user_resume import getInfo
from backend.resources.data.contract_data_import import Contract_Data_Import
from backend.resources.data.download import download
from backend.resources.data.get_userid import getUserId
from backend.resources.data.get_mainprocess_report import GetReport
from backend.resources.data.hello import HelloWorld
from backend.resources.data.new_lagouPlus_open_product import openProduct
from backend.resources.data.operation_resume import getResume
from backend.resources.data.product_template import productTemplate
from backend.resources.data.registe import registe
from backend.resources.data.run_pytest import run_Pytest
from backend.resources.data.submit_resume_to_position import submit_Resume_To_Position
from backend.resources.data.upload import upload
from backend.resources.data.work_address import work_address

api = Api(data)

api.add_resource(HelloWorld, '/')
api.add_resource(B_Post_Position, '/jianzhao/position')
api.add_resource(B_Basic_Process, '/jianzhao/company/registration')
api.add_resource(B_Add_People_Into_Company, '/jianzhao/personal/registration')
api.add_resource(submit_Resume_To_Position, '/customer/resume')
api.add_resource(C_Basic_Process, '/customer/registration')
api.add_resource(run_Pytest, '/pytest')
api.add_resource(b_process_resume, '/jianzhao/resume')
api.add_resource(app_process_resume, '/bapp/resume')
api.add_resource(app_post_position, '/bapp/position')
api.add_resource(Contract_Data_Import, '/home/import')
api.add_resource(getUserId, '/customer')
api.add_resource(getResume, '/customer/resumedata')
api.add_resource(channel_build, '/build')
api.add_resource(upload, '/upload')
api.add_resource(download, '/download')
api.add_resource(registe, '/entry/registration')
api.add_resource(work_address, '/jianzhao/address')
api.add_resource(openProduct, '/home/product')
api.add_resource(productTemplate, '/home/product/template')
api.add_resource(getInfo, '/person/info')
api.add_resource(GetReport,'/mainprocess/report')
import backend.resources.user.urls
