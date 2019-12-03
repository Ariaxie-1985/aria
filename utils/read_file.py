# coding:utf-8
# @Time  : 2018-12-29 13:02
# @Author: Xiawang

import yaml
import os


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
        with open('/Users/wang/Desktop/lg-project/lg_api_script/tests/test_B_enter/testdata_no_delete_Xiawang_c.txt', 'at') as f:
            f.write('{},'.format(kw['userId']))
    elif type == 2:
        with open('/Users/wang/Desktop/lg-project/lg_api_script/tests/test_B_enter/testdata_no_delete_Xiawang_b.txt', 'at') as f:
            f.write('({},{},{}),'.format(kw['userId'], kw['UserCompanyId'], kw['lg_CompanyId']))


if __name__ == '__main__':
    record_test_data(1, userId=123124, phone='0085220190909')
