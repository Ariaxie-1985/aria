# coding:utf-8
# @Time  : 2019-07-10 17:30
# @Author: Xiawang
from utils.telnet_invoke_dubbo import Dubbo
import time

conn = Dubbo('10.1.201.182', 30060)
service_name = 'com.lagou.service.business.base.company.api.CompanysQueryService'
method_name = 'queryCompanyById'

# CompanysQueryService.queryCompanyById

def case(service_name, method_name, data):
    result = conn.invoke(
        service_name,
        method_name,
        data
    )
    print(result)


if __name__ == '__main__':
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(start_time)
    args = [146827, 142136, 143228, 143015, 143033, 143041, 143070, 143071, 143075, 142373, 142375, 142379, 142380, 142381,
            142382, 142383, 142384, 142385]
    argslist = [142136]
    for index in range(len(args)):
        case(service_name, method_name, args[index])
