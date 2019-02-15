# coding:utf-8
# @Time  : 2019-02-15 10:30
# @Author: Xiawang

from flask import Blueprint
from flask_restful import Api
from backend.app.external_interface.views import run_Pytest

external_interface_app_api = Blueprint(name="external_interface", import_name=__name__)
restful_api = Api(external_interface_app_api)

restful_api.add_resource(run_Pytest, "/runpytest")
