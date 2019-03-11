# coding:utf-8
# @Time  : 2019-02-15 15:44
# @Author: cloudyyuan
import pymysql
from flask_restful import Resource, reqparse
class user_list(Resource):
    '''
    插入并查询
    '''
    def post(self):
        '''

        :param self:
        :return:
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help="请输入用户名", required=True)
        parser.add_argument('role', type=str, help="请输入角色", required=True)
        parser.add_argument('account', type=str, help="请输入名称", required=True)
        args = parser.parse_args()
        print(args['username']+"??????????????????????")
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123456',
            db='test',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        cur = conn.cursor()
        print(1)
        cur.execute("INSERT INTO userlist (userid,username,role,account) VALUES ( NULL,'%s','%s','%s')" % (args['username'],args['role'],args['account']))
        conn.commit()
        conn.close()
        status=1
        return status
    def get(self):
        '''
        获取所有数据
        :return:
        '''
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123456',
            db='test',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM userlist")
        results=cur.fetchall()
        conn.commit()
        print(results)
        conn.close()

        return results


