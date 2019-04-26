# -*- coding: utf-8 -*-
__author__ = 'yqzhang'
import os
import shutil


class common():

    def __init__(self):
        os.chdir('/var/backend/lg_api_script/ApkChannelBuildTool2/')
        self.srcDir =  'srcApks'
        # self.commonPath = '//file.oss.lagou.com/config/ACP/android-c/V'
        self.commonPath = './android-c/Vt'
        self.resultpath = 'targetApks'

    def getApkname(self,dirName):
        # dirName：目录名。返回值为列表
        list = os.listdir(dirName)
        apkNum = 0
        for apks in list:
            apkName = os.path.basename(apks)
            if apkName.split('.')[-1] == "apk":
                apkNum = apkNum + 1
            else:
                 list.remove(apks)
        # print(apkName)
        # print (list)
        return list

    def getVersion(self):
        apklist = self.getApkname(self.srcDir)
        apk = apklist[0]
        cmd = 'aapt d badging srcApks/'+apk
        os.chdir(os.getcwd())
        value = os.popen(cmd)
        # a=bytes(value.read())
        # print(chardet.detect(a))
        # print(value.read().decode('gbk','ignore').encode('utf-8'))
        # open(value,'rb')
        # print(s)
        sValue = value.readline()
        # print(sValue.encode('gbk'))
        version1 = sValue.split(' ')[3]
        version = version1.split('versionName=')[1]
        # version = sValue.split('versionName=')[1]
        return version

    def channelPath(self):
        apklist = self.getApkname(self.resultpath)
        for chanelApk in apklist:
            apkName = os.path.basename(chanelApk)
            if "360" in apkName:
                if "sem" in apkName or "SEM" in apkName:
                    path = self.commonPath + self.getVersion().strip("\n""''") + '/sem/360/'
                elif "feed" in apkName or "feeds" in apkName:
                    path = self.commonPath + self.getVersion().strip("\n""''") + '/new/feed/'
                else:
                    path = self.commonPath + self.getVersion().strip("\n""''") + '/other/360/'
            else:
                if "sem" in apkName or "SEM" in apkName:
                    path = self.commonPath + self.getVersion().strip("\n""''") + '/sem/baidu/'
                elif "feed" in apkName or "feeds" in apkName:
                    path = self.commonPath + self.getVersion().strip("\n""''") + '/new/feed/'
                else:
                    path = self.commonPath + self.getVersion().strip("\n""''") + '/other/baidu/'
            print(path)
            return path

    def upload(self):
        apklist = self.getApkname(self.resultpath)
        count = 0
        for chanelApk in apklist:
            apkName = os.path.basename(chanelApk)
            print (apkName)
            if apkName.split('.')[-1] == "apk":
                uploadpath = self.channelPath()
                if not os.path.exists(uploadpath):
                    os.makedirs(uploadpath)
                shutil.move('targetApks/'+apkName,uploadpath+apkName)
                count = count + 1
                print("move:",count)
        print("已上传：",count)

    def uploadother(self):
        uploadpath_new = self.commonPath +self.getVersion().strip("\n""''")+ '/new/'
        for i in self.getApkname(self.resultpath):
            if not os.path.exists(uploadpath_new):
                os.makedirs(uploadpath_new)
                shutil.move("targetApks/" + i, uploadpath_new + i)
            else:
                shutil.move("targetApks/" + i, uploadpath_new + i)


if __name__=="__main__":
    test=common()
    # test.uploadother()
    # print (test.getApkname( 'targetApks'))
    # test.getApkname('targetApks')
    print(test.getVersion())
    # test.upload()
    # a=os.system('adb')
    # print(a)

