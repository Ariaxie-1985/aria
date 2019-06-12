# coding:utf-8
# @Time  : 2019-06-12 12:37
# @Author: Xiawang

from flask_restful import Resource, reqparse
import pymysql

db = pymysql.connect(
    host='10.1.200.166',
    port=3306,
    user='lagouro',
    passwd='Q12_#*s#$opIx',
    db='mds_position',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = db.cursor()


class work_address(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('address1', type=int, help="请输入正确手机号", required=True)
        parser.add_argument('address2', type=int, help="请输入正确手机号", required=True)
        parser.add_argument('province', type=str, help="请输入正确手机号", required=True)
        args = parser.parse_args()
        db.ping(reconnect=True)
        cursor.execute(
            "SELECT id, province,city,district,detail_address FROM t_work_address where {} <= id and id <= {} and province = '{}'".format(
                args['address1'], args['address2'], args['province']))
        results = cursor.fetchall()
        db.close()
        return results
