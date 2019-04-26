# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
import os
class upload(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('file', type=FileStorage,help="请上传文件", location='files',required=True)
        parser.add_argument('path', type=str, help="上传path", required=True)
        args = parser.parse_args()
        f=args['file']
        f.save(os.path.join(args['path'],f.filename))
        return {'state':1,'message':'upload ok'}