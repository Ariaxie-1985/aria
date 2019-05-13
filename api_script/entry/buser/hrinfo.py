# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from utils.util import get_app_header, get_requests, json_post
import json
# header=get_app_header(100014641)
header = {"Accept": "application/json", "X-L-REQ-HEADER": {"deviceType": 10}, "X-L-USER-ID": str(100018375),
          'appVerdion': 70100,
          "X-L-DA-HEADER": "da5439aadaf04ade94a214d730b990d83ec71d3e9f274002951143c843badffbc543b213dfe84e21a37bb782dd9bbca4be8d947ead7041f79d336cb1217127d15"}
header["X-L-REQ-HEADER"] = json.dumps(header["X-L-REQ-HEADER"])


def hrinfo():
    url = 'https://gate.lagou.com/v1/entry/buser/hrInfo/100014641'
    return get_requests(url=url, headers=header, remark='hr信息')


# print(hrinfo())