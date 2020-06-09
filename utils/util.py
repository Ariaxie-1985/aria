# coding:utf-8
import os
import sys
import time
import zipfile
from datetime import datetime
import datetime
from urllib.parse import urlparse

import pysnooper
import requests
import re
from requests import RequestException
import json
import logging

from utils.loggers import logers
from utils.mainprocess_api_developer import return_api_developer
from utils.user_exception import Http500Error

sys.path.append(os.path.dirname(__file__))

logging.getLogger().setLevel(logging.INFO)

requests.packages.urllib3.disable_warnings()
session = requests.session()

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
app_header = {
    'User-Agent': '%E6%8B%89%E5%8B%BE%E6%8B%9B%E8%81%98/7988 CFNetwork/978.0.7 Darwin/18.5.0'
}

count = 0

loger = logers()


# 获取页面的token和code
def get_code_token(url, referer=False, ip_port=None):
    global count
    try:
        token_values, code_values = 0, None
        if ip_port is None:
            code = session.get(url=url, headers=header, verify=False, timeout=60)
        else:
            ip_port_url = domain_convert_ip_port(url=url, ip_port=ip_port)
            code = session.get(url=ip_port_url, headers=header, verify=False, timeout=60)
            with open('/home/test/1.log', 'w') as f:
                f.write(code.text)
        token_values = re.findall("X_Anti_Forge_Token = '(.*?)'", code.text, re.S)[0]
        code_values = re.findall("X_Anti_Forge_Code = '(.*?)'", code.text, re.S)[0]
        if referer == False:
            headers = {"X-Anit-Forge-Code": code_values, "X-Anit-Forge-Token": token_values,
                       'Referer': url,
                       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3615.0 Safari/537.36"}
        else:
            headers = {"X-Anit-Forge-Code": code_values, "X-Anit-Forge-Token": token_values,
                       'referer': 'www.lagou.com',
                       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3615.0 Safari/537.36"}
        if token_values != '' and code_values != '':
            return headers
        else:
            if count < 1:
                count = count + 1
                return get_code_token(url=url)
            else:
                return headers
    except (RequestException, IndexError):
        return get_code_token(url=url)


def form_post(url, remark, data=None, files=None, headers={}, verifystate=True, allow_redirects=True, ip_port=None):
    """
    form表单传参的post请求
    :param url: 请求url
    :param remark: str, 备注
    :param data: dict, 请求数据
    :param headers: dict, 请求header
    :return: json格式化的响应结果
    """
    global count
    if verifystate == False:
        count = 3
    try:
        if not data is None:
            headers = {**header, **headers, **{'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}}
        else:
            headers = {**header, **headers}
        if ip_port is None:
            response = session.post(url=url, data=data, files=files, headers=headers, verify=False,
                                    timeout=60,
                                    allow_redirects=allow_redirects)
        else:
            ip_port_url = domain_convert_ip_port(url=url, ip_port=ip_port)
            response = session.post(url=ip_port_url, data=data, files=files, headers=headers, verify=False,
                                    timeout=60,
                                    allow_redirects=allow_redirects)
        pard_id = response.headers.get('Pard-Id', 0)
        status_code = response.status_code
        if 200 <= status_code <= 302:
            if is_json_response(response):
                response_json = convert_response(response)
                if response_json.get('state', 0) == 1 or response_json.get('success', False) or (not response_json.get(
                        'code', 1)):
                    logging.info(f'该接口URL {url} ,备注 {remark} 执行成功\n')
                    return response_json
                else:
                    if count < 1:
                        count = count + 1
                        return form_post(url=url, headers=headers, remark=remark, data=data)
                    else:
                        logging.error(
                            msg='该接口URL {} , 备注: {},  响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                        return response_json
            else:
                return convert_response(response)
        else:
            if count < 1:
                count = count + 1
                return form_post(url=url, headers=headers, remark=remark, data=data)
            else:
                return judging_other_abnormal_conditions(status_code, url, remark, pard_id)
    except RequestException:
        logging.error("该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark))
        return {'content': '请求异常(requests捕获的异常)', 'url': url, 'remark': remark}


# @pysnooper.snoop()
def json_post(url, remark, data=None, headers={}, app=False, verifystate=True, ip_port=None):
    """
    json传参的post请求
    :param url: 请求url
    :param remark: str, 备注
    :param data: dict, 请求数据
    :param headers: dict, 请求header
    :return: json格式化的响应结果
    """
    global count
    if verifystate == False:
        count = 3
    if app == False:
        headers = {**header, **headers, **{'Content-Type': 'application/json;charset=UTF-8'}}
    try:
        if ip_port is None:
            response = session.post(url=url, json=data, headers=headers, verify=False, timeout=60)
        else:
            ip_port_url = domain_convert_ip_port(url=url, ip_port=ip_port)
            response = session.post(url=ip_port_url, json=data, headers=headers, verify=False,
                                    timeout=60)
        pard_id = response.headers.get('Pard-Id', 0)
        status_code = response.status_code
        if 200 <= status_code <= 302:
            if is_json_response(response):
                response_json = convert_response(response)
                if response_json.get('state', 0) == 1 or response_json.get('success', False):
                    logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                    return response_json
                else:
                    if count < 1:
                        count = count + 1
                        return json_post(url=url, headers=headers, remark=remark, data=data)
                    else:
                        logging.error(
                            msg='该接口URL {} , 备注 {}, 响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                        return response_json
            else:
                return convert_response(response)
        else:
            if count < 1:
                count = count + 1
                return json_post(url=url, headers=headers, remark=remark, data=data)
            else:
                return judging_other_abnormal_conditions(status_code, url, remark, pard_id)
    except RequestException as e:
        logging.error(msg="该接口URL {} , 备注 {} 异常: {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark, e))
        return {'content': '请求执行错误', 'url': url, 'remark': remark}


def get_requests(url, data=None, headers={}, remark=None, ip_port=None):
    """
    get请求
    :param url: str, 接口地址
    :param remark: str, 备注
    :param headers: dict, requests header
    :return: object, 响应对象
    """
    headers = {**header, **headers, **{'Content-Type': 'charset=UTF-8'}}
    global count
    try:

        if ip_port is None:
            response = session.get(url=url, params=data, headers=headers, verify=False, timeout=60)
        else:
            ip_port_url = domain_convert_ip_port(url=url, ip_port=ip_port)
            response = session.get(url=ip_port_url, params=data, headers=headers, verify=False, timeout=60)

        status_code = response.status_code
        pard_id = response.headers.get('Pard-Id', 0)
        if 200 <= status_code <= 302:
            if is_json_response(response):
                response_json = convert_response(response)
                if response_json.get('state', 0) == 1 or response_json.get('success', False) or (not response_json.get(
                        'code', 1)):
                    logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                    return response_json
                else:
                    if count < 1:
                        count = count + 1
                        logging.error(
                            msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response_json))
                        return convert_response(response)
                    else:
                        logging.error(
                            msg='该接口URL {} , 备注 {}, 响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                        return convert_response(response)
            else:
                return convert_response(response)
        else:
            if count < 1:
                count += 1
                logging.error(
                    msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response.text))
                return get_requests(url, data=data, headers=headers, remark=remark)
            else:
                return judging_other_abnormal_conditions(status_code, url, remark, pard_id)
    except RequestException:
        logging.error(msg="该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark))
        return {'content': '请求执行错误', 'url': url, 'remark': remark}


def convert_response(response):
    headers = response.headers.get('Content-Type') or response.headers.get('content-type')
    if 'application/json' in headers:
        return response.json()
    elif 'text/html' in headers:
        return response.text
    elif 'application/octet-stream' in headers:
        return response
    try:
        return response.json()
    except AttributeError:
        return response.text


def is_json_response(response):
    if 'application/json' in (response.headers.get('Content-Type', '') or response.headers.get('content-type', '')):
        return True
    return False


# get请求---获取header
def get_header(url, headers={}, allow_redirects=True, ip_port=None):
    headers = {**header, **headers}
    try:
        if ip_port is None:
            response = session.get(url=url, headers=headers, verify=False, timeout=60, allow_redirects=allow_redirects)
        else:
            ip_port_url = domain_convert_ip_port(url=url, ip_port=ip_port)
            response = session.get(url=ip_port_url, headers=headers, verify=False, timeout=60,
                                   allow_redirects=allow_redirects)
        if response.status_code == 200:
            return response.request.headers
    except RequestException as e:
        return {"errors": str(e)}


# 企业微信报警
def wxsend(username, content):
    s = {'userids': username, 'msgtype': 'text', 'content': content}
    params = json.dumps(s)
    try:
        content = requests.post('http://api.oss.lagou.com/v2/send/wechat/', data=params, timeout=3)
        if content.status_code != 200:
            raise IOError("exception")
    except  Exception as e:
        raise IOError("exception")


def login(countryCode, username):
    '''
    从www.lagou.com登录，验证码登录
    :param countryCode: str, 地区编号
    :param username: str, 用户名
    '''
    session.cookies.clear()
    login_url = 'https://passport.lagou.com/login/login.json'
    login_data = {'isValidate': 'true', 'username': username, 'phoneVerificationCode': '049281',
                  'countryCode': countryCode, 'challenge': 111}
    referer_login_html = 'https://passport.lagou.com/login/login.html'
    login_header = get_code_token(referer_login_html)
    remark = str(username) + "在登录拉勾"
    r = form_post(url=login_url, data=login_data, headers=login_header, remark=remark)
    if r['message'] == "操作成功":
        logging.info("用户名: " + str(username) + " 登录成功")
    return r


def login_home(username, password):
    '''
    从home.lagou.com登录，密码登录
    :param username: str, 用户名
    :param password: str, 密码
    :param remark: str, 备注
    '''
    session.cookies.clear()
    referer_login_home_url = "https://home.lagou.com/"
    login_url = 'https://passport.lagou.com/login/login.json'
    login_data = {'isValidate': 'true', 'username': username, 'password': password}
    login_home_header = get_code_token(referer_login_home_url)
    remark = "用户 " + str(username) + " 在登录拉勾home后台"
    r = form_post(url=login_url, data=login_data, headers=login_home_header, remark=remark)
    get_requests(url='https://passport.lagou.com/grantServiceTicket/grant.html')
    if r['message'] == "操作成功":
        logging.info("用户名: " + str(username) + " 登录成功")
    return r


def login_home_code(countryCode, username):
    '''
    从www.lagou.com登录，验证码登录
    :param countryCode: str, 地区编号
    :param username: str, 用户名
    '''
    session.cookies.clear()
    referer_login_home_url = "https://home.lagou.com/"
    login_url = 'https://passport.lagou.com/login/login.json'
    login_data = {'isValidate': 'true', 'username': username, 'phoneVerificationCode': '049281',
                  'countryCode': countryCode, 'challenge': 111}
    login_header = get_code_token(referer_login_home_url)
    remark = str(username) + "在登录拉勾"
    r = form_post(url=login_url, data=login_data, headers=login_header, remark=remark)
    if r['message'] == "操作成功":
        logging.info("用户名: " + str(username) + " 登录成功")
    return r


def assert_equal(expect_value, actual_value, success_message, fail_message=None):
    '''
    断言两个值是否相等, 并对结果打印日志
    :param expect_value: 期望结果
    :param actual_value: 实际结果
    :param success_message: str, 断言成功打印的日志
    :param fail_message:str, 断言失败打印的日志
    '''

    if expect_value == actual_value:
        # loger.success(success_message)
        state = 1
    else:
        loger.error(fail_message)
        state = 0
    assert expect_value == actual_value
    return state


def assert_not_equal(expect_value, actual_value, success_message, fail_message=None):
    '''
    断言两个值是否相等, 并对结果打印日志
    :param expect_value: 期望结果
    :param actual_value: 实际结果
    :param success_message: str, 断言成功打印的日志
    :param fail_message:str, 断言失败打印的日志
    '''

    if expect_value != actual_value:
        # loger.success(success_message)
        pass
    else:
        loger.error(fail_message)
    assert expect_value != actual_value


def assert_in(expect_value, actual_value, success_message, fail_message=None):
    '''
    断言两个值是否相等, 并对结果打印日志
    :param expect_value: 期望结果
    :param actual_value: 实际结果
    :param success_message: str, 断言成功打印的日志
    :param fail_message:str, 断言失败打印的日志
    '''
    if expect_value in actual_value:
        # loger.success(success_message)
        pass
    else:
        loger.error(fail_message)
    assert expect_value in actual_value


def assert_not_in(expect_value, actual_value, success_message, fail_message=None):
    '''
    断言两个值是否相等, 并对结果打印日志
    :param expect_value: 期望结果
    :param actual_value: 实际结果
    :param success_message: str, 断言成功打印的日志
    :param fail_message:str, 断言失败打印的日志
    '''
    if expect_value not in actual_value:
        # loger.success(success_message)
        pass
    else:
        loger.error(fail_message)
    assert expect_value not in actual_value


# 获取url的html源码
def gethtml(url):
    '''

    :param url:
    :return:
    '''
    html = session.get(url)
    return html.text


def wait(time):
    '''
    设置等待时间
    :param time:
    :return:
    '''


def get_app_header(userId, reqVersion=80201):
    header = {"Accept": "application/json", "X-L-REQ-HEADER": {"deviceType": 10, "reqVersion": reqVersion},
              "X-L-USER-ID": str(userId),
              "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
    header["X-L-REQ-HEADER"] = json.dumps(header["X-L-REQ-HEADER"])
    return header


def get_app_header1(userId):
    header = {"Content-Type": "application/json", "X-L-REQ-HEADER": {"deviceType": 10},
              "X-L-USER-ID": str(userId),
              "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
    header["X-L-REQ-HEADER"] = json.dumps(header["X-L-REQ-HEADER"])
    return header


def get_app_header_new(userId, X_L_REQ_HEADER={}):
    app_header = {"deviceType": 10}
    X_L_REQ_HEADER = {**app_header, **X_L_REQ_HEADER}
    header = {"Accept": "application/json", "X-L-REQ-HEADER": X_L_REQ_HEADER,
              "X-L-USER-ID": str(userId),
              "User-Agent": "%E6%8B%89%E5%8B%BE%E6%8B%9B%E8%81%98/7945 CFNetwork/978.0.7 Darwin/18.5.0",
              "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
    header["X-L-REQ-HEADER"] = json.dumps(header["X-L-REQ-HEADER"])
    return header


def json_put(url, remark, data=None, headers={}, ip_port=None):
    """
    json传参的put请求
    :param url: 请求url
    :param remark: str, 备注
    :param data: dict, 请求数据
    :param headers: dict, 请求header
    :return: json格式化的响应结果
    """
    global count
    try:
        headers = {**headers, **header, **{'Content-Type': 'application/json;charset=UTF-8'}}
        if ip_port is None:
            response = session.put(url=url, json=data, headers=headers, verify=False, timeout=60)
        else:
            ip_port_url = domain_convert_ip_port(url=url, ip_port=ip_port)
            response = session.put(url=ip_port_url, json=data, headers=headers, verify=False, timeout=60)

        pard_id = response.headers.get('Pard-Id', 0)
        status_code = response.status_code
        if 200 <= status_code <= 400:
            if is_json_response(response):
                response_json = convert_response(response)
                if response_json.get('state', 0) == 1 or response_json.get('success', False):
                    logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                    return response_json
                else:
                    if count < 1:
                        count = count + 1
                        logging.error(
                            msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response_json))
                        return json_put(url=url, headers=headers, remark=remark, data=data)
                    else:
                        logging.error(
                            msg='该接口URL {} , 备注 {}, 响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                        return response_json
            else:
                return convert_response(response)
        else:
            if count < 1:
                count = count + 1
                logging.error(msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response))
                return json_put(url=url, headers=headers, remark=remark, data=data)
            else:
                return judging_other_abnormal_conditions(status_code, url, remark, pard_id)
    except RequestException as e:
        logging.error(msg="该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n该异常为{}".format(url, remark, e))
        return {'content': '请求执行错误', 'url': url, 'remark': remark}


def put_requests(url, headers={}, remark=None, ip_port=None):
    """
    put请求
    :param url: str, 接口地址
    :param remark: str, 备注
    :param headers: dict, requests header
    :return: object, 响应对象
    """
    global count
    try:
        if ip_port is None:
            response = session.put(url=url, headers=headers, verify=False, timeout=60)
        else:
            ip_port_url = domain_convert_ip_port(url=url, ip_port=ip_port)
            response = session.put(url=ip_port_url, headers=headers, verify=False, timeout=60)
        pard_id = response.headers.get('Pard-Id', 0)
        status_code = response.status_code
        if 200 <= status_code <= 400:
            if is_json_response(response):
                response_json = convert_response(response)
                if response_json.get('state', 0) == 1 or response_json.get('success', False):
                    logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                    return response_json
                else:
                    if count < 1:
                        count = count + 1
                        logging.error(
                            msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response_json))
                        return put_requests(url=url, headers=headers, remark=remark)
                    else:
                        logging.error(
                            msg='该接口URL {} , 备注 {}, 响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                        return response_json
            else:
                return convert_response(response)
        else:
            if count < 1:
                count = count + 1
                logging.error(msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response))
                return put_requests(url=url, headers=headers, remark=remark)
            else:
                return judging_other_abnormal_conditions(status_code, url, remark, pard_id)
    except RequestException:
        logging.error(msg="该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark))
        return {'content': '请求执行错误', 'url': url, 'remark': remark}


def delete_requests(url, headers={}, remark=None, ip_port=None):
    """
    put请求
    :param url: str, 接口地址
    :param remark: str, 备注
    :param headers: dict, requests header
    :return: object, 响应对象
    """
    global count
    try:
        if ip_port is None:
            response = session.delete(url=url, headers=headers, verify=False, timeout=60)
        else:
            ip_port_url = domain_convert_ip_port(url=url, ip_port=ip_port)
            response = session.delete(url=ip_port_url, headers=headers, verify=False, timeout=60)
        pard_id = response.headers.get('Pard-Id', 0)
        status_code = response.status_code
        if 200 <= status_code <= 302:
            if is_json_response(response):
                response_json = convert_response(response)
                if response_json.get('state', 0) == 1 or response_json.get('success', False):
                    logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                    return response_json
                else:
                    if count < 1:
                        count = count + 1
                        logging.error(
                            msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response_json))
                        return delete_requests(url=url, headers=headers, remark=remark)
                    else:
                        logging.error(
                            msg='该接口URL {} , 备注 {}, 响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                        return response_json
            else:
                return convert_response(response)
        else:
            if count < 1:
                count = count + 1
                logging.error(msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response))
                return delete_requests(url=url, headers=headers, remark=remark)
            else:
                return judging_other_abnormal_conditions(status_code, url, remark, pard_id)
    except RequestException:
        logging.error(msg="该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark))
        return {'content': '请求执行错误', 'url': url, 'remark': remark}


def dfs_get_zip_file(input_path, result):
    #
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            dfs_get_zip_file(input_path + '/' + file, result)
        else:
            result.append(input_path + '/' + file)


def zip_path(input_path, output_path, output_name):
    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    filelists = []
    dfs_get_zip_file(input_path, filelists)
    for file in filelists:
        f.write(file)
    f.close()
    file_Path = os.path.abspath(os.path.join(os.getcwd(), ".."))
    zip_file_Path = os.path.join(file_Path, output_name)
    return zip_file_Path


def judging_other_abnormal_conditions(status_code, url, remark, pard_id=None):
    if bool(pard_id):
        call_chain = ' 其调用链:http://oss.pard.inter.lagou.com/#/traDetail?traceId={}'.format(pard_id)
    else:
        call_chain = ''

    if status_code == 500:
        developer_name = return_api_developer(url) or ''
        logging.error(msg="该接口URL:{} , 备注:{} 报错500, {}, 负责人:{} \n".format(url, remark, call_chain, developer_name))
        raise Http500Error
        return {'state': 500, 'content': '报错500, 服务端错误', 'url': url, 'remark': remark + call_chain}
    elif status_code == 415:
        logging.error(msg="该接口URL {} 备注 {} 报错415, 请检查接口的请求方法是否正确\n".format(url, remark))
        return {'state': 415, 'content': '报错415, 接口请求方法不可用', 'url': url, 'remark': remark}
    elif status_code == 404:
        logging.error(msg="该接口URL {} , 备注 {} 报错404, 请检查接口地址是否正确及业务服务是否可用,{}\n".format(url, remark, call_chain))
        return {'state': 404, 'content': '报错404, 接口地址不可用', 'url': url, 'remark': remark + call_chain}
    elif status_code == 401:
        logging.error(msg="该接口URL {} , 备注 {} 报错401 请检查接口的用户认证是否有效\n".format(url, remark))
        return {'state': 401, 'content': '报错401, 接口的用户认证失效', 'url': url, 'remark': remark}
    elif status_code == 400:
        logging.error(msg="该接口URL {} , 备注 {} 报错400 请检查接口的传参是否有效\n".format(url, remark))
        return {'state': 400, 'content': '报错400, 接口的传参有误', 'url': url, 'remark': remark}
    elif status_code == 502:
        logging.error(msg="该接口URL {} , 备注 {} 报错502, 请检查业务服务是否可用,{}\n".format(url, remark, call_chain))
        return {'state': 502, 'content': '报错502, 业务服务不可用', 'url': url, 'remark': remark + call_chain}
    else:
        return {'state': 0, 'content': '报错{}, 请检查业务服务是否正常, {}'.format(status_code, call_chain), 'url': url,
                'remark': remark}


f = 0


def get_verify_code_list(countryCode, phone):
    if countryCode == '0086':
        countryCode = ''
    url = 'https://home.lagou.com/msc/message/page'
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    data = {"commId": countryCode + phone, "startTime": str(yesterday) + "T16:00:00.000Z", 'templateId': '749',
            "page": 1, "count": 10}
    r = json_post(url=url, data=data, headers={'X-L-REQ-HEADER': json.dumps({"deviceType": 1})}, remark="获取验证码列表")
    try:
        if r['content']['totalCount'] == 0:
            return 0, None, None
        else:
            return r['content']['totalCount'], r['content']['result'][0]['msgId'], r['content']['result'][0][
                'createTime']
    except IndexError:
        return 0, None, None


def verify_code_message(countryCode, phone, flag_num=0):
    login_home('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
    import time
    for i in range(10):
        time.sleep(12)
        total_count, id, createTime = get_verify_code_list(countryCode, phone)
        if total_count > flag_num:
            verify_code = get_verify_code(id, createTime)
            if verify_code:
                return verify_code


def get_verify_code(id, createTime):
    url = 'https://home.lagou.com/msc/message/view'
    data = {"createTime": createTime, "msgId": id}
    r = json_post(url=url, data=data, headers={'X-L-REQ-HEADER': json.dumps({"deviceType": 1})}, remark="获取验证码")
    try:
        verify_code = re.findall(r'[1-9]\d+', r.get('content').get('content'))[0]
    except IndexError:
        return None
    return verify_code


# @pysnooper.snoop()
def get_verify_code_message_len(countryCode, phone):
    login_home('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
    if countryCode == '0086':
        countryCode = ''
    time.sleep(2)
    url = 'https://home.lagou.com/msc/message/page'
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    data = {"commId": countryCode + phone, "startTime": str(yesterday) + "T16:00:00.000Z",
            "page": 1, "count": 10, 'templateId': '749'}
    r = json_post(url=url, data=data, headers={'X-L-REQ-HEADER': json.dumps({"deviceType": 1})}, remark="获取验证码列表")
    try:
        return r['content']['totalCount']
    except:
        return -1


def app_header_999(userToken=None, DA=True, userId=None, app_type='zhaopin'):
    if app_type == 'zhaopin':
        header = {"deviceType": '150', "userType": '0', "lgId": "898BCC3F-E662-4761-87E8-845788525443_1532945379",
                  "reqVersion": '73100', "appVersion": "7.31.0"}
    elif app_type == 'LGEdu':
        header = {"lgId": "898BCC3F-E662-4761-87E8-845788525443_1582611503", "appType": 1, "reqVersion": 10300,
                  "appVersion": "1.2.4", "deviceType": 170}
    if not userToken is None:
        header['userToken'] = userToken

    header[
        'X-L-PC-HEADER'] = 'iHYcIxmNf1a/H6tR/hao1vahOgvJmZIEwaWWSXc7bO+Nx3TnQlgHcteuBXnK5zrLHHwxbd10XVRCPVoT3M/T6VkqkEftfJqSfcEZhNJLuRQ='

    header = {'X-L-REQ-HEADER': json.dumps(header)}
    header = {**app_header, **header}
    if userId:
        header['X-L-USER-ID'] = str(userId)
    if DA == False:
        return header
    header[
        'X-L-DA-HEADER'] = "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"
    return header


def login_password(username, password):
    '''
    从www.lagou.com登录，验证码登录
    :param countryCode: str, 地区编号
    :param username: str, 用户名
    '''
    session.cookies.clear()
    # login_url = 'https://passport.lagou.com/login/login.json?isValidate=true&username={}&password={}&request_form_verifyCode=&_={}'.format()
    login_url = 'https://passport.lagou.com/login/login.json'
    login_data = {'isValidate': 'true', 'username': username,
                  'password': password}
    referer_login_html = 'https://passport.lagou.com/login/login.html'
    login_header = get_code_token(referer_login_html)
    remark = str(username) + "在登录拉勾"
    r = form_post(url=login_url, data=login_data, headers=login_header, remark=remark)
    if r['message'] == "操作成功":
        logging.info("用户名: " + str(username) + " 登录成功")
    return r


def login_verifyCode(countryCode, phone, verifyCode):
    '''
    从www.lagou.com登录，验证码登录
    :param countryCode: str, 地区编号
    :param username: str, 用户名
    '''
    session.cookies.clear()
    login_url = 'https://passport.lagou.com/login/login.json'
    login_data = {'isValidate': 'true', 'username': phone,
                  'phoneVerificationCode': verifyCode, 'countryCode': countryCode}
    referer_login_html = 'https://passport.lagou.com/login/login.html'
    login_header = get_code_token(referer_login_html)
    remark = str(phone) + "在登录拉勾"
    r = form_post(url=login_url, data=login_data, headers=login_header, remark=remark)
    if r['message'] == "操作成功":
        logging.info("用户名: " + str(phone) + " 登录成功")
    return r


def pc_send_register_verifyCode(countryCode, phone):
    session.cookies.clear()
    url = 'https://passport.lagou.com/register/getPhoneVerificationCode.json'
    header = get_header(url='https://passport.lagou.com/register/register.html')
    send_data = {'countryCode': countryCode, 'phone': phone, 'type': 0, 'request_form_verifyCode': '', '_': str(int(
        time.time())) + '000'}
    return form_post(url=url, headers=header, data=send_data, remark='发送验证码')['state']


def pc_send_login_verifyCode(countryCode, phone):
    url = 'https://passport.lagou.com/login/sendLoginVerifyCode.json'
    header = get_header(url='https://passport.lagou.com/login/login.html')
    send_data = {'countryCode': countryCode, 'phone': phone, 'type': 0, 'request_form_verifyCode': '', '_': str(int(
        time.time())) + '000'}
    return form_post(url=url, headers=header, data=send_data, remark='发送验证码')['state']


def user_register_lagou(countryCode, phone, verify_code):
    session.cookies.clear()
    b_register_url = 'https://passport.lagou.com/register/register.html?from=b'
    register_url = "https://passport.lagou.com/register/register.json"
    register_data = {"isValidate": "true", "phone": phone, "phoneVerificationCode": verify_code, "challenge": 111,
                     "type": 1, "countryCode": countryCode}
    register_header = get_code_token(b_register_url)
    remark = "验证B端注册"
    return form_post(url=register_url, data=register_data, headers=register_header, remark=remark)


def request_retry(count, request_func, judging_func=None, response_text=None):
    if count < 1:
        count += 1
        return request_func
    elif not response_text is None:
        return response_text
    else:
        judging_func


def domain_convert_ip_port(url, ip_port):
    parsed = urlparse(url)
    if 'gate.lagou.com' == parsed.hostname:
        gate_lagou_com_rule = {'entry': 'gate.lagou.com/v1/entry', 'neirong': 'gate.lagou.com/v1/neirong',
                               'zhaopin': 'gate.lagou.com/v1/zhaopin'}
        domain, verison, module = re.findall(r"https://(.+?)/(.+?)/(.+?)/", url)[0]
        return url.replace('https', 'http').replace(gate_lagou_com_rule.get(module), ip_port)
    return url.replace('https', 'http').replace(parsed.hostname, ip_port)


if __name__ == '__main__':
    sys.path.append(os.path.dirname(__file__))
    url = 'https://gate.lagou.com/v1/zhaopin/shop/goodsOrder/check/312312312321'
    url1 = 'https://easy.lagou.com/session/batchCreate/2132134.json'
    url2 = 'https://gate.lagou.com/v1/zhaopin/talent/app/search'
    url3 = 'https://home.lagou.com/audit/companyApprove/addRiskLabelsByCompany.json'
    url4 = 'https://gate.lagou.com/v1/entry/positionindex/new'
    url5 = 'https://gate.lagou.com/v1/entry/deliver/create'

    # for u in [url, url1, url2, url3, url4, url5]:
    #     r = return_api_developer(url=u)
    #     print(r)
    # curPath = os.path.abspath(os.path.dirname(__file__))
    # rootPath = os.path.split(curPath)[0]
    # print(os.path.dirname(__file__))
    r = judging_other_abnormal_conditions(500, url5, '测试')
    print(r)
