# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from flask_restful import Resource, reqparse
from ApkChannelBuildTool2.startBuild import start
from ApkChannelBuildTool2.ApkBuilder import ApkBuilder
from ApkChannelBuildTool2.clear import clear
class channel_build(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('build_type', type=int,choices=(1, 2, 3, 4),help="请输入打包类型", required=True)
        # parser.add_argument('clear', type=bool, help="请输入用户的手机号", required=True)
        args = parser.parse_args()
        startobj=start()
        buildobj=ApkBuilder()
        clearobj=clear('/ApkChannelBuildTool2/android-c/Vt')
        if args['build_type']==1:
            startobj.clearTarget()
            buildobj.builder()
            startobj.clearSrc()
            return {'message':'ok'}

        elif args['build_type']==2:
            startobj.clearSrc()
            startobj.clearTarget()
            startobj.clearChannel()
            startobj.startcommon('360')
            # time.sleep(2000)
            startobj.clearChannel()
            startobj.startcommon('baidu')
            # time.sleep(2000)
            startobj.clearChannel()
            startobj.startother()
            try:
                clearobj.clearC()
            except Exception as e:
                return {'message':'2 ok,but clear Exception'}
            return {'message':'2 ok'}
