#@author:betty
#@time:2019-4-23

from utils.util import json_post,get_app_header
from api_script.neirong.company.view_fuli import *

def create_fuli():
    # r = get_requests()
    url = "https://gate.lagou.com/v1/neirong/company/benefit/create"
    header = get_app_header(100014641)
    data = {
        "ids": ['23']
    }
    return json_post(url=url, headers=header, data=data, remark="增加公司福利")

s = create_fuli()
print(s)

# r = view_fuli()
# print(r)

