from utils.util import get_requests,app_header_999,get_edu_app_header
def get_user_base_info(userToken):
    url = 'https://gate.lagou.com/v1/neirong/app/getUserBaseInfo'
    header=get_edu_app_header(userToken=userToken,DA=False)
    remarke="获取基本信息成功"
    return get_requests(url=url,headers=header,remark=remarke,rd="旭峰")
