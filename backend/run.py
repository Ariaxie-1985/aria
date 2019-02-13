# coding:utf-8
# @Time  : 2019-02-13 16:41
# @Author: Xiawang

from flask import Flask

from backend.app import app

app.run(debug=True, host='0.0.0.0', port=9000)
