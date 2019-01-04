#批量分配

import json
from util.BeautifulSoup import exist_class_name
from util.util import login,get_requests,form_post,get_code_token,gethtml,assert_equal
import logging
logging.getLogger().setLevel(logging.INFO)


username = 20181205
#login("00852", username)
#查看是否出现可以批量分配
def batch_allocation():
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
                add1=form_post(url="https://easy.lagou.com/subAccount/addAcount.json",data={'userId':100014642},remark="添加子账号",headers=header)
                add1=form_post(url="https://easy.lagou.com/subAccount/addAcount.json",data={'userId':100014643},remark="添加子账号",headers=header)
                jsonobject = get_requests(url="https://easy.lagou.com/subAccount/queryAcount.json?pageNo=1&pageSize=7&keyword=",remark="获取当前有几个子账号")
                childaccount = jsonobject.json()['content']['data']['subAcccountPage']['totalCount']
                print('添加后' + str(childaccount) + '个子账号')
                b=gethtml("https://easy.lagou.com/subAccount/queryAcount/index.htm")
                a=exist_class_name(b,"batch-handle-btn ")
                assert_equal(False,a,"出现了批量分配,正确","没有出现了批量分配,失败")
    else:
        b=gethtml("https://easy.lagou.com/subAccount/queryAcount/index.htm")
        a=exist_class_name(b,"batch-handle-btn ")
        assert_equal(False,a,"没有出现批量分配","出现了批量分配")


batch_allocation()

'''
1、批量分配
2、验证是否分配成功
'''
def batchAllocate():
    headerurl="https://easy.lagou.com/subAccount/queryAcount/index.htm"
    header = get_code_token(headerurl)
    batchAllocate_url="https://easy.lagou.com/userGoodsRecord/batchAllocate"
    batchAllocate_Data={"allocateInfo":[{"userId":"100014643","allocateDetail":[{"baseGoodsId":"704","allocateNum":"1"},
                                                                                {"baseGoodsId":"701","allocateNum":"1"},
                                                                                {"baseGoodsId":"706","allocateNum":"1"},
                                                                                {"baseGoodsId":"705","allocateNum":"1"},
                                                                                {"baseGoodsId":"614","allocateNum":"1"}]},
                                        {"userId":"100014642","allocateDetail":[{"baseGoodsId":"704","allocateNum":"1"},
                                                                                {"baseGoodsId":"701","allocateNum":"1"},
                                                                                {"baseGoodsId":"706","allocateNum":"1"},
                                                                                {"baseGoodsId":"705","allocateNum":"1"},
                                                                                {"baseGoodsId":"614","allocateNum":"1"}]}]}
    batchAllocate_Data["allocateInfo"] = json.dumps(batchAllocate_Data["allocateInfo"])
    jsonobject =form_post(url=batchAllocate_url,remark="批量分配每个用户1个",data=batchAllocate_Data,headers=header)
    actualvalue=jsonobject.get("message")
    assert_equal("批量分配成功",actualvalue,"批量分配成功","批量分配失败")
    headerurl="https://easy.lagou.com/subAccount/queryAcount/index.htm"
    header = get_code_token(headerurl)
    batchAllocate_url="https://easy.lagou.com/userGoodsRecord/batchAllocate"
    batchAllocate_Data={"allocateInfo":[{"userId":"100014643","allocateDetail":[{"baseGoodsId":"704","allocateNum":"99999"},
                                                                                {"baseGoodsId":"701","allocateNum":"1"},
                                                                                {"baseGoodsId":"706","allocateNum":"1"},
                                                                                {"baseGoodsId":"705","allocateNum":"1"},
                                                                                {"baseGoodsId":"614","allocateNum":"1"}]},
                                        {"userId":"100014642","allocateDetail":[{"baseGoodsId":"704","allocateNum":"1"},
                                                                                {"baseGoodsId":"701","allocateNum":"1"},
                                                                                {"baseGoodsId":"706","allocateNum":"1"},
                                                                                {"baseGoodsId":"705","allocateNum":"1"},
                                                                                {"baseGoodsId":"614","allocateNum":"1"}]}]}
    batchAllocate_Data["allocateInfo"] = json.dumps(batchAllocate_Data["allocateInfo"])
    jsonobject =form_post(url=batchAllocate_url,remark="批量分配每个用户1个",data=batchAllocate_Data,headers=header)
    actualvalue=jsonobject.get("message")
    assert_equal("批量分配异常批量分配失败，子账号需要分配的704权益总数大于父账号的剩余数量",actualvalue,"大于可分配数量，后台不允许分配","批量分配失败")

batchAllocate()

