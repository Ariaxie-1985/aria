# -*- coding: utf8 -*-
__author__ = 'yqzhang'


from utils.util import get_code_token, form_post, get_header ,login
import math

login('0086','18211111111')
def getpositionidfromcompanyid(companyId):
    page = 1
    positioblist=[]
    url = 'https://www.lagou.com/gongsi/searchPosition.json'
    header = get_code_token('https://www.lagou.com/gongsi.html')
    data = {'companyId':companyId,'positionFirstType':'全部','schoolJob':'false','pageNo':page,'pageSize':10}
    s = form_post(url=url,data=data,headers=header,remark='获取该公司下所有职位')
    position=s['content']['data']['hrInfoMap']
    total=s['content']['data']['page']['totalCount']
    i = math.ceil(int(total)/10)
    while i-1 > 0:
        page = page+1
        data = {'companyId':companyId,'positionFirstType':'全部','schoolJob':'false','pageNo':page,'pageSize':10}
        r = form_post(url=url,data=data,headers=header,remark='获取该公司下所有职位')
        position1=r['content']['data']['hrInfoMap']
        position=dict(position ,**position1)
        i = i-1
    for key in position:
        # print (key)
        positioblist.append(key)
    return(positioblist)


# print(getpositionidfromcompanyid(142128))

def collection(positionlist,type):
    # type=1收藏，type=0取消收藏
    collectPosition_url = 'https://www.lagou.com/mycenter/collectPositoin.json'
    get_header(collectPosition_url)
    for i in positionlist:
        collectPositoin_html = 'https://www.lagou.com/jobs/'+str(i)+'.html'
        collectPositoin_data = {'positionId':i,'type':type}
        collectPositoin_header = get_code_token(collectPositoin_html)
        form_post(url=collectPosition_url,headers=collectPositoin_header,data=collectPositoin_data,remark='收藏')

collection(getpositionidfromcompanyid(142128),1)