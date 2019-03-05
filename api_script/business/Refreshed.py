#2018秋版合同刷新职位
#需要自己配置等待多长时间
from utils.util import login ,get_code_token,form_post,assert_equal
import time

login('00852','20181205')
def Refreshed(second):
    '''
    18版合同“刷新职位”
    :return:
    '''
    position_url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    position_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    s = form_post(url=position_url,headers=position_header,data={'pageNo':1},remark='获取职位id')
    positionId=s['content']['data']['parentPositionVOs'][0]['positions'][0]['positionId']
    print(positionId)
    refresh_url = "https://easy.lagou.com/position/refreshPosition.json"
    refresh_header = get_code_token("https://easy.lagou.com/position/my_online_positions.htm?pageNo=1")
    refresh_data = {'positionId': positionId}
    print (refresh_header)
    jsonobject = form_post(url=refresh_url,headers=refresh_header,data=refresh_data,remark='刷新职位')
    a=jsonobject.get("message")
    print(a)

    if a=="操作成功":
        assert_equal("操作成功",a,"首次刷新成功","首次刷新失败")
    else:
        time.sleep(second)
        jsonobject = form_post(url=refresh_url,headers=refresh_header,data=refresh_data,remark='刷新职位')
        assert_equal("操作成功",a,"首次刷新成功","首次刷新失败")


