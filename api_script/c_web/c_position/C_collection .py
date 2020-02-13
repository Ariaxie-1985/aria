# coding:utf-8

from utils.util import get_code_token, form_post, get_header, login

login('0086', '1821111111')

positionId = 90135
# 1收藏，0取消收藏
type = 1
url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
collectPositoin_html = 'https://www.lagou.com/jobs/' + str(positionId) + '.html'
get_header(url)
collectPosition_url = 'https://www.lagou.com/mycenter/collectPositoin.json'
collectPositoin_header = get_code_token(collectPositoin_html)
collectPositoin_data = {'positionId': positionId, 'type': type}
form_post(url=collectPosition_url, headers=collectPositoin_header, data=collectPositoin_data, remark='收藏')
