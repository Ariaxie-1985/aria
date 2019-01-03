
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import  logging
import requests
import  urllib.request
import sys
type = sys.getfilesystemencoding()

logging.getLogger().setLevel(logging.INFO)
session = requests.session()
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


#解析html文件

#通过class-name 获取属性，来判断是否存在改标签
def exist_class_name(html,classname):
    soup=BeautifulSoup(html,"html.parser")
    a=soup.find_all("a",attrs={"class":classname})
   # print(a.__len__())
    if a.__len__()==0:
        logging.info("不存在该标签")
        return  True
    else:
        logging.info("存在该标签")
        return False

'''
通过class获得标签里某个具体的值
'''
def find_classname(html,class_name,key):
    soup=BeautifulSoup(html,"html.parser")
    print(soup)
    key=soup.find_all('li',attrs={'class':'position-list-item'})
    print(key)
    return key