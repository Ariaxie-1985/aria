# coding:utf-8
# @Time  : 2019-07-30 21:36
# @Author: Xiawang
import json

from flask import make_response


class ResponseCode:
    SUCCESS = (1, '成功')
    FAIL_CREATE_USER = (1000, '创建用户失败, 请重试')
    FAIL_REGISTER_EMAIL = (1001, '该邮箱已注册, 请登录')
    FAIL_STANDARD_EMAIL = (1002, '邮箱不符合规范')
    FAIL_RE_PASSWORD = (1003, '确认密码不一致')
    FAIL_LOGIN_USERNAME = (1004, '用户名不存在, 请重新输入')
    FAIL_LOGIN_PASSWORD = (1005, '密码输入错误, 请重新输入')
    SUCCESS_LOGIN = (1, '登录成功')
    FAIL_LOGIN_AUTH = (1011, '认证失效')
    FAIL_LOGIN = (1006, '登录失败, 请重新登录')
    SUCCESS_LOGOUT = (1, '退出登录成功')
    SUCCESS_CREATE_TESTSHEET = (1, '创建业务提测成功')
    FAIL_CREATE_TESTSHEET = (1007, '创建业务提测')
    FAIL_FIND_USER = (1006, '查找不到该用户, 请重输入用户名')
    SUCCESS_GET_TESTSHEET = (1, '查询成功')
    SUCCESS_UPDATE_TESTSHEET = (1, '更新业务提测成功')
    FAIL_UPDATE_TESTSHEET = (1009, '未更新业务提测')
    FAIL_FIND_TESTSHEET = (1010, '未查到该业务提测')

    def get_message(self, responseCode):
        message = responseCode[1]
        return message

    def get_state(self, responseCode):
        state = responseCode[0]
        return state


class Result():

    def __init__(self, state, message, data=None):
        self.state = state
        self.message = message
        self.data = data

    def get(self):
        return {'state': self.state, 'message': self.message, 'data': self.data}

    def set(self, reponse, data=None):
        reponse['data'] = data
        return reponse


class Results:
    def get(self, response_code, data=None, page_result=None):
        if page_result == None:
            return {'state': response_code[0], 'message': response_code[1], 'data': data}
        else:
            page_result['data'] = data
            return {'state': response_code[0], 'message': response_code[1], 'data': page_result}

    def set_data(self, data=None):
        init_data = []
        if not data is None:
            init_data.append(data)
        return init_data

    def set_response(self, data, token):
        return make_response(json.dumps(data), 200, {'Access-Control-Expose-Headers': 'TOKEN','Content-Type': 'application/json', 'TOKEN': token})


class DBData():
    def parse_data(self, data, **kwargs):
        key_set = data.keys() & kwargs.keys()
        for key in key_set:
            if key in kwargs:
                data.pop(key)
        return data


if __name__ == '__main__':
    # state = responseCode()
    print(ResponseCode.SUCCESS)
    # print(.SUCCESS[0])
    # print(state.get_state(state.SUCCESS))
