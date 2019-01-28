# coding:utf-8
# @Time  : 2019-01-16 17:21
# @Author: Xiawang
import os
import subprocess

os.chdir('..')

subprocess.call("pipenv shell", shell=True)
subprocess.call("pytest tests/test_app_b_position.py", shell=True)
