# coding:utf-8
# @Time  : 2019-01-09 11:54
# @Author: Xiawang

# 设计数据模型
from datetime import datetime
from backend.exts import db


class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	telephone = db.Column(db.String(11), nullable=False)
	username = db.Column(db.String(50), nullable=False)
	password = db.Column(db.String(100), nullable=False)


class Results(db.Model):
	__tablename__ = 'results'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	url = db.Column(db.String(100), nullable=False)
	requestsdata = db.Column(db.Text, nullable=False)
	headers = db.Column(db.Text, nullable=True)
	remark = db.Column(db.Text, nullable=False)
	create_time = db.Column(db.DateTime, default=datetime.now)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	executive = db.relationship('User', backref=db.backref('results'))
