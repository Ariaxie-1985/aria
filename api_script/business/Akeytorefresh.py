#2018秋版合同一键刷新

from utils.util import login ,get_code_token,form_post,assert_equal
import time

login("00852","20181205")
'''
获取第二个职位进行一键刷新
'''
def akeyRefresh(second):

    position_url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    position_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    s = form_post(url=position_url,headers=position_header,data={'pageNo':1},remark='获取职位id')
    positionId=s['content']['data']['parentPositionVOs'][1]['positions'][0]['positionId']
    print(positionId)
    refresh_url = "https://easy.lagou.com/parentPosition/multiChannel/statistics.json"
    refresh_header = get_code_token("https://easy.lagou.com/position/my_online_positions.htm?pageNo=1")
    refresh_data = {'needCandidateNum':'true','parentIds': positionId}
    print (refresh_header)
    jsonobject = form_post(url=refresh_url,headers=refresh_header,data=refresh_data,remark='一键刷新职位')
    a=jsonobject.get("message")
    print(a)

    if a=="操作成功":
        assert_equal("操作成功",a,"一键刷新成功","一键刷新失败")
    else:
        time.sleep(second)
        jsonobject = form_post(url=refresh_url,headers=refresh_header,data=refresh_data,remark='刷新职位')
        assert_equal("操作成功",a,"一键刷新成功","一键刷新失败")


def Refreshed(second):
    '''
    18版合同“一键刷新”
    刷新所有职位，包括已经刷新过一次的
    :return:
    '''
    position_url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    position_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    s = form_post(url=position_url,headers=position_header,data={'pageNo':1},remark='获取职位id')
    positionId=s['content']['data']['parentPositionIds']
    refresh_url = "https://easy.lagou.com/parentPosition/multiChannel/statistics.json"
    refresh_header = get_code_token("https://easy.lagou.com/position/my_online_positions.htm?pageNo=1")
    refresh_data = {'needCandidateNum':'true','parentIds': positionId}
    print (refresh_header)
    jsonobject = form_post(url=refresh_url,headers=refresh_header,data=refresh_data,remark='一键刷新职位')
    a=jsonobject.get("message")
    print(a)

    if a=="操作成功":
        assert_equal("操作成功",a,"一键刷新成功","一键刷新失败")
    else:
        time.sleep(second)
        jsonobject = form_post(url=refresh_url,headers=refresh_header,data=refresh_data,remark='刷新职位')
        assert_equal("操作成功",a,"一键刷新成功","一键刷新失败")

akeyRefresh(3000)
Refreshed(3000)
#
