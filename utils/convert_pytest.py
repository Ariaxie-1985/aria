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
    elif method == 'POST' or method == 'PUT' or method == 'DELETE':
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

    return jsonData


'''
postman 用例编写规则

1. url, body, header, 不使用变量代替
2. 在用例名称注明测试点
3. 在 postman test断言处注释前两行，第一行写期望结果，第二行写实际结果，涉及到校验数据时，用python语法，响应结果统一为JsonData

例如
# 校验期望结果的某字段是否等于确定已知的值
// 1
// jsonData['state']

# 校验期望结果的某字段的值不为空
// True
// bool(jsonData['state'])

# 校验期望结果的某字段是否存在
// True
// bool('state' in jsonData)
'''
