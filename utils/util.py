# coding:utf-8
import os
import zipfile
from json import JSONDecodeError

import requests
import re
from requests import RequestException
import json
import logging

logging.getLogger().setLevel(logging.ERROR)

requests.packages.urllib3.disable_warnings()
session = requests.session()

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

count = 0


# 获取页面的token和code
def get_code_token(url):
    global count
    try:
        token_values, code_values = 0, None
        code = session.get(url=url, headers=header, verify=False, timeout=60)
        token_values = re.findall("X_Anti_Forge_Token = '(.*?)'", code.text, re.S)[0]
        code_values = re.findall("X_Anti_Forge_Code = '(.*?)'", code.text, re.S)[0]
        headers = {"X-Anit-Forge-Code": code_values, "X-Anit-Forge-Token": token_values,
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


def form_post(url, remark, data=None, files=None, headers={}):
    """
    form表单传参的post请求
    :param url: 请求url
    :param remark: str, 备注
    :param data: dict, 请求数据
    :param headers: dict, 请求header
    :return: json格式化的响应结果
    """
    global count
    try:
        headers = {**headers, **header}
        response = session.post(url=url, data=data, files=files, headers=headers, verify=False, timeout=60)
        response_json = response.json()
        status_code = response.status_code
        if 200 <= status_code <= 400:
            if response_json.get('state', 0) == 1 or response_json.get('success', False):
                logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                return response_json
            else:
                if count < 1:
                    count = count + 1
                    logging.error(msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response_json))
                    return form_post(url=url, headers=headers, remark=remark, data=data)
                else:
                    logging.error(msg='该接口URL {} , 备注: {},  响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                    return response_json
        else:
            return judging_other_abnormal_conditions(status_code, url, remark)
    except RequestException:
        logging.error(msg="该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark))
        return {'content': '请求异常(requests捕获的异常)', 'url': url, 'remark': remark}
    except JSONDecodeError:
        logging.error(msg="该接口URL {} ,备注 {} 报错json解码错误, 请检查接口的响应是否正确的返回并解析\n".format(url, remark))
        return {'content': '响应内容不是期望的json格式', 'url': url, 'remark': remark}


def json_post(url, remark, data=None, headers={}):
    """
    json传参的post请求
    :param url: 请求url
    :param remark: str, 备注
    :param data: dict, 请求数据
    :param headers: dict, 请求header
    :return: json格式化的响应结果
    """
    global count
    try:
        headers = {**headers, **header}
        response = session.post(url=url, json=data, headers=headers, verify=False, timeout=60)
        response_json = response.json()
        status_code = response.status_code
        if 200 <= status_code <= 400:
            if response_json.get('state', 0) == 1 or response_json.get('success', False):
                logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                return response_json
            else:
                if count < 1:
                    count = count + 1
                    logging.error(msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response_json))
                    return json_post(url=url, headers=headers, remark=remark, data=data)
                else:
                    logging.error(msg='该接口URL {} , 备注 {}, 响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                    return response_json
        else:
            return judging_other_abnormal_conditions(status_code, url, remark)
    except RequestException:
        logging.error(msg="该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark))
        return {'content': '请求执行错误', 'url': url, 'remark': remark}
    except JSONDecodeError:
        logging.error(msg="该接口URL {} ,备注 {} 报错json解码错误, 请检查接口的响应是否正确的返回并解析\n".format(url, remark))
        return {'content': '响应内容不是期望的json格式', 'url': url, 'remark': remark}


def get_requests(url, data=None, headers={}, remark=None):
    """
    get请求
    :param url: str, 接口地址
    :param remark: str, 备注
    :param headers: dict, requests header
    :return: object, 响应对象
    """
    global count
    try:
        response = session.get(url=url, params=data, headers=headers, verify=False, timeout=60)
        status_code = response.status_code
        if 200 <= status_code <= 400:
            if "application/json" in response.headers['content-type']:
                response_json = response.json()
                if 200 <= status_code <= 400:
                    if response_json.get('state', 0) == 1 or response_json.get('success', False):
                        logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                        return response
                    else:
                        if count < 1:
                            count += 1
                            logging.error(
                                msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response_json))
                            return get_requests(url, data=data, headers=headers, remark=remark)
                        else:
                            logging.error(
                                msg='该接口URL {} , 备注 {}, 响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                            return response
            else:
                return response
        else:
            return judging_other_abnormal_conditions(status_code, url, remark)
    except RequestException:
        logging.error(msg="该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark))
        return {'content': '请求执行错误', 'url': url, 'remark': remark}
    except JSONDecodeError:
        logging.error(msg="该接口URL {} ,备注 {} 报错json解码错误, 请检查接口的响应是否正确的返回并解析\n".format(url, remark))
        return {'content': '响应内容不是期望的json格式', 'url': url, 'remark': remark}


# get请求---获取header
def get_header(url):
    try:
        response = session.get(url=url, headers=header, verify=False, timeout=60)
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
    referer_login_html = 'https://www.lagou.com/frontLogin.do'
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


def assert_equal(expectvalue, actualvalue, success_message, fail_message=None):
    '''
    断言两个值是否相等, 并对结果打印日志
    :param expectvalue: 期望结果
    :param actualvalue: 实际结果
    :param success_message: str, 断言成功打印的日志
    :param fail_message:str, 断言失败打印的日志
    '''
    assert expectvalue == actualvalue
    if expectvalue == actualvalue:
        logging.info(success_message)
        return 1
    else:
        logging.error(fail_message)
        return 0


def assert_not_equal(expectvalue, actualvalue, success_message, fail_message=None):
    '''
    断言两个值是否相等, 并对结果打印日志
    :param expectvalue: 期望结果
    :param actualvalue: 实际结果
    :param success_message: str, 断言成功打印的日志
    :param fail_message:str, 断言失败打印的日志
    '''
    assert expectvalue != actualvalue
    if expectvalue != actualvalue:
        logging.info(success_message)
    else:
        logging.error(fail_message)


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


def json_put(url, remark, data=None, headers={}):
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
        headers = {**headers, **header}
        response = session.put(url=url, json=data, headers=headers, verify=False, timeout=3)
        response_json = response.json()
        status_code = response.status_code
        if 200 <= status_code <= 400:
            if response_json.get('state', 0) == 1 or response_json.get('success', False):
                logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                return response_json
            else:
                if count < 1:
                    count = count + 1
                    logging.error(msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response_json))
                    return json_put(url=url, headers=headers, remark=remark, data=data)
                else:
                    logging.error(msg='该接口URL {} , 备注 {}, 响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                    return response_json
        else:
            return judging_other_abnormal_conditions(status_code, url, remark)
    except RequestException:
        logging.error(msg="该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark))
        return {'content': '请求执行错误', 'url': url, 'remark': remark}
    except JSONDecodeError:
        logging.error(msg="该接口URL {} ,备注 {} 报错json解码错误, 请检查接口的响应是否正确的返回并解析\n".format(url, remark))
        return {'content': '响应内容不是期望的json格式', 'url': url, 'remark': remark}


def put_requests(url, headers={}, remark=None):
    """
    put请求
    :param url: str, 接口地址
    :param remark: str, 备注
    :param headers: dict, requests header
    :return: object, 响应对象
    """
    global count
    try:
        response = session.put(url=url, headers=headers, verify=False, timeout=3).json()
        response_json = response.json()
        status_code = response.status_code
        if 200 <= status_code <= 400:
            if response_json.get('state', 0) == 1 or response_json.get('success', False):
                logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                return response_json
            else:
                if count < 1:
                    count = count + 1
                    logging.error(msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response_json))
                    return put_requests(url=url, headers=headers, remark=remark)
                else:
                    logging.error(msg='该接口URL {} , 备注 {}, 响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                    return response_json
        else:
            return judging_other_abnormal_conditions(status_code, url, remark)
    except RequestException:
        logging.error(msg="该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark))
        return {'content': '请求执行错误', 'url': url, 'remark': remark}
    except JSONDecodeError:
        logging.error(msg="该接口URL {} ,备注 {} 报错json解码错误, 请检查接口的响应是否正确的返回并解析\n".format(url, remark))
        return {'content': '响应内容不是期望的json格式', 'url': url, 'remark': remark}


def delete_requests(url, headers={}, remark=None):
    """
    put请求
    :param url: str, 接口地址
    :param remark: str, 备注
    :param headers: dict, requests header
    :return: object, 响应对象
    """
    global count
    try:
        response = session.delete(url=url, headers=headers, verify=False, timeout=3)
        response_json = response.json()
        status_code = response.status_code
        if 200 <= status_code <= 400:
            if response_json.get('state', 0) == 1 or response_json.get('success', False):
                logging.info(msg='该接口URL {} ,备注 {} 执行成功\n'.format(url, remark))
                return response_json
            else:
                if count < 1:
                    count = count + 1
                    logging.error(msg='该接口URL {} , 备注: {} , 响应内容: {} 断言失败, 在重试\n'.format(url, remark, response_json))
                    return delete_requests(url=url, headers=headers, remark=remark)
                else:
                    logging.error(msg='该接口URL {} , 备注 {}, 响应内容: {} 请求成功, 但断言错误\n'.format(url, remark, response_json))
                    return response_json
        else:
            return judging_other_abnormal_conditions(status_code, url, remark)
    except RequestException:
        logging.error(msg="该接口URL {} , 备注 {} 请求异常, 请检查接口服务并重试一次\n".format(url, remark))
        return {'content': '请求执行错误', 'url': url, 'remark': remark}
    except JSONDecodeError:
        logging.error(msg="该接口URL {} ,备注 {} 报错json解码错误, 请检查接口的响应是否正确的返回并解析\n".format(url, remark))
        return {'content': '响应内容不是期望的json格式', 'url': url, 'remark': remark}


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


def judging_other_abnormal_conditions(status_code, url, remark):
    if status_code == 500:
        logging.error(msg="该接口URL {} , 备注 {} 报错500, 请检查业务服务是否可用\n".format(url, remark))
        return {'content': '报错500, 服务端错误', 'url': url, 'remark': remark}
    elif status_code == 415:
        logging.error(msg="该接口URL {} 备注 {} 报错415, 请检查接口的请求方法是否正确\n".format(url, remark))
        return {'content': '报错415, 接口请求方法不可用', 'url': url, 'remark': remark}
    elif status_code == 404:
        logging.error(msg="该接口URL {} , 备注 {} 报错404, 请检查接口地址是否正确及业务服务是否可用\n".format(url, remark))
        return {'content': '报错404, 接口地址不可用', 'url': url, 'remark': remark}
    elif status_code == 502:
        logging.error(msg="该接口URL {} , 备注 {} 报错502, 请检查业务服务是否可用\n".format(url, remark))
        return {'content': '报错502, 业务服务不可用', 'url': url, 'remark': remark}
    else:
        return {'content': '报错{}, 请检查业务服务是否正常'.format(status_code), 'url': url, 'remark': remark}
