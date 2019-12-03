# coding:utf-8
import os
import time
import zipfile
from datetime import datetime
import datetime
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
app_header = {
    'User-Agent': '%E6%8B%89%E5%8B%BE%E6%8B%9B%E8%81%98/7988 CFNetwork/978.0.7 Darwin/18.5.0'
}

count = 0


# 获取页面的token和code
def get_code_token(url, referer=False):
    global count
    try:
        token_values, code_values = 0, None
        code = session.get(url=url, headers=header, verify=False, timeout=60)
        token_values = re.findall("X_Anti_Forge_Token = '(.*?)'", code.text, re.S)[0]
        code_values = re.findall("X_Anti_Forge_Code = '(.*?)'", code.text, re.S)[0]
        if referer == False:
            headers = {"X-Anit-Forge-Code": code_values, "X-Anit-Forge-Token": token_values,
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


def get_code_token_new(url):
    global count
    try:
        token_values, code_values = 0, None
        code = session.get(url=url, headers=header, verify=False, timeout=60)
        token_values = re.findall("X_Anti_Forge_Token = '(.*?)'", code.text, re.S)[0]
        code_values = re.findall("X_Anti_Forge_Code = '(.*?)'", code.text, re.S)[0]
        headers = {"Content-Type": "application/json", "X-Anit-Forge-Code": code_values,
                   "X-Anit-Forge-Token": token_values,
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
        headers = {**header, **headers}
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


def json_post(url, remark, data=None, headers={}, app=False, verifystate=True):
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
        headers = {**header, **headers}
    try:
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
    except RequestException as e:
        print(e)
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
    headers = {**header, **headers}
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


def get_app_header_new(userId, X_L_REQ_HEADER={}):
    app_header = {"deviceType": 10}
    X_L_REQ_HEADER = {**app_header, **X_L_REQ_HEADER}
    header = {"Accept": "application/json", "X-L-REQ-HEADER": X_L_REQ_HEADER,
              "X-L-USER-ID": str(userId),
              "User-Agent": "%E6%8B%89%E5%8B%BE%E6%8B%9B%E8%81%98/7945 CFNetwork/978.0.7 Darwin/18.5.0",
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


f = 0


def verify_code_message(countryCode, phone, flag_num=0):
    if countryCode == '0086':
        countryCode = 0
    url = 'http://msg.lagou.com/msc/message/page'
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    data = {"commId": countryCode + phone, "startTime": str(yesterday) + "T16:00:00.000Z",
            "page": 1, "count": 10}
    header = {"X-L-REQ-HEADER": '{deviceType:1}',
              "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    r = requests.post(url=url, json=data, headers=header, verify=False).json()
    if len(r['content']['result']) > flag_num:
        id, createTime = r['content']['result'][0]['msgId'], r['content']['result'][0]['createTime']
        verify_code = get_verify_code(id, createTime)
    else:
        import time
        for i in range(10):
            time.sleep(12)
            r = requests.post(url=url, json=data, headers=header, verify=False).json()
            if len(r['content']['result']) == 0:
                if i == 9:
                    logging.error(msg="未获取到验证码，手机号为{}".format(countryCode + phone))
                    return None
                continue
            else:
                id, createTime = r['content']['result'][0]['msgId'], r['content']['result'][0]['createTime']
                verify_code = get_verify_code(id, createTime)
                break
    return verify_code


def get_verify_code(id, createTime):
    url = 'http://msg.lagou.com/msc/message/view'
    data = {"createTime": createTime, "msgId": id}
    header = {"X-L-REQ-HEADER": '{deviceType:1}',
              "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    r = requests.post(url=url, json=data, headers=header, verify=False).json()
    verify_code = r['content']['content'][3:9]
    return verify_code


def get_verify_code_message_len(countryCode, phone):
    if countryCode == '0086':
        countryCode = 0
    url = 'http://msg.lagou.com/msc/message/page'
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    data = {"commId": countryCode + phone, "startTime": str(yesterday) + "T16:00:00.000Z",
            "page": 1, "count": 10}
    header = {"X-L-REQ-HEADER": '{deviceType:1}',
              "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    r = requests.post(url=url, json=data, headers=header, verify=False).json()
    if r['content']['totalCount'] >= 2:
        return 1
    else:
        return 0


def app_header_999(userToken=None, DA=True):
    if not userToken is None:
        header = {"deviceType": '150', "userType": '0', "lgId": "898BCC3F-E662-4761-87E8-845788525443_1532945379",
                  "reqVersion": '72200', "appVersion": "7.21.0", "userToken": userToken}
    else:
        header = {"deviceType": '150', "userType": '0', "lgId": "898BCC3F-E662-4761-87E8-845788525443_1532945379",
                  "reqVersion": '72200', "appVersion": "7.21.0"}

    header = {'X-L-REQ-HEADER': json.dumps(header)}
    if DA == False:
        return {**app_header, **header}
    header = {**app_header, **header,
              "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
    return header


# def login1(username,password,):
#     '''
#     从www.lagou.com登录，验证码登录
#     :param countryCode: str, 地区编号
#     :param username: str, 用户名
#     '''
#     session.cookies.clear()
#     header={'Accept':'application/json','Content-Type':'text/plain;charset=UTF-8'}
#     challenge_r=requests.post(verify=False,url='https://api.geetest.com/gt_judgement?pt=0&gt=66442f2f720bfc86799932d8ad2eb6c7',headers=header,data='xF)VH7p1T2jZ2bXtuNPD(((TeJVNrqFXel9WBuiDPaxt(RBE)CgB1ZHBPWQv8pbCGFX9hhob70gKbhr3elumR6d809rKTi8ALjdY5uuqGeWVCCqLfOACHGZLij30xCPX3UJP4dL8KN)vrYynjXVDlPUXC(Bla9LSKOYosrkLyz3spLupaOsI0hEdnG)xrOEus4ubQ2cCRLMxn0uRiGnvhSymN5LNevafm11tesPdEhkkfTC92nNDcLPI1dlVHESW)KFqYwZ8qMpB2)brEYvyD4MfNhqac8kbi0w64OphGNjHl1lUuxd(RcSkk0OPQkj7G6vOK0p0CtN7tt(yBz7g(UFN2Imz5OrfNLXdR6BfHX8Rocrw8oNjnUXX6SOIQPlGgcu1dYCXtNGlQf84lz67o1RhrWnHdAybr7zhYmEKIbg6aSvLW68NZh2(nBRgNfhbalAc3F2ofUnaXYDo(XC1NGFP2lF7j9d1fwUSId7P84ei3(TpZX3pEfY(pP5DfrCAOvUqAy0ay06)aJwZl8i3ldFRLO0ioghQg)(rJ7O5sE4yRJH8Ew(hYHGoccvfY0md1ado8qnG43EL6JgcT4b4TACqJVQNd0mvbgDHgvg8e3ClsSTHkRGHNjVz(MbTbY6HYZNgNXMIH9p9VbsYJVk(GMaA8G4Jm4kc5arjGVW)zeXsLopYlHEiDGTYOVQEI6dGr)OI0i2U0Uh4E0pvUfqXVDBy4V)BqF6Phqa7mPbvEqxOKfQ6TWELH0tZ5H2BcgEAaVDXY9t0S3ZwXRRKrjVDVIXRlhUELE2VMKkn6tuoLYLevVj7k9OoFwjNk2ipht6Llb16s7Xs(e0ttQYYx))H9ipM6koFn6RSLICgU9PrNWqJ4y6(yGZM2a8d9eE8tC)r4XNb)MJU3GTmMzMQ5B(XmzOVEsypnX)1LDi4bL13AP8C)5cxBUzPrUIWQUoGP39a3NjOVVqLNz8fmGHtCB34l3)GTJXxHwnw(laqqv4pz18L8P2(KAcbScOOk(rS7My)hOtkKNEma6pA9hzx7DpPFiQXK6j7U6d5fGMYpSyBWvhRAmUopsdnEd914MkH1UX6pLJQ03JtWKBaQjtb7sojT5o3B5pRR26EMPTDR90h9wRpqZUPSJb2y262HfEuNHJeuiOa)1QONyEGKLKZkpeIzBVl90dgz2rr9mg9PzVu0VwSecwY0JongnqM5t6NbOkzf8XfYeU3FjBqOZ3pQ4vBNpqrzwx6pOagN2bL(YkrZJfO276YavUlKiEaX4eWNKQFoudWWwPb5dXYwpFHAmNj1J4XkJPhmXGZrLwS)G1f2(JjKTMxmTSilq2xBVaHE(77Oe3B3eUc1pS1uc1WBQEFadZxghrOirPCbh9ppCLnZcg2DqSoBvq0fg93EaaGM0oGBtDGuNsSZP3(ds061inhgm8npGvugtbbv4DleNFSIIwHZPwXAeog)duEAjODt((iAVxPlrdyZBt9eYVUdUU6hlidv8v32lPoqaeLPMVsdT(XxMYYTPXjYlcChi25LiQol99p6pFYVavMkkdkcudThGCvEyQBH5yejJsBS3mTKi5KQYZVBZIpd)ACAIi5I3ufSX9G1EIbttWIOCnumpbzFikiFxUUe051nvl7)Xx6k4obyeCF5JFavR1aqarzhNsnJ5JO9SBqLleICsfwvXbKrldUzLINzhedeHN4u83TumVcTSkgHN6CDRGXc6ZvnCWdFabIJg43tMa9gArP9ysBwK73ODBc6FNGidvyzcpvEFaiPDSM7rDT1NlSXOgs2vcpG)4rVsK1sBAPdzWJhr0rzQsAzueiuIKMSCLQJ1dV)KMtxWE(2JN0XmYEOB8E81OdiFyYtIVfgMBkIlSv1YUfziVutnL6pHvvtBj4ZqYF3IL06UaArsuqYNeA1AgTb7M)ZhYFGVSrlvAE72OOhKy8xVCmsBTDByTG96)eCnaR4W5fzJvsnjXunwlwRSrKd8GMlSXX8whAsmVoAszfAMuMOWfPdRKuPNI0JTVnsxJ5wbON29d06OjsVmS2DGQ5erImWw13dz04dNw(8YgXoxrDu1BSN65n69NWD72EMJQNpGR7SYWfOMgH8Vuv6Tm9laih8P8GFP3OWTMkyiuZhw(jG6nqbLO()npRWdRzIG4M574XhAgwYZR76YZLuP(wo5X(ZnOodTzJMipXJypQ2h06xitPfHXtkQ12suCIihuyXFRQuNFtvD8Kgj3qTZXbq9Lg7LAUf26X3clmtoiZZSc6DVvBPcBcQuCrUfaOKtZ3(OEvgyhFxyve4R(P6xdMAeojqJ24FEioqZqnh5gzOMMBvgax3GGwzr7sQ7Jb1BnCNSzzCjbSnDwbEPPT5w1wQnkSuifinv56QvdocvuyuoiqtzplxtJ0hpS(2mEsPXxXsA)DJ5uKoMeiQzY2SciCEQThs6F(XbU(F9jHAQyFrOQJbm(6bRrhmdLnl(lruIPHF9JnO8R2wSMA9QLVqQ7dWQ1UWL4lZL4QGykeGA47ojei0l5JqrQ0TzOYBF58Aet)0xBOCOFVld43dpnwrh(KRiRhBb54Aaf0sFVmVebTbM7VjMKrQWYrAMgKxQFqKJ457kerPWJvTyHBEAlYvXJr9K179w7FJFHSKX0yJdWhJabsLLCZjAAnFtiwqkI2HU1H9OT42zmHbqQ7IyfC84QtOyZKLwDwsl21AiqAjCwVBpv4d8SgeEliSuSNrTtlu(BBndU.95599294653dbf31a80c3b0ec63cbcf039a4408b77a7fab484b560316d4c4c3f350e3d24cabf2e3badf55f162561a9413ccfe49bf17c564385e7a0cedf47d3d9a957dfaab3ee546eec4f887b7a4c128d88866915fc43c1505ab6070b964ef12bc0daaa7ee1387c0052360808cfd915092de7a16329e6f9c832d64478cd164ce8').json()
#     if challenge_r['status']=='success':
#         login_url = 'https://passport.lagou.com/login/login.json'
#         login_data = {'isValidate': 'true', 'username': username,
#                       'password': password, 'challenge': challenge_r['challenge']}
#         referer_login_html = 'https://www.lagou.com/frontLogin.do'
#         login_header = get_code_token(referer_login_html)
#         remark = str(username) + "在登录拉勾"
#         r = form_post(url=login_url, data=login_data, headers=login_header, remark=remark)
#         if r['message'] == "操作成功":
#             logging.info("用户名: " + str(username) + " 登录成功")
#         return r
#     else:
#         logging.info("challenge请求失败")
#         return False
# def challenge():
#     header={'Accept':'application/json','Content-Type':'text/plain;charset=UTF-8'}
#     gt='\&gt=66442f2f720bfc86799932d8ad2eb6c7'
#     r=requests.post(verify=False,url='https://api.geetest.com/gt_judgement?pt=2',headers=header,data='xF)VH7p1T2jZ2bXtuNPD(((TeJVNrqFXel9WBuiDPaxt(RBE)CgB1ZHBPWQv8pbCGFX9hhob70gKbhr3elumR6d809rKTi8ALjdY5uuqGeWVCCqLfOACHGZLij30xCPX3UJP4dL8KN)vrYynjXVDlPUXC(Bla9LSKOYosrkLyz3spLupaOsI0hEdnG)xrOEus4ubQ2cCRLMxn0uRiGnvhSymN5LNevafm11tesPdEhkkfTC92nNDcLPI1dlVHESW)KFqYwZ8qMpB2)brEYvyD4MfNhqac8kbi0w64OphGNjHl1lUuxd(RcSkk0OPQkj7G6vOK0p0CtN7tt(yBz7g(UFN2Imz5OrfNLXdR6BfHX8Rocrw8oNjnUXX6SOIQPlGgcu1dYCXtNGlQf84lz67o1RhrWnHdAybr7zhYmEKIbg6aSvLW68NZh2(nBRgNfhbalAc3F2ofUnaXYDo(XC1NGFP2lF7j9d1fwUSId7P84ei3(TpZX3pEfY(pP5DfrCAOvUqAy0ay06)aJwZl8i3ldFRLO0ioghQg)(rJ7O5sE4yRJH8Ew(hYHGoccvfY0md1ado8qnG43EL6JgcT4b4TACqJVQNd0mvbgDHgvg8e3ClsSTHkRGHNjVz(MbTbY6HYZNgNXMIH9p9VbsYJVk(GMaA8G4Jm4kc5arjGVW)zeXsLopYlHEiDGTYOVQEI6dGr)OI0i2U0Uh4E0pvUfqXVDBy4V)BqF6Phqa7mPbvEqxOKfQ6TWELH0tZ5H2BcgEAaVDXY9t0S3ZwXRRKrjVDVIXRlhUELE2VMKkn6tuoLYLevVj7k9OoFwjNk2ipht6Llb16s7Xs(e0ttQYYx))H9ipM6koFn6RSLICgU9PrNWqJ4y6(yGZM2a8d9eE8tC)r4XNb)MJU3GTmMzMQ5B(XmzOVEsypnX)1LDi4bL13AP8C)5cxBUzPrUIWQUoGP39a3NjOVVqLNz8fmGHtCB34l3)GTJXxHwnw(laqqv4pz18L8P2(KAcbScOOk(rS7My)hOtkKNEma6pA9hzx7DpPFiQXK6j7U6d5fGMYpSyBWvhRAmUopsdnEd914MkH1UX6pLJQ03JtWKBaQjtb7sojT5o3B5pRR26EMPTDR90h9wRpqZUPSJb2y262HfEuNHJeuiOa)1QONyEGKLKZkpeIzBVl90dgz2rr9mg9PzVu0VwSecwY0JongnqM5t6NbOkzf8XfYeU3FjBqOZ3pQ4vBNpqrzwx6pOagN2bL(YkrZJfO276YavUlKiEaX4eWNKQFoudWWwPb5dXYwpFHAmNj1J4XkJPhmXGZrLwS)G1f2(JjKTMxmTSilq2xBVaHE(77Oe3B3eUc1pS1uc1WBQEFadZxghrOirPCbh9ppCLnZcg2DqSoBvq0fg93EaaGM0oGBtDGuNsSZP3(ds061inhgm8npGvugtbbv4DleNFSIIwHZPwXAeog)duEAjODt((iAVxPlrdyZBt9eYVUdUU6hlidv8v32lPoqaeLPMVsdT(XxMYYTPXjYlcChi25LiQol99p6pFYVavMkkdkcudThGCvEyQBH5yejJsBS3mTKi5KQYZVBZIpd)ACAIi5I3ufSX9G1EIbttWIOCnumpbzFikiFxUUe051nvl7)Xx6k4obyeCF5JFavR1aqarzhNsnJ5JO9SBqLleICsfwvXbKrldUzLINzhedeHN4u83TumVcTSkgHN6CDRGXc6ZvnCWdFabIJg43tMa9gArP9ysBwK73ODBc6FNGidvyzcpvEFaiPDSM7rDT1NlSXOgs2vcpG)4rVsK1sBAPdzWJhr0rzQsAzueiuIKMSCLQJ1dV)KMtxWE(2JN0XmYEOB8E81OdiFyYtIVfgMBkIlSv1YUfziVutnL6pHvvtBj4ZqYF3IL06UaArsuqYNeA1AgTb7M)ZhYFGVSrlvAE72OOhKy8xVCmsBTDByTG96)eCnaR4W5fzJvsnjXunwlwRSrKd8GMlSXX8whAsmVoAszfAMuMOWfPdRKuPNI0JTVnsxJ5wbON29d06OjsVmS2DGQ5erImWw13dz04dNw(8YgXoxrDu1BSN65n69NWD72EMJQNpGR7SYWfOMgH8Vuv6Tm9laih8P8GFP3OWTMkyiuZhw(jG6nqbLO()npRWdRzIG4M574XhAgwYZR76YZLuP(wo5X(ZnOodTzJMipXJypQ2h06xitPfHXtkQ12suCIihuyXFRQuNFtvD8Kgj3qTZXbq9Lg7LAUf26X3clmtoiZZSc6DVvBPcBcQuCrUfaOKtZ3(OEvgyhFxyve4R(P6xdMAeojqJ24FEioqZqnh5gzOMMBvgax3GGwzr7sQ7Jb1BnCNSzzCjbSnDwbEPPT5w1wQnkSuifinv56QvdocvuyuoiqtzplxtJ0hpS(2mEsPXxXsA)DJ5uKoMeiQzY2SciCEQThs6F(XbU(F9jHAQyFrOQJbm(6bRrhmdLnl(lruIPHF9JnO8R2wSMA9QLVqQ7dWQ1UWL4lZL4QGykeGA47ojei0l5JqrQ0TzOYBF58Aet)0xBOCOFVld43dpnwrh(KRiRhBb54Aaf0sFVmVebTbM7VjMKrQWYrAMgKxQFqKJ457kerPWJvTyHBEAlYvXJr9K179w7FJFHSKX0yJdWhJabsLLCZjAAnFtiwqkI2HU1H9OT42zmHbqQ7IyfC84QtOyZKLwDwsl21AiqAjCwVBpv4d8SgeEliSuSNrTtlu(BBndU.95599294653dbf31a80c3b0ec63cbcf039a4408b77a7fab484b560316d4c4c3f350e3d24cabf2e3badf55f162561a9413ccfe49bf17c564385e7a0cedf47d3d9a957dfaab3ee546eec4f887b7a4c128d88866915fc43c1505ab6070b964ef12bc0daaa7ee1387c0052360808cfd915092de7a16329e6f9c832d64478cd164ce8').json()
#     # r=requests.post(verify=False,url='https://api.geetest.com/gt_judgement?pt=0&gt=66442f2f720bfc86799932d8ad2eb6c7',headers=header)
#     return r
# # print(login1('yqzhang@lagou.com','cfe4d90b488c85e34838a604822e10ca'))
# # print(challenge())
# def login_app():
#     url ="https://gate.lagou.com/v1/entry/account/passport/login"
#     remark = "登录"
#     headers = {
#         'content-type': "application/json",
#         'x-l-req-header': "{\"appVersion\":\"7.18.0\",\"deviceType\":200,\"reqVersion\":71800,\"userType\":-1}",
#         'X-L-PC-HEADER': 'LYwTbsvR16WEbyc3HzmVu6MVT9G6nb0wxpOKLqy05SQE6gE1Vo4ad8m3yEEr8O4VqQMnJvjYYkiK/LcrQoJcAZP29PqI6bSEFR0FZYhoSes=',
#         'cache-control': "no-cache",
#         # 'x-l-da-header':'da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15'
#     }
#     # headers["X-L-REQ-HEADER"] = json.dumps(headers["X-L-REQ-HEADER"])
#     # print(type(headers))
#     data={"accountName":"940238856@qq.com","loginType":0,"password":"123456"}
#     return json_post(url=url, headers=headers, remark=remark, data=data)
#
# login_app()
# # print(challenge())
# # from api_script.business.B_energycard import getpositionId
# # def getpositionId():
# #     position_url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
# #     position_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
# #     s = form_post(url=position_url,headers=position_header,data={'pageNo':1},remark='获取职位id')
# #     return s['content']['data']['parentPositionVOs'][0]['positions'][0]['positionId']
# # login1('yqzhang@lagou.com')
# # getpositionId()
#
# def searchPositions():
#     header={"Accept": "application/json", "X-L-REQ-HEADER": {"userToken":"9c7228e5ebcbb621d0ace829bd9d6dbda398935887eec834","reqVersion":71800,"lgId":"99000646684560_1560396841537","appVersion":"7.18.0","userType":0,"deviceType":200}}
#     header["X-L-REQ-HEADER"] = json.dumps(header["X-L-REQ-HEADER"])
#     url='https://gate.lagou.com/v1/entry/positionsearch/searchPosition'
#     data={"keyword":"Java","hiTag":"","shieldDeliveyCompany":False,"refreshHiTagList":True,"showId":"269D6E0E-0F60-41DD-9518-6BAF4AF862D3_577696731.055195","lastShowCompanyId":0,"keywordSource":2,"isAd":"1","tagType":"","salaryLower":0,"city":"北京","salaryUpper":0,"longitudeAndLatitude":"-1.000000,-1.000000","pageNo":1,"sort":"0","pageSize":15}
#     return json_post(url=url,data=data,headers=header,remark='搜索职位')
# # def goods_product_version():
# #     url = "https://gate.lagou.com/v1/zhaopin/rights/getRightsList"
# #     remark = "获取当前用户商业产品版本号"
# #     header={"userToken":"42950bed7acc28db48ed54ab14d367caf758f16bd45c3347","reqVersion":71800,"lgId":"99000646684560_1560396841537","appVersion":"7.18.0","userType":0,"deviceType":200}
# #     return json_post(url=url, headers=header, remark=remark)
# # print(searchPositions())
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
    b_register_url = 'https://passport.lagou.com/register/register.html?from=b'
    register_url = "https://passport.lagou.com/register/register.json"
    register_data = {"isValidate": "true", "phone": phone, "phoneVerificationCode": verify_code, "challenge": 111,
                     "type": 1, "countryCode": countryCode}
    register_header = get_code_token(b_register_url)
    remark = "验证B端注册"
    return form_post(url=register_url, data=register_data, headers=register_header, remark=remark)


if __name__ == '__main__':
    # r = get_verify_code_message_len('00852', '20180917')
    # r = verify_code_message('00852', '20180917')
    # r1 = get_verify_code_message_len('00852', '20180917')
    # print(r)
    # print(r1l)
    # login_password('betty@lagou.com', '00f453dfec0f2806db5cfabe3ea94a35')
    state_code = pc_send_register_verifyCode('00852', 20030105)
    # print(verify_code_message('00852', '20030105', flag_num=1))
