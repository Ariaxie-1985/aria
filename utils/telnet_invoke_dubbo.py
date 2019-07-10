# coding:utf-8
# @Time  : 2019-07-10 17:24
# @Author: Xiawang

import json
import telnetlib
import socket

'''
此代码抄的: https://china-testing.github.io/python3_lib_dubbo.html
'''


class Dubbo(telnetlib.Telnet):
    prompt = 'dubbo>'
    coding = 'gbk'

    # coding = 'utf-8'

    def __init__(self, host=None, port=0,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        super().__init__(host, port)
        self.write(b'\n')

    def command(self, flag, str_=""):
        data = self.read_until(flag.encode())
        self.write(str_.encode() + b"\n")
        return data

    def invoke(self, service_name, method_name, arg):
        command_str = "invoke {0}.{1}({2})".format(
            service_name, method_name, json.dumps(arg))
        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, "")
        data = json.loads(data.decode(Dubbo.coding,
                                      errors='ignore').split('\n')[0].strip())
        return data


if __name__ == '__main__':
    conn = Dubbo('10.1.201.182', 30060)

    data = 143033

    result = conn.invoke(
        "com.lagou.service.business.base.company.api.CompanysQueryService",
        "queryCompanyById",
        data
    )
    print(result)
