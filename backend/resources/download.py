# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from flask_restful import Resource, reqparse
from flask import send_from_directory
import os,zipfile
class download(Resource):
    def get(self):

        # parser = reqparse.RequestParser()
        zipf = zipfile.ZipFile('channelapks.zip', 'w')
        pre_len = len(os.path.dirname('/var/backend/lg_api_script/ApkChannelBuildTool2/targetApks'))
        print(pre_len)
        for parent, dirnames, filenames in os.walk('/var/backend/lg_api_script/ApkChannelBuildTool2/targetApks'):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
                zipf.write(pathfile, arcname)
        zipf.close()

        if os.path.isfile('/var/backend/lg_api_script/channelapks.zip'):
            return send_from_directory('/var/backend/lg_api_script/','channelapks.zip',as_attachment=True)
            #return{'message':'ok'}
        else:
            return{'message':'error'}
