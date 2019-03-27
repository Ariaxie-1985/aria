# coding:utf-8
# @Time  : 2019-03-26 17:15
# @Author: Xiawang
import json

file_path = '/Users/wang/Downloads/言职社区通知页优化需求.postman_collection.json'


def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
    except:
        return "文件找不到, 请确认路径是否正确"


def parser(data):
    while len(data['item']):
        for t in data['item']:
            if 'item' in t:
                pass
            else:
                pass
    else:
        return "请确认是否有用例"






r = read_json()
print(r)
