# coding:utf-8
# @Time  : 2019-09-01 23:44
# @Author: Xiawang
# Description:
from flask_login import UserMixin
from peewee import *
import datetime
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask_bcrypt import generate_password_hash, check_password_hash

mysql_db = MySQLDatabase('testing_platform', user='lagourw', password='JUY#*f2349Kl',
                         host='10.1.200.166', port=3306)


class BaseModel(Model):
    class Meta:
        database = mysql_db


class User(BaseModel, UserMixin):
    username = CharField(max_length=20)
    position = CharField(max_length=20)
    password_hash = CharField()
    email = CharField(max_length=50)
    update_time = DateTimeField(default=datetime.datetime.now)
    create_time = DateTimeField()

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password).decode('utf-8')
        return self.password_hash

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=60 * 60 * 24 * 30):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            # valid token, but expired
            return None
        except BadSignature:
            # invalid token
            return None
        user = User.get_by_id(data['id'])
        return user


class TestSheet(BaseModel):
    title = CharField()
    qa_id = IntegerField()
    status = CharField(max_length=10, default='待部署')
    backend_id = IntegerField(null=True)
    backend_content = TextField(null=True)
    front_id = IntegerField(null=True)
    front_content = TextField(null=True)
    content = TextField(null=True)
    update_time = DateTimeField(default=datetime.datetime.now)
    create_time = DateTimeField(default=datetime.datetime.now)


if __name__ == '__main__':
    mysql_db.connect()
    mysql_db.create_tables([TestSheet, User])
    # xia = User(username='Xiawang', position='测试', password='123456',email='Xiawang@sina.com')
    # result = xia.save()
    # person, created = Person.get_or_create(
    #     first_name=first_name,
    #     last_name=last_name,
    #     defaults={'dob': dob, 'favorite_color': 'green'})
    # email_info = User.get_or_createt(User.email == '4234234234')
    # email_info = User.select().where(User.email == '3
    # 23432423')
    # user, created = User.get_or_create(email='Xiawang@sina.com',
    #                                    defaults={'username': '2423', 'position': '测试', 'password': '342423423'})
    # print(user, created)
    # result = User.get(User.username == 'yqzhang1')
    # result = User.select().where(User.username == '423423').get()
    # for r in result:
    # print(r.position)
    # user = User.get_or_none(User.username == 'Royliu')
    # print(user)
    # testsheet_info = TestSheet.select().where(TestSheet.id == 1).dicts()
    # for row in testsheet_info:
    #     print(row)
    # xia = User.create(username='Xiawang',position='测试', password='123456', email='Xiawang@lagou.com')
    # xia.id = 3
    # import json
    # result = User.get_by_id(1)
    # print(json.dumps(result))
    # print(model_to_dict(result))
    # xia = User.update({User.position: '测试', User.email:'Xiawang@lagou.com'}).where(User.username == 'Xiawang')
    # xia.password = '34234235'
    # result = xia.execute()
    # testsheet_model = TestSheet.get_by_id(1)
    # result = model_to_dict(testsheet_model)
    # json_data = json.dumps(model_to_dict(testsheet_model))
    # result['update_time'] = result['update_time'].strftime("%Y-%m-%d %H:%M:%S")
    # result['create_time'] = result['create_time'].strftime("%Y-%m-%d %H:%M:%S")
    # print(update_time)
    # result['create_time'] = create_time
    # result['update_time'] = update_time
    # result = json.load(result)
    # for t in TestSheet.select().join(User).where(TestSheet.title % '%功能%', User.id == 2).order_by(
    #         TestSheet.create_time.desc()).paginate(1, 10):
    #     new_model_dict = model_to_dict(t)
    #     print(new_model_dict['qa_id'])
    # result = User.get_or_none(User.id == 2).username
    # print(result)
    # for t in TestSheet.select().join(User).where(User.id )
    # results = TestSheet.get_or_none(TestSheet.qa_id == 2, TestSheet.status == '待部署')
    # print(results)
