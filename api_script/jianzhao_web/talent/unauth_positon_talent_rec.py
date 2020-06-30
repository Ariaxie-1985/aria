# coding:utf-8
# @Author: Xiawang
from utils.util import get_code_token, get_requests, login, login_password


def talent_rec_unAuth(positionId):
    # 未认证发布职位的推荐人才
    refer_query_talent_url = f"https://easy.lagou.com/position/multiChannel/createPosition.htm"
    query_talent_url = f"https://easy.lagou.com/talent/position/rec.json?positionId={positionId}"
    query_talent_header = get_code_token(refer_query_talent_url)
    remark = f"为职位{positionId}推荐人才"
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark, rd='Mandy')

# login_password('00912881044064','c47eeb69fa4e64971fb29cb1e9163a19')
# print(talent_rec_unAuth(8145338))