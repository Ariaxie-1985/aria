# coding:utf-8
from bs4 import BeautifulSoup
import  logging
import requests
import  urllib

logging.getLogger().setLevel(logging.INFO)

#解析html文件

#通过class-name 获取属性，来判断是否存在改标签
def exist_class_name(url):
    page=urllib.urlopen()
    html=page.read()
    soup=BeautifulSoup(html,"html.parser")
    a=soup.findAll("a","batch-handle-btn ")
    print(a)
