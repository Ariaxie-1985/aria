# coding:utf-8
# @Author: Xiawang
from utils.util import get_code_token, get_header ,form_post ,login

login('00853','05180001')

rf_url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
get_header(rf_url)

positionId = str(5375250)
location = 'first_level'
date = '2018-12-28'
topCardNum = str(1)


topCard_html = 'https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1'
topCard_url = 'https://easy.lagou.com/topCard/add-schedule.json'
header = get_code_token(topCard_html)
data = {'scheduleAddList':'[{"positionId":'+positionId+','+'"location"'+':'+location+','+'"date"'+':'+date+','+'"topCardNum"'+':'+topCardNum+'}]'}
form_post(url=topCard_url,headers=header,data=data)


