# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_app_header, get_requests, json_post
import json

def searchPositions():
    header={"Accept": "application/json", "X-L-REQ-HEADER": {'deviceType':10,'appVersion':'70800','reqVersion':'71300'}, "X-L-USER-ID": '100014641',
            "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
    header["X-L-REQ-HEADER"] = json.dumps(header["X-L-REQ-HEADER"])
    url='https://gate.lagou.com/v1/entry/positionsearch/searchPosition'
    data={"keyword":"Java","hiTag":"","shieldDeliveyCompany":False,"refreshHiTagList":True,"showId":"269D6E0E-0F60-41DD-9518-6BAF4AF862D3_577696731.055195","lastShowCompanyId":0,"keywordSource":2,"isAd":"1","tagType":"","salaryLower":0,"city":"北京","salaryUpper":0,"longitudeAndLatitude":"-1.000000,-1.000000","pageNo":1,"sort":"0","pageSize":15}
    return json_post(url=url,data=data,headers=header,remark='搜索职位')
# searchPositions()