# coding:utf-8
# @Author: cloudyyuan

'''
home,在当前公司的合同下增加17和18套餐
'''

from utils.util import login_home, get_code_token, form_post, get_header, get_requests, assert_equal, wait, \
    login_home_code
import json
'''
获取当前时间
'''
<<<<<<< HEAD

=======
login_home_code("0086", "18810896987")
>>>>>>> 7557cba358193bc3f19e72720b5ba2e51c79f32e

def lagouPlus():
    '''
    终止当前套餐
    新增17套餐
    查看套餐是否正常
    :return:
    '''
    login_home("18810896987", "c47eeb69fa4e64971fb29cb1e9163a19")
    header=get_header("https://home.lagou.com/")
    Request_url="https://home.lagou.com/crm/contractController/list.json"
    data={"companyId":14}
    object=form_post(url=Request_url,remark="查询当前公司下的合同",data=data,headers=header)
    #childaccount = jsonobject.json()['content']['data']['subAcccountPage']['totalCount']
    number=object['data']['pageData'][0]['number']
    '''
    先终止合同
    '''
    Request_url="https://home.lagou.com/crm/valueadded/product/close.json"

    data={"contractNo":number}
    object=form_post(url=Request_url,remark="终止所有合同",data=data,headers=header)
    '''
    增加免费合同
    '''
    contractnumurl="https://home.lagou.com/crm/valueadded/product/open.json"

    data={"templateId":1,"num":1,"companyId":14,"contractNo":"LG-HD-WANGXIA-2019030401","userId":84,"startTimeStr":"2019-01-07","endTimeStr":"2020-01-10","upgrade":"false"}
    object=form_post(url=contractnumurl,remark="新增免费合同",data=data,headers=header)
    print(object)
    treatycontents=get_requests(url="https://home.lagou.com/crm/olddata/queryByCsv.json?userId=84&pageIndex=0&pageSize=100&sortField=&sortOrder=&_=1546593382369",headers=header,remark="获取合同内容")
    print(treatycontents.json())
    #在线职位数
    TotalNum=treatycontents.json()['data'][0]['num']
    #PLUS权限
    Pluspower=treatycontents.json()['data'][1]['num']
    #发布职位数
    PostsnNumber=treatycontents.json()['data'][2]['num']
    #子账号数
    users=treatycontents.json()['data'][3]['num']
    print('?????')
    print(str(str(TotalNum)+str(Pluspower)+str(PostsnNumber)+str(users)))
    print ('????')
    assert_equal("50.050.050.014.0",str(TotalNum)+str(Pluspower)+str(PostsnNumber)+str(users),"对比套餐内容，所得内容正确免费版","对比套餐内容，所得内容不匹配")

# lagouPlus()


def lagouPlusqiu():
    '''
    终止当前套餐
    新增18套餐
    查看套餐是否正常
    :return:
    '''
    login_home("18810896987", "c47eeb69fa4e64971fb29cb1e9163a19")
    header=get_header("https://home.lagou.com/")
    Request_url="https://home.lagou.com/crm/contractController/list.json"
    data={"companyId":14}
    object=form_post(url=Request_url,remark="查询当前公司下的合同",data=data,headers=header)
    print(object)
    print(object['data']['pageData'][0]['number'])
    #childaccount = jsonobject.json()['content']['data']['subAcccountPage']['totalCount']
    number=object['data']['pageData'][0]['number']
    '''
    先终止合同
    '''
    Request_url="https://home.lagou.com/crm/valueadded/product/close.json"
    wait(5000)
    data={"contractNo":number}
    object=form_post(url=Request_url,remark="终止所有合同",data=data,headers=header)
    '''
    增加17版合同,增加的固定合同
    '''
    contractnumurl="https://home.lagou.com/crm/valueadded/product/open.json"
    data={"templateId":5,"num":1,"companyId":14,"contractNo":"LG-HD-WANGXIA-2019030401","userId":84,"startTimeStr":"2019-01-07","endTimeStr":"2020-01-10","upgrade":"false"}
    object=form_post(url=contractnumurl,remark="新增18特权",data=data,headers=header)
    print(object)
    treatycontents=get_requests(url="https://home.lagou.com/crm/olddata/queryByCsv.json?userId=84&pageIndex=0&pageSize=100&sortField=&sortOrder=&_=1546593382369",headers=header,remark="获取合同内容")
    print(treatycontents.json())
    #在线职位数
    TotalNum=treatycontents.json()['data'][0]['num']
    #子账号
    users=treatycontents.json()['data'][1]['num']
    print('?????')
    print(str(TotalNum)+str(users))
    assert_equal("222.01.0",str(TotalNum)+str(users),"对比套餐内容，所得内容正确18版","对比套餐内容，所得内容不匹配")
    '''
      先终止合同
      '''
    Request_url="https://home.lagou.com/crm/valueadded/product/close.json"
    data={"contractNo":number}
    object=form_post(url=Request_url,remark="终止所有合同",data=data,headers=header)

    contractnumurl="https://home.lagou.com/crm/valueadded/product/open.json"
    data={"templateId":6,"num":1,"companyId":14,"contractNo":"LG-HD-WANGXIA-2019030401","userId":84,"startTimeStr":"2019-01-07","endTimeStr":"2020-01-10","upgrade":"false"}
    object=form_post(url=contractnumurl,remark="变成万能合同",data=data,headers=header)
# lagouPlusqiu()

