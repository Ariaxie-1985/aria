# -*- coding: utf8 -*-
__author__ = 'yqzhang'
import xlrd
from ApkChannelBuildTool2.common import common
from time import strftime, localtime
xlrd.Book.encoding = "gbk"

class getXlrdchannel():
    def __init__(self):
        # self.day = strftime("%d",localtime())
        # self.mon = strftime("%m",localtime())
        # self.xlsfile =  self.mon + self.day + r'.xlsx'
        self.xlsfile = 'channel.xlsx'
        self.book = xlrd.open_workbook(self.xlsfile)
        self.path = "config/channel.txt"
        self.srcDir = 'srcApks'
        self.commonobj = common()


    def getSheets(self):
        # return len(self.book.sheet_names())
        return self.book.sheet_names()

    def readChannel(self,sheetNum):
        sheet_name = self.book.sheet_names()[sheetNum]
        print(sheet_name)
        sheet = self.book.sheet_by_name(sheet_name)
        row_data = sheet.row_values(0)
        for i in row_data:
            if u"渠道标识" in i:
                print (i)
                x=row_data.index(i)
                col_data = sheet.col_values(x)[1:]
                print(col_data)
            elif u"打包注意事项" in i:
                print(i)
                x = row_data.index(i)
                col_data1 = sheet.col_values(x)[1:]
                print(col_data1)
        dic=dict(zip(col_data,col_data1))
        return dic


    def writeChannel(self,dic,writetype):
        # dic:字典类型的渠道表，readChannel（）返回；writetype：写入类型，为“a”时不覆盖txt文件中已有渠道，为“w”时覆盖已有渠道
        y=0
        list = self.commonobj.getApkname(self.srcDir)
        # apkName = ['lagouapk-7.1.1-name_zpzgz-360.apk']
        if "baidu" in list[0]:
            fo = open(self.path, writetype)
            for key in dic:
                if u"百度加固" in dic[key]:
                    y = y + 1
                    fo.write(key)
                    fo.write("\n")
            fo.close()
            print("baidu num:",y)
        elif "360" in list[0]:
            fo = open(self.path, writetype)
            for key in dic:
                if u"360加固" in dic[key] or u"自由" in dic[key]:
                    y = y + 1
                    fo.write(key)
                    fo.write("\n")
            fo.close()
            print("360 num:",y)


class getOtherchannel():
    def __init__(self):
        self.xlsfile = "OtherChannel.xlsx"
        self.book = xlrd.open_workbook(self.xlsfile)
        self.channelpath = "config/channel.txt"
        self.otherjiaguapk = "other jiaguapk"
        self.commonobj = common()
        self.getXlrdchannelobj = getXlrdchannel()

    def readOtherchannel(self):
        sheet = self.book.sheet_by_index(0)
        row_data = sheet.row_values(0)
        for i in row_data:
            if u"包名关键字" in i:
                # print(i)
                x = row_data.index(i)
                col_data = sheet.col_values(x)[1:]
            elif u"渠道号" in i:
                # print(i)
                x = row_data.index(i)
                col_data1 = sheet.col_values(x)[1:]
                # print(col_data1)
        dic = dict(zip(col_data, col_data1))
        # print(dic)
        return dic

    def writeOtherchannel(self,dic):
        apkName = self.commonobj.getApkname("srcApks")
        # print(dic)
        for i in dic:
            keyword = i.split(",")
            channel = dic[i].split(u"，")
            # print(keyword)
            # print(channel)
            if keyword[0] in apkName[0] and keyword[1] in apkName[0]:
                fo = open(self.getXlrdchannelobj.path, "w")
                for j in channel:
                    # print(j)
                    fo.write(j)
                    fo.write("\n")
                fo.close()
            # else:
            #     print("no")



if __name__ == '__main__':
    # test2=common()
    test=getOtherchannel()
    dic=test.readOtherchannel()
    # print(dic)
    test.writeOtherchannel(dic)
    # print (test.getSheets())
    # print (test.readChannel(1))
    # a=test.readChannel(1)
    # test.writeChannel(a)