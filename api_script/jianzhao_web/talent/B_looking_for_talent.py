# coding:utf-8
# @Author: Xiawang
from utils.util import get_requests, get_code_token, login

'''
找人才的推荐人才和最新人才
'''
# 登录
username = 20181205
login("00852",username)

# 推荐人才
refer_querytalent_url = "https://easy.lagou.com/search/index.htm"
querytalent_url = "https://easy.lagou.com/talent/rec/1.json?positionId=5375318&notSeen=false&strongly=false"
querytalent_header = get_code_token(refer_querytalent_url)
get_requests(querytalent_url,querytalent_header)

# 最新人才
querytalent_url = "https://easy.lagou.com/talent/newest/1.json?positionId=5375290"
get_requests(querytalent_url,querytalent_header)