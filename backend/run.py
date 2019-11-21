# coding:utf-8
# @Time  : 2019-11-21 16:15
# @Author: Xiawang
# Description:
from backend.app import create_app

app = create_app()
app.run(host='127.0.0.1', port=18980)
