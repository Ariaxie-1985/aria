# coding:utf-8
# @Author: cloudyyuan

'''
登录home 然后根据版本号更换套餐
'''

from utils.util import login_home,form_post,get_header
import json
'''
获取当前时间
'''

def lagouPlus(templateId):
    '''
    终止当前套餐
    新增17套餐
    查看套餐是否正常
    :return:
    '''
    login_home("anan@lagou.com","990eb670f81e82f546cfaaae1587279a")

    header=get_header("https://home.lagou.com/")
    Request_url="https://home.lagou.com/crm/contractController/list.json"
    data={"companyId":142136}
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
    增加17版合同,增加的固定合同
    '''
    contractnumurl="https://home.lagou.com/crm/valueadded/product/open.json"

    data={"templateId":templateId,"num":1,"companyId":142136,"contractNo":"LG-HD-WANGXIA-18112801","userId":100014641,"startTimeStr":"2019-01-07","endTimeStr":"2020-01-10","upgrade":"false"}
    object=form_post(url=contractnumurl,remark="新增合同, 其id: "+str(templateId),data=data,headers=header)
    print(object)
    # treatycontents=get_requests(url="https://home.lagou.com/crm/olddata/queryByCsv.json?userId=100014641&pageIndex=0&pageSize=100&sortField=&sortOrder=&_=1546593382369",headers=header,remark="获取合同内容")
    # print(treatycontents.json())
    # #在线职位数
    # TotalNum=treatycontents.json()['data'][0]['num']
    # #PLUS权限
    # Pluspower=treatycontents.json()['data'][1]['num']
    # #发布职位数
    # PostsnNumber=treatycontents.json()['data'][2]['num']
    # #子账号数
    # users=treatycontents.json()['data'][3]['num']
    # print(str(str(TotalNum)+str(Pluspower)+str(PostsnNumber)+str(users)))
    # assert_equal("999.01.0999.0999.0",str(TotalNum)+str(Pluspower)+str(PostsnNumber)+str(users),"对比套餐内容，所得内容正确17版","对比套餐内容，所得内容不匹配")

#lagouPlus(87)
