# coding:utf-8
# @Time  : 2019-07-09 14:39
# @Author: Sunnyzhang

from utils.util import get_requests, get_code_token, json_post
from utils.read_file import read_shop_time,record_shop_time
import datetime,os,json


def create_shop_goodsOrder_course(payLagouCoinNum, sellGoodsPriceId, gateLoginToken, shopOrderToken):
    url = 'https://gate.lagou.com/v1/zhaopin/shop/goodsOrder/create'
    header = get_code_token(url='https://easy.lagou.com/shop/onSaleGoods.htm?')
    header.update({'X-L-REQ-HEADER': json.dumps({'deviceType': 1}), "Cookie": f"gate_login_token ={gateLoginToken};",
                'shop-order-token': shopOrderToken})
    data = {
        "payLagouCoinNum": payLagouCoinNum,
        "sellGoodsPriceId": sellGoodsPriceId,
        "expandInfo": "https://kaiwu.lagou.com/course/courseInfo.htm?"
    }
    remark = '课程订单创建'
    return json_post(url=url, headers=header, data=data, remark=remark, rd='Mrpro Liu')

'''首次执行用例时，写入当前用例执行时间
非首次对比当前用例执行时间与上次用例执行时间,获取时间差'''
def lead_time():
    # 获取当前文件的上级目录
    file_path = os.getcwd()
    #获取当前时间并转换为字符串格式
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #将date转换为datetime.datetime类型的
    date1 = datetime.datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
    #读文档查看文档是否有值
    shoptime = read_shop_time(file_path).strip()
    if shoptime:
        date2 = datetime.datetime.strptime(shoptime, '%Y-%m-%d %H:%M:%S')
        leadtime = int(((date1 - date2).seconds) / 60)
        # if leadtime > 60:
        #     record_shop_time(file_path, date1)
        return leadtime
    else:
        record_shop_time(file_path,date1)

if __name__ == '__main__':
    print(lead_time())
