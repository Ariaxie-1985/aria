# coding:utf-8
# @Time  : 2020/6/3 19:26
# @Author: Sunnyzhang
# Description:
from api_script.entry.account.passport import password_login
from utils.util import  get_requests,app_header_999



def getToken(userToken):
    url = 'https://gate.lagou.com/v1/entry/account/h5/getToken'
    # header = get_header(url="https://kaiwu.lagou.com/distribution/appCenter.html")
    header = app_header_999(userToken=userToken,DA=False,appType=1)
    header["appVersion"]="1.2.7.680"
    header["reqVersion"] = "10207"
    header["lgId"] = "862502040661300_1591588692323"
    remark = "获取gate_login_token"
    return get_requests(url=url, headers=header, remark=remark)




