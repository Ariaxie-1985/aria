# coding:utf-8
# @Time  : 2020/7/14 17:19
# @Author: Sunnyzhang
# Description:
import pytest, os, ast
from api_script.education.course import get_course_info
from api_script.education.shop import create_shop_goodsOrder_course, lead_time,local_time
from api_script.education.edu import get_course_list
from utils.util import assert_equal, assert_not_equal
from utils.read_file import read_shop_time, record_shop_time,record_shop_order,read_shop_order
from utils.loggers import logers

loger = logers()

orderNo = {}
nohasBuy_courseids = {}


@pytest.mark.incremental
class TestShopGoodOrderCourse(object):
    def test_get_course_list(self, c_login_education_041701):
        r = get_course_list(userToken=c_login_education_041701[0])
        assert_equal(1, r[0]["state"], "获取课程列表用例成功", te='张红彦')
        global nohasBuy_courseid_list
        nohasBuy_courseid_list = r[2]

    def test_get_course_info(self, get_shop_h5_token):
        for id in nohasBuy_courseid_list:
            r = get_course_info(courseId=id, gateLoginToken=get_shop_h5_token)
            nohasBuy_courseids.update({id: {"sellGoodsPriceId": r[0], "joinMember": r[1], "joinSeckill": r[2],
                                            "lgCoinPrice": r[3], "discounts": r[4], "freeForVip": r[5],
                                            "courseType": r[6], "orderToken": r[7]}})
            assert_equal(True, bool(r[0]), "获取课程价格&售卖策略用例通过", te='张红彦')

    def test_create_shop_goodsOrder_course(self, get_shop_h5_token):
        file_path = os.getcwd()
        date1 = local_time()
        orderNofile = read_shop_order(file_path)
        b = list(orderNofile.keys())
        for id in nohasBuy_courseid_list:
            leadtime = lead_time(date1)
            result = create_shop_goodsOrder_course(payLagouCoinNum=nohasBuy_courseids[id]["lgCoinPrice"],
                                                   sellGoodsPriceId=nohasBuy_courseids[id]["sellGoodsPriceId"],
                                                   gateLoginToken=get_shop_h5_token,
                                                   shopOrderToken=nohasBuy_courseids[id]["orderToken"])

            assert_equal(True, bool(result["content"]["orderNo"]), '课程创建订单用例通过', te='张红彦')
            #如果读取的文件中有值且id在list中，则进行断言，否则直接将值加入字典中即可
            if id in b:
                if leadtime > 60:
                    assert_not_equal(result["content"]["orderNo"], orderNofile[id], "大于一小时重新生成新订单用例通过", te='张红彦')
                    record_shop_time(file_path, date1)
                    orderNo.update({id: result["content"]["orderNo"]})
                elif leadtime > 0:
                    assert_equal(result["content"]["orderNo"], orderNofile[id], "一小时内订单id未变用例通过", te='张红彦')
                    orderNo.update({id: result["content"]["orderNo"]})
                else:
                    orderNo.update({id: result["content"]["orderNo"]})
            else:
                orderNo.update({id: result["content"]["orderNo"]})
        record_shop_order(file_path,orderNo)
