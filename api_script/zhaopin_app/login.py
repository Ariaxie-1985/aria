# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import json_post, get_requests
host = "http://10.1.201.237:32040/"

def login():
    url =host+"account/passport/login"
    remark = "登录"
    headers = {
    'content-type': "application/json",
    'x-l-req-header': "{\"appVersion\":\"V_70000_1\",\"deviceType\":200,\"lgId\":\"283d90c4-cd3c-410b-a75f-ce5ec0921bcf\",\"reqVersion\":70000,\"userType\":0}",
    'cache-control': "no-cache",

}
    # headers["X-L-REQ-HEADER"] = json.dumps(headers["X-L-REQ-HEADER"])
    # print(type(headers))
    data={"accountName":"13436460923","loginType":0,"password":"king123"}
    return json_post(url=url, headers=headers, remark=remark, data=data)
# print(login())

def token_login():
    url=host+"account/passport/loginByToken"
    # t=login()["content"]["userToken"]
    remark="获取token"
    headers={
        'content-type': "application/json",
        'x-l-req-header': "{\"appVersion\":\"V_70000_1\",\"deviceType\":200,\"lgId\":\"283d90c4-cd3c-410b-a75f-ce5ec0921bcf\",\"reqVersion\":70000,\"userType\":0,\"userToken\":\"fafbdb43980259cc3e21db026401cbc622e01de3bdde19da178c69e841aa9250\",\"appTime\":1551424200000,\"deviceToken\":\"SB_0000001\"}",
        'cache-control': "no-cache",
    }
    return get_requests(url=url,headers=headers,remark=remark)
# token_login()

def logout():
    url=host+"account/passport/logout"
    remark="退出"
    headers={
        'content-type': "application/json",
        'x-l-req-header': "{\"appVersion\":\"V_70000_1\",\"deviceType\":200,\"lgId\":\"283d90c4-cd3c-410b-a75f-ce5ec0921bcf\",\"reqVersion\":70000,\"userType\":0,\"userToken\":\"1cce55d79b7c34acca97bd995fa1fd3d53011487415647a7bba6263e4b40a261\",\"appTime\":1551424200000,\"deviceToken\":\"SB_0000001\"}",
        'cache-control': "no-cache",
    }
    return get_requests(url=url,headers=headers,remark=remark)
# logout()

def setting():
    url=host+"account/oauth/settings"
    headers={
        'content-type': "application/json",
        'x-l-req-header': "{\"appVersion\":\"V_70000_1\",\"deviceType\":200,\"lgId\":\"283d90c4-cd3c-410b-a75f-ce5ec0921bcf\",\"reqVersion\":70000,\"userType\":0,\"userToken\":\"1cce55d79b7c34acca97bd995fa1fd3d53011487415647a7bba6263e4b40a261\",\"appTime\":1551424200000,\"deviceToken\":\"SB_0000001\"}",
        'cache-control': "no-cache",
        'X-L-USER-ID':"100014023"
    }
    return get_requests(url=url,headers=headers)
setting()

def B_basestatus():
    url =host+"buser/baseStatus/get"
    headers={
        'content-type': "application/json",
        'x-l-req-header': "{\"appVersion\":\"V_70000_1\",\"deviceType\":200,\"lgId\":\"283d90c4-cd3c-410b-a75f-ce5ec0921bcf\",\"reqVersion\":70000,\"userType\":0,\"userToken\":\"1cce55d79b7c34acca97bd995fa1fd3d53011487415647a7bba6263e4b40a261\",\"appTime\":1551424200000,\"deviceToken\":\"SB_0000001\"}",
        'cache-control': "no-cache",
        'X-L-USER-ID':"100014023"
    }
    remark='B端基本信息'
    return get_requests(url,headers,remark)
B_basestatus()

def C_basestatus():
    url =host+"cuser/baseStatus/get"
    headers={
        'content-type': "application/json",
        'x-l-req-header': "{\"appVersion\":\"V_70000_1\",\"deviceType\":200,\"lgId\":\"283d90c4-cd3c-410b-a75f-ce5ec0921bcf\",\"reqVersion\":70000,\"userType\":0,\"userToken\":\"1cce55d79b7c34acca97bd995fa1fd3d53011487415647a7bba6263e4b40a261\",\"appTime\":1551424200000,\"deviceToken\":\"SB_0000001\"}",
        'cache-control': "no-cache",
        'X-L-USER-ID':"100014023"
    }
    remark='C端基本信息'
    return get_requests(url,headers,remark)
C_basestatus()

def buser():
    url=host+"buser/get"
    headers={
        'content-type': "application/json",
        'x-l-req-header': "{\"appVersion\":\"V_70000_1\",\"deviceType\":200,\"lgId\":\"283d90c4-cd3c-410b-a75f-ce5ec0921bcf\",\"reqVersion\":70000,\"userType\":0,\"userToken\":\"1cce55d79b7c34acca97bd995fa1fd3d53011487415647a7bba6263e4b40a261\",\"appTime\":1551424200000,\"deviceToken\":\"SB_0000001\"}",
        'cache-control': "no-cache",
        'X-L-USER-ID':"100014023"
    }
    remark='个人信息'
    return get_requests(url,headers,remark)
buser()

def appsetting():
    url=host+"config/appSetting/get"
    headers={
        'content-type': "application/json",
        'x-l-req-header': "{\"appVersion\":\"V_70000_1\",\"deviceType\":200,\"lgId\":\"283d90c4-cd3c-410b-a75f-ce5ec0921bcf\",\"reqVersion\":70000,\"userType\":0,\"userToken\":\"1cce55d79b7c34acca97bd995fa1fd3d53011487415647a7bba6263e4b40a261\",\"appTime\":1551424200000,\"deviceToken\":\"SB_0000001\"}",
        'cache-control': "no-cache",
    }
    remark='app初始参数'
    return get_requests(url,headers,remark)
# appsetting()