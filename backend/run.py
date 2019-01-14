# coding:utf-8
# @Time  : 2019-01-09 14:41
# @Author: Xiawang
from flask import Flask

from backend.app import app

app.run(debug=True, host='0.0.0.0', port=9000)
