# coding:utf-8
# @Time  : 2019-01-08 18:58
# @Author: Xiawang

# 配置文件，数据库配置，项目的debug模式
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = '10.1.200.127'
PORT = '3306'
DATABASE = 'lagou_resume'
USERNAME = 'lagourw'
PASSWORD = 'JUY#*f2349Kl'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False