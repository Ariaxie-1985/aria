# coding:utf-8
from util import get, get_code_token, login

# 登录
username = 20181205
login("00852",username)

# 推荐人才
refer_querytalent_url = "https://easy.lagou.com/search/index.htm"
querytalent_url = "https://easy.lagou.com/talent/rec/1.json?positionId=5375318&notSeen=false&strongly=false"
querytalent_header = get_code_token(refer_querytalent_url)
get(querytalent_url,querytalent_header)

# 最新人才
querytalent_url = "https://easy.lagou.com/talent/newest/1.json?positionId=5375290"
get(querytalent_url,querytalent_header)