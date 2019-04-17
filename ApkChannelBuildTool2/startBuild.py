# -*- coding: utf8 -*-
__author__ = 'yqzhang'
import time
import shutil
import os
from ApkChannelBuildTool2.clear import clear
from ApkChannelBuildTool2.getChannel import getXlrdchannel
from ApkChannelBuildTool2.common import common
from ApkChannelBuildTool2.ApkBuilder import ApkBuilder
from ApkChannelBuildTool2.getChannel import getOtherchannel
from retry import retry


class start():

    def __init__(self):
        os.chdir(os.getcwd()+'/ApkChannelBuildTool2')
        self.jiagu = "/common jiaguapk"
        self.list = os.listdir(self.jiagu)
        self.builderobj = ApkBuilder()
        self.commonobj = common()
        self.getXlrdchannelobj = getXlrdchannel()
        self.ApkBuilderobj = ApkBuilder()
        self.getOtherchannelobj = getOtherchannel()
        self.otherjiaguapk = "/other jiaguapk"
        # self.clearChannel()

    @retry(tries=3)
    def clearSrc(self):
        if (os.path.exists("srcApks")):
            shutil.rmtree("srcApks")
        os.mkdir("srcApks")

    @retry(tries=3)
    def clearTarget(self):
        self.builderobj.clear_target()

    def clearChannel(self):
        if (os.path.exists("config/channel.txt")):
            os.remove("config/channel.txt")
            file = open("config/channel.txt","w")
            file.close()
        else:
            file = open("config/channel.txt", "w")
            file.close()

    @retry(tries=3)
    def startcommon(self,jiaguchannel):
        for i in self.commonobj.getApkname(self.jiagu):
            if  jiaguchannel in i:
                shutil.move(self.jiagu + "/" + i, "srcApks/" + i)
                for j in range(len(self.getXlrdchannelobj.getSheets())):
                    channel=self.getXlrdchannelobj.readChannel(j)
                    self.getXlrdchannelobj.writeChannel(channel,"a")
                self.ApkBuilderobj.builder()
                self.commonobj.upload()
                time.sleep(2)
                shutil.rmtree("srcApks")
                os.mkdir("srcApks")
            else:
                print("no "+jiaguchannel+" apk")

    @retry(tries=3)
    def startother(self):
        list = self.commonobj.getApkname(self.otherjiaguapk)

        for apks in list:
            shutil.move(self.otherjiaguapk + "/" + apks, "srcApks/" + apks)
            self.getOtherchannelobj.writeOtherchannel(self.getOtherchannelobj.readOtherchannel())
            self.ApkBuilderobj.builder()
            self.commonobj.uploadother()
            time.sleep(2)
            shutil.rmtree("srcApks")
            os.mkdir("srcApks")
            time.sleep(1.5)


if __name__=="__main__":


    test = start()
    test.clearTarget()
    test.clearSrc()
    # 初始化srcApks文件夹
    # test.startcommon("360")
    # 批量执行common360
    test.clearChannel()
    # 初始化渠道文件
    # test.startcommon("baidu")
    # 批量执行commom百度
    test.startother()
    # 批量执行非common包

    try:
        clear = clear("//file.oss.lagou.com/config/ACP/android-c/")
        clear.clearC()
    except Exception as e:
        print(u"无需清理或者有其他错误",e)
    else:
        print(u"清理成功")
