# coding:utf-8
# @Time  : 2018-12-29 13:02
# @Author: Xiawang
import re

import yaml
import os,ast

from api_script.entry.cuser.baseStatus import batchCancel
from api_script.home.forbid import verify_user_is_forbid, get_userId
from utils.util import login_home


def get_yaml_test_data(yamlfile):
    # 获取当前脚本所在文件夹路径
    if os.name == "nt":
        curPath = os.getcwd() + "\\tests\\testdata"
        print(curPath)
    else:
        curPath = os.getcwd() + "/tests/testdata"

    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, yamlfile)
    # open方法打开直接读出来
    cfg = open(yamlPath, 'r', encoding='utf-8').read()
    return yaml.load(cfg)  # 用load方法转字典


def get_file_path(file):
    # 获取当前脚本所在文件夹路径
    if os.name == "nt":
        curPath = os.getcwd() + "\\tests\\testdata"
        print(curPath)
    else:
        curPath = os.getcwd() + "/tests/testdata"

    # 获取yaml文件路径
    file_Path = os.path.join(curPath, file)
    return file_Path


def record_test_data(type, **kw):
    if type == 1:
        with open('/home/test/data_no_delete/c.txt', 'at') as f:
            f.write('{},'.format(kw['userId']))
    elif type == 2:
        with open('/home/test/data_no_delete/b.txt', 'at') as f:
            f.write('({},{},{}),'.format(kw['userId'], kw['UserCompanyId'], kw['lg_CompanyId']))


def record_jsessionid(file_path, jsessionid):
    with open('{}/tests/testdata/JSESSIONID.txt'.format(file_path), 'w') as f:
        f.write('{}'.format(jsessionid))

def read_jsessionid(file_path):
    with open('{}/tests/testdata/JSESSIONID.txt'.format(file_path), 'r') as f:
        jsessionid = f.read()
    return jsessionid


def record_cancel_account(userId):
    with open('/home/test/data_no_delete/account.txt', 'at') as f:
        # with open('account.txt', 'at') as f:
        f.write(f'{userId},')


def read_cancel_account():
    with open('/home/test/data_no_delete/account.txt', 'r') as f:
    # with open('account.txt', 'r') as f:
        result = re.split(',|\n', f.read())
        if result[-1] == '':
            result.remove('')
    return result


def rewrite_cancel_account():
    with open('/home/test/data_no_delete/account.txt', 'w') as f:
        f.write('')

def batch_cancel_account(country_code_phone_list):
    login_home('autotest@lagou.com', 'a52f33ba89bd7af92982da737cafc8d0')
    for country_code_phone in country_code_phone_list:
        userId = get_userId(country_code_phone)
        if userId is not None:
            result = batchCancel(userIds=userId)
            assert result.get('state') == 1

def record_shop_time(file_path, shoptime):
    with open('{}/tests/testdata/shoptime.txt'.format(file_path), 'w') as f:
        f.write('{}'.format(shoptime))


def read_shop_time(file_path):
    with open('{}/tests/testdata/shoptime.txt'.format(file_path), 'a+') as f:
        shoptime = f.read()
    return shoptime


<<<<<<< HEAD
=======

>>>>>>> master
def record_shop_order(file_path, shoporder):
    with open('{}/tests/testdata/shoporder.txt'.format(file_path), 'w') as f:
        f.write('{}'.format(shoporder))


def read_shop_order(file_path):
    with open('{}/tests/testdata/shoporder.txt'.format(file_path), 'a+') as f:
        shoporder = f.read()
    if shoporder:
        return ast.literal_eval(shoporder)  # 将读取的字符串转换为字典
    else:
        return {}


# if __name__ == '__main__':
   #  record_test_data(1, userId=123124, phone='0085220190909')
   #  record_jsessionid('fhkjashdfkasjdhkj')
   #  l = [str(i) for i in range(20190101, 20190131)]
   #  for country_code_phone in l:
   #      record_cancel_account(country_code_phone)
   #  print(read_cancel_account(),1)
   #  rewrite_cancel_account()
   # read_shop_time("2021")
   #  print(read_shop_time("D:\\lg-apiscript-python"))
   #  print(record_shop_time("D:\\lg-apiscript-python","22"))

