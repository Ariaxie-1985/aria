# coding:utf-8
# @Time  : 2019-03-26 17:15
# @Author: Xiawang
import json
import os
import re

import requests

from utils.util import get_requests, form_post, get_app_header, assert_equal, json_post
requests.packages.urllib3.disable_warnings()

def read_json(jsonfile):
    if os.name == "nt":
        curPath = os.getcwd() + "\\tests\\test_postman_script\\testcase"
    else:
        curPath = os.getcwd() + "/tests/test_postman_script/testcase"
        # curPath = os.getcwd() + "/testcase"
    jsonPath = os.path.join(curPath, jsonfile)
    try:
        with open(jsonPath, 'r') as f:
            data = json.load(f)
            return data
    except BaseException:
        return "文件找不到, 请确认路径是否正确"


def parser(data):
    # case_list = []
    if isinstance(data['item'], list):
        for t in data['item']:
            url = t['request']['url']['raw']
            method = t['request']['method']
            header_list = t['request']['header']
            content_type = None
            for h in header_list:
                if not ("disabled" in h):
                    if h['key'] == "X-L-USER-ID":
                        userId = h['value']
                    elif h['key'] == "Content-Type":
                        content_type = h['value']

            header = get_app_header(userId)
            body = t['request']['body']
            remark = t['name']
            try:
                expect_res = ''.join(
                    re.split(
                        '[// ]',
                        t['event'][0]['script']['exec'][0]))
            except BaseException:
                return "缺失期望结果"

            try:
                expect_res = eval(expect_res)
            except NameError:
                expect_res = expect_res
            try:
                actual_res = ''.join(
                    re.split(
                        '[// ]',
                        t['event'][0]['script']['exec'][1]))
            except BaseException:
                return "缺失实际结果"
            # case = (url, method, content_type, header, body, remark, expect_res, actual_res)
            # case_list.append(case)
            yield url, method, content_type, header, body, remark, expect_res, actual_res
    else:
        return "请检查用例数据"


def run_case(
        url,
        method,
        content_type,
        header,
        body,
        remark):
    if method == 'GET':
        jsonData = get_requests(
            url=url, headers=header, remark=remark).json()
    elif method == 'POST':
        if content_type == 'application/x-www-form-urlencoded':
            requets_data = dict()
            for i in body['urlencoded']:
                requets_data[i['key']] = i['value']

            jsonData = form_post(
                url=url,
                data=requets_data,
                headers=header,
                remark=remark)
        elif content_type == 'application/x-www-form-urlencoded':
            requets_data = json.loads(body['raw'])
            jsonData = json_post(
                url=url,
                data=requets_data,
                headers=header,
                remark=remark)
        else:
            jsonData = form_post(url=url, headers=header, remark=remark)
    elif method == 'PUT':
        if content_type == 'application/x-www-form-urlencoded':
            requets_data = dict()
            for i in body['urlencoded']:
                requets_data[i['key']] = i['value']

            jsonData = form_post(
                url=url,
                data=requets_data,
                headers=header,
                remark=remark)
        elif content_type == 'application/x-www-form-urlencoded':
            requets_data = json.loads(body['raw'])
            jsonData = json_post(
                url=url,
                data=requets_data,
                headers=header,
                remark=remark)
        else:
            jsonData = form_post(url=url, headers=header, remark=remark)
    elif method == 'DELETE':
        if content_type == 'application/x-www-form-urlencoded':
            requets_data = dict()
            for i in body['urlencoded']:
                requets_data[i['key']] = i['value']

            jsonData = form_post(
                url=url,
                data=requets_data,
                headers=header,
                remark=remark)
        elif content_type == 'application/json':
            requets_data = json.loads(body['raw'])
            jsonData = json_post(
                url=url,
                data=requets_data,
                headers=header,
                remark=remark)

        else:
            jsonData = form_post(url=url, headers=header, remark=remark)

    return jsonData


# data = read_json(
#     '/Users/wang/Desktop/lg-project/lg_api_script/tests/test_postman_script/testcase/言职社区通知页优化需求.postman_collection.json')
#
#
# for url, method, content_type, header, body, remark, expect_res, actual_res in parser(data):
#     run_case(url, method, content_type, header, body, remark)
#     assert_equal(expect_res, eval(actual_res), ''.join(
#         [remark, ' 用例通过']), ''.join([remark, ' 用例失败']))

'''
postman 用例编写规则

1. url, body, header, 尽量不使用变量代替
2. 在用例名称注明测试点
'''
