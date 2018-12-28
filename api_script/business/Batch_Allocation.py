#批量分配
import json
from api_script.BeautifulSoup import exist_class_name
from api_script.util import login,get,form_post,get_code_token,gethtml
import logging
logging.getLogger().setLevel(logging.INFO)

username = 20181205
login("00852", username)
#查看是否出现可以批量分配
def batch_allocation():
    headerurl="https://easy.lagou.com/subAccount/queryAcount/index.htm"
    header = get_code_token(headerurl)
    jsonobject = get("https://easy.lagou.com/subAccount/queryAcount.json?pageNo=1&pageSize=7&keyword=","获取当前有几个子账号")
    childaccount=jsonobject.get("content").get("data").get("subAcccountPage").get("totalCount")
    print('当前有' + str(childaccount) + '个子账号')
    if childaccount < 2:
        #b=exist_class_name("https://easy.lagou.com/subAccount/queryAcount/index.htm")
        b=gethtml("https://easy.lagou.com/subAccount/queryAcount/index.htm")
        a=exist_class_name(b,"batch-handle-btn ")
        while childaccount < 2:
                add1=form_post(url="https://easy.lagou.com/subAccount/addAcount.json",data={'userId':100014642},remark="添加子账号",headers=header)
                add1=form_post(url="https://easy.lagou.com/subAccount/addAcount.json",data={'userId':100014643},remark="添加子账号",headers=header)
                jsonobject = get("https://easy.lagou.com/subAccount/queryAcount.json?pageNo=1&pageSize=7&keyword=","获取当前有几个子账号")
                childaccount=jsonobject.get("content").get("data").get("subAcccountPage").get("totalCount")
                print('添加后' + str(childaccount) + '个子账号')
batch_allocation()