# coding:utf-8
# @Author: cloudyyuan

'''
发布职位邀约
'''
from utils.util import login,get_code_token,form_post,get_header,get_requests,assert_equal

login('00852','20181205')
def hot():
    '''
    判断是否是热门职位
    :return:
    '''
    header=get_header("https://easy.lagou.com/dashboard/index.htm?")
    #data={"pageNo":1,"pageSize":15,"createBy":0,"unReadOnly":0}
    url="https://easy.lagou.com/parentPosition/multiChannel/hot/测试.json"
    object=get_requests(url=url,remark="判断是否是热门职位",headers=header)
    meassage=object['message']
    assert_equal("操作成功",meassage,"判断是否是热门职位成功","判断是否是热门职位失败")

def invaitonnumber():
    '''
    查询邀约候选人数量
    :return:
    '''
    position_url = 'https://easy.lagou.com/parentPosition/multiChannel/myOnlinePositions.json'
    position_header = get_code_token('https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm')
    s = form_post(url=position_url,headers=position_header,data={'pageNo':1},remark='获取职位id')
    positionId=s['content']['data']['parentPositionVOs'][1]['positions'][0]['positionId']
    print(positionId)
    header=get_header("https://easy.lagou.com/dashboard/index.htm?")
    #data={"pageNo":1,"pageSize":15,"createBy":0,"unReadOnly":0}
    url="https://easy.lagou.com/parentPosition/multiChannel/invitation/"+str(positionId)+".json"
    object=get_requests(url=url,remark="查询邀约候选人数量",headers=header)
    meassage=object['message']
    assert_equal("操作成功",meassage,"查询邀约候选人数量成功","查询邀约候选人数量失败")
#
#
#
# hot()
# invaitonnumber()