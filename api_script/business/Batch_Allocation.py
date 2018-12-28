#批量分配
from util.util import login ,get

login('00852','20181205')
#查看是否出现可以批量分配
def batch_allocation():
    r = get("https://easy.lagou.com/subAccount/queryAcount.json?pageNo=1&pageSize=7&keyword=","获取当前有几个子账号")

    print(r)

batch_allocation()