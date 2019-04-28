#!/usr/bin/python
# coding=utf-8
import zipfile
import sys, os, shutil

class ApkBuilder():

    def __init__(self):
        os.chdir('/var/backend/lg_api_script/ApkChannelBuildTool2/')
        self.srcDir = 'srcApks'
        self.tmpDir_sig = 'tmp_sig'
        self.tmpDir = 'tmp_align'
        self.configDir = 'config'
        self.keyDir = self.configDir + '/LagouAndroid.keystore'
        self.psw = 'zxp943128087'
        self.alias = 'lagou'
        self.outDir = 'targetApks/'

    def builder(self):
        if (os.path.exists(self.tmpDir_sig)):
            shutil.rmtree(self.tmpDir_sig)
        os.mkdir(self.tmpDir_sig)

        if (os.path.exists(self.tmpDir)):
            shutil.rmtree(self.tmpDir)
        os.mkdir(self.tmpDir)

        list = os.listdir(self.srcDir)
        for filename in list:
            fullname = os.path.join(self.srcDir, filename)
            signedname = os.path.join(self.tmpDir_sig, 'sig_' + filename)
            outname = os.path.join(self.tmpDir, filename)
            os.system(
                'jarsigner -digestalg SHA1 -sigalg MD5withRSA -keystore ' + self.keyDir + ' -storepass ' + self.psw + ' -keypass ' + self.psw + ' -signedjar ' + signedname + ' ' + fullname + ' ' + self.alias)
            os.system('/var/android-sdk-linux/build-tools/24.0.0/zipalign -f -v 4 ' + signedname + ' ' + outname)

        print('end sign...')
        print('')
        print('')
        print('start channel....')
        print('')
        srcDir = self.tmpDir + '/'
        outDir = 'targetApks/'

        # if (os.path.exists(outDir)):
        #     shutil.rmtree(outDir)
        # os.mkdir(outDir)

        # 空文件 便于写入此空文件到apk包中作为channel文件
        src_empty_file = self.configDir + '/tmp.txt'
        # 创建一个空文件（不存在则创建）
        f = open(src_empty_file, 'w')
        f.close()

        # 获取当前目录中所有的apk源包
        src_apks = []
        # python3 : os.listdir()即可，这里使用兼容Python2的os.listdir('.')
        # for file in os.listdir('.'):
        for file in os.listdir(srcDir):
            if os.path.isfile(srcDir + file):
                extension = os.path.splitext(file)[1][1:]
                if extension in 'apk':
                    src_apks.append(srcDir + file)

        # print (src_apks)
        # 获取渠道列表
        channel_file = self.configDir + '/channel.txt'
        f = open(channel_file)
        lines = f.readlines()
        f.close()

        for src_apk in src_apks:
            # file name (with extension)
            src_apk_file_name = os.path.basename(src_apk)
            # 分割文件名与后缀
            temp_list = os.path.splitext(src_apk_file_name)
            # name without extension
            src_apk_name = temp_list[0]
            # 后缀名，包含.   例如: ".apk "
            src_apk_extension = temp_list[1]

            # 创建生成目录,与文件名相关
            # output_dir = 'output_' + src_apk_name + '/'
            # output_dir = 'unsigned/'
            output_dir = outDir
            # 目录不存在则创建
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)

            allCount = len(lines)
            print('channel need count = ' + str(allCount))
            count = 0
        # 遍历渠道号并创建对应渠道号的apk文件
            for line in lines:
            # 获取当前渠道号，因为从渠道文件中获得带有\n,所有strip一下
                target_channel = line.strip()
            # 拼接对应渠道号的apk
                target_apk = output_dir + src_apk_name + "_" + target_channel + src_apk_extension
            # 拷贝建立新apk
                shutil.copy(src_apk, target_apk)
            # zip获取新建立的apk文件
                zipped = zipfile.ZipFile(target_apk, 'a', zipfile.ZIP_DEFLATED)
            # 初始化渠道信息
                empty_channel_file = "META-INF/lagouchannel_{channel}".format(channel=target_channel)
            # 写入渠道信息
                zipped.write(src_empty_file, empty_channel_file)
            # 关闭zip流
                zipped.close()
            # 渠道成功则自增
                count = count + 1
            # 不是很准确，应该读取channel标识并进行比对方可确定成功
            print('channel success count = ' + str(count))
            print('channel fail count = ' + str(allCount - count))

        if (os.path.exists(self.tmpDir)):
            shutil.rmtree(self.tmpDir)
        if (os.path.exists(self.tmpDir_sig)):
            shutil.rmtree(self.tmpDir_sig)

        print('')
        print('end channel....')

    def clear_target(self):
        if (os.path.exists(self.outDir)):
            shutil.rmtree(self.outDir)
        os.mkdir(self.outDir)

if __name__=="__main__":
    test = ApkBuilder()
    test.builder()
    # test.clear_target()
