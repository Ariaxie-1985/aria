#批量分配

import json

from api_script.business.sub_account import get_user_goods_info, get_userId
from utils.BeautifulSoup import exist_class_name
from utils.util import login,get_requests,form_post,get_code_token,gethtml,assert_equal
import logging
logging.getLogger().setLevel(logging.INFO)

#
username = 20181205
login("00852", username)
#查看是否出现可以批量分配
def batch_allocation(userId_list):
    userId_list = [str(y) for y in userId_list]
    headerurl="https://easy.lagou.com/subAccount/queryAcount/index.htm"
    header = get_code_token(headerurl)
    jsonobject = get_requests(url="https://easy.lagou.com/subAccount/queryAcount.json?pageNo=1&pageSize=7&keyword=",remark="获取当前有几个子账号")
    childaccount = jsonobject.json()['content']['data']['subAcccountPage']['totalCount']
    # childaccount=jsonobject.get("content").get("data").get("subAcccountPage").get("totalCount")
    print('当前有' + str(childaccount) + '个子账号')
    if childaccount < 2:
        #b=exist_class_name("https://easy.lagou.com/subAccount/queryAcount/index.htm")
        b=gethtml("https://easy.lagou.com/subAccount/queryAcount/index.htm")
        a=exist_class_name(b,"batch-handle-btn ")
        assert_equal(True,a,"没有出现批量分配","出现了批量分配")
        while childaccount < 2:
                add1=form_post(url="https://easy.lagou.com/subAccount/addAcount.json",data={'userId':userId_list[0]},remark="添加子账号",headers=header)
                add1=form_post(url="https://easy.lagou.com/subAccount/addAcount.json",data={'userId':userId_list[1]},remark="添加子账号",headers=header)
                jsonobject = get_requests(url="https://easy.lagou.com/subAccount/queryAcount.json?pageNo=1&pageSize=7&keyword=",remark="获取当前有几个子账号")
                childaccount = jsonobject.json()['content']['data']['subAcccountPage']['totalCount']
                print('添加后' + str(childaccount) + '个子账号')
                b=gethtml("https://easy.lagou.com/subAccount/queryAcount/index.htm")
                a=exist_class_name(b,"batch-handle-btn ")
                assert_equal(False,a,"出现了批量分配,正确","没有出现了批量分配,失败")
    else:
        b=gethtml("https://easy.lagou.com/subAccount/queryAcount/index.htm")
        a=exist_class_name(b,"batch-handle-btn ")
        assert_equal(True,a,"出现了批量分配按钮","没有出现批量分配按钮")



'''
1、批量分配
2、验证是否分配成功
'''
def batchAllocate(userId_list, user_goods_info):
    goods_list = user_goods_info[userId_list[0]][2]
    goods_list = [str(x) for x in goods_list]
    userId_list = [str(y) for y in userId_list]
    headerurl="https://easy.lagou.com/subAccount/queryAcount/index.htm"
    header = get_code_token(headerurl)
    batchAllocate_url="https://easy.lagou.com/userGoodsRecord/batchAllocate"
    batchAllocate_Data={"allocateInfo":[{"userId":userId_list[0],"allocateDetail":[{"baseGoodsId":goods_list[0],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[1],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[2],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[3],"allocateNum":"1"}]},
                                                                                # {"baseGoodsId":"614","allocateNum":"1"}]},
                                        {"userId":userId_list[1],"allocateDetail":[{"baseGoodsId":goods_list[0],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[1],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[2],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[3],"allocateNum":"1"}]}]}
                                                                                # {"baseGoodsId":"614","allocateNum":"1"}]}]}
    batchAllocate_Data["allocateInfo"] = json.dumps(batchAllocate_Data["allocateInfo"])
    jsonobject =form_post(url=batchAllocate_url,remark="批量分配每个用户1个",data=batchAllocate_Data,headers=header)
    actualvalue=jsonobject.get("message")
    assert_equal("批量分配成功",actualvalue,"批量分配成功","批量分配失败")
    headerurl="https://easy.lagou.com/subAccount/queryAcount/index.htm"
    header = get_code_token(headerurl)
    batchAllocate_url="https://easy.lagou.com/userGoodsRecord/batchAllocate"
    batchAllocate_Data={"allocateInfo":[{"userId":userId_list[0],"allocateDetail":[{"baseGoodsId":goods_list[0],"allocateNum":"9999"},
                                                                                {"baseGoodsId":goods_list[1],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[2],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[3],"allocateNum":"1"}]},
                                                                                # {"baseGoodsId":"614","allocateNum":"1"}]},
                                        {"userId":userId_list[1],"allocateDetail":[{"baseGoodsId":goods_list[0],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[1],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[2],"allocateNum":"1"},
                                                                                {"baseGoodsId":goods_list[3],"allocateNum":"1"}]}]}
                                                                                # {"baseGoodsId":"614","allocateNum":"1"}]}]}
    batchAllocate_Data["allocateInfo"] = json.dumps(batchAllocate_Data["allocateInfo"])
    jsonobject =form_post(url=batchAllocate_url,remark="批量分配每个用户1个",data=batchAllocate_Data,headers=header)
    actualvalue=jsonobject.get("message")
    assert_equal("批量分配异常批量分配失败，子账号需要分配的"+str(goods_list[0])+"权益总数大于父账号的剩余数量",actualvalue,"大于可分配数量，后台不允许分配","批量分配失败")

# batchAllocate()
# userinfo = get_userId()
# print(userinfo)
#
# user_goods_info = get_user_goods_info(userinfo)
# goods_list = user_goods_info[userinfo[0]][2]
# print(goods_list)
# # print(r)
#
# userId_list = [100014642, 100014643]
# batch_allocation(userId_list)