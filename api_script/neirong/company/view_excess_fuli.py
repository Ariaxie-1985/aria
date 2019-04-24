#@author:betty
#@time:2019-4-23

from utils.util import get_requests,get_app_header


def view_excess_fuli():
    url = "https://gate.lagou.com/v1/neirong/company/benefit/category/left"
    header = get_app_header(userId=100014641)
    return get_requests(url=url,headers=header,remark="查看公司剩余福利")

# r = get_requests()
# fuli = r.content['lables'][0]['lable']


