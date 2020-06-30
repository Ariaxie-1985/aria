# coding:utf-8
# @Time  : 2020/6/3 19:26
# @Author: Sunnyzhang
# Description:
from api_script.entry.account.passport import password_login
from utils.util import  get_requests,get_edu_app_header



'''def getToken(userToken):
    print("gettoken中的usertoken"+userToken)
    url = 'https://gate.lagou.com/v1/entry/account/h5/getToken'
    # header = get_header(url="https://kaiwu.lagou.com/distribution/appCenter.html")
    header = get_edu_app_header(userToken=userToken,DA=False)
    header["appVersion"]="1.2.7.680"
    header["reqVersion"] = "10207"
    header["lgId"] = "862502040661300_1591588692323"
    remark = "获取gate_login_token"
    return get_requests(url=url, headers=header, remark=remark)'''


def getToken(userToken):
    print("gettoken中的usertoken"+userToken)
    url = 'https://gate.lagou.com/v1/entry/account/h5/getToken'
    # header = get_header(url="https://kaiwu.lagou.com/distribution/appCenter.html")
    header = get_edu_app_header(userToken=userToken,DA=False)
    header["appVersion"]="1.3.0"
    header["reqVersion"] = "10300"
    header["lgId"] = "269D6E0E-0F60-41DD-9518-6BAF4AF862D3_1593075931"
    remark = "获取gate_login_token"
    return get_requests(url=url, headers=header, remark=remark)

"""def getToken(userToken='ef53bdf784870e928c50e0583fd8b8de63fc2b92e60747ec3aacadbdf1dea2d4'):
    print("gettoken中的usertoken"+userToken)
    url = 'https://gate.lagou.com/v1/entry/account/h5/getToken'
    # header = get_header(url="https://kaiwu.lagou.com/distribution/appCenter.html")
   
    header={'User-Agent': '%E6%8B%89%E5%8B%BE%E6%8B%9B%E8%81%98/7988 CFNetwork/978.0.7 Darwin/18.5.0', 'X-L-REQ-HEADER': '{"lgId":"269D6E0E-0F60-41DD-9518-6BAF4AF862D3_1593075931","appVersion":"1.3.0","deviceType":170,"reqVersion":10300,"userType":0,"appType":1,"userToken":"ef53bdf784870e928c50e0583fd8b8de63fc2b92e60747ec3aacadbdf1dea2d4"}', 'X-L-PC-HEADER': 'iHYcIxmNf1a/H6tR/hao1vahOgvJmZIEwaWWSXc7bO+Nx3TnQlgHcteuBXnK5zrLHHwxbd10XVRCPVoT3M/T6VkqkEftfJqSfcEZhNJLuRQ='}

    #header={"lgId":"269D6E0E-0F60-41DD-9518-6BAF4AF862D3_1593075931","appVersion":"1.3.0","deviceType":170,"reqVersion":10300,"userType":0,"appType":1,"userToken":"ef53bdf784870e928c50e0583fd8b8de63fc2b92e60747ec3aacadbdf1dea2d4"}
    return get_requests(url=url, headers=header)"""
if __name__ == '__main__':
    a=getToken()
    print(a)