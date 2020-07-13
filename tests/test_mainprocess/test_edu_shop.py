# coding:utf-8
# @Time  : 2020/3/6 17:19
# @Author: Xiawang
# Description:
import pytest,os,datetime
from api_script.education.course import get_course_info
from api_script.education.shop import create_shop_goodsOrder_course, lead_time
from api_script.education.edu import get_course_list
from utils.util import assert_equal, assert_not_equal
from utils.read_file import read_shop_time,record_shop_time

orderNo = {}
nohasBuy_courseids = {}

@pytest.mark.incremental
class TestShopGoodOrderCourse(object):
    def test_get_course_list(self, c_login_education):
        r = get_course_list(userToken=c_login_education[0])
        assert_equal(1, r[0]["state"], "获取课程列表用例成功", te='张红彦')
        global nohasBuy_courseid_list
        nohasBuy_courseid_list = r[2]

    def test_get_course_info(self, get_h5_token):
        for id in nohasBuy_courseid_list:
            r = get_course_info(courseId=id, gateLoginToken=get_h5_token)
            nohasBuy_courseids.update({id: {"sellGoodsPriceId": r[0], "joinMember": r[1], "joinSeckill": r[2],
                                            "lgCoinPrice": r[3], "discounts": r[4], "freeForVip": r[5],
                                            "courseType": r[6], "orderToken": r[7]}})
            assert_equal(True, bool(r[0]), "获取课程价格&售卖策略用例通过", te='张红彦')

    # @pytest.mark.parametrize("id", nohasBuy_courseid_list=nohasBuy_courseid_list)
    def test_create_shop_goodsOrder_course(self,get_h5_token):
        for id in nohasBuy_courseid_list:
            leadtime = lead_time()
            result = create_shop_goodsOrder_course(payLagouCoinNum=nohasBuy_courseids[id]["lgCoinPrice"],
                                                   sellGoodsPriceId=nohasBuy_courseids[id]["sellGoodsPriceId"],
                                                   gateLoginToken=get_h5_token,
                                                   shopOrderToken=nohasBuy_courseids[id]["orderToken"])
            print(result["content"]["orderNo"])
            assert_equal(True, bool(result["content"]["orderNo"]), '课程创建订单用例通过', te='张红彦')
            if leadtime > 60:
                file_path = os.getcwd()
                record_shop_time(file_path,datetime.datetime.now())
                print("执行到这里了吗，不能写入当前时间",leadtime,read_shop_time(file_path),result["content"]["orderNo"],orderNo[id])
                assert_not_equal(result["content"]["orderNo"], orderNo[id], "大于一小时重新生成新订单用例通过", te='张红彦')
                orderNo.update({id: result["content"]["orderNo"]})
                print("在断言后执行了更新字典")
            elif leadtime > 0:
                print("222222222222", leadtime, read_shop_time(file_path))
                assert_equal(result["content"]["orderNo"], orderNo[id], "一小时内订单id未变用例通过", te='张红彦')
            else:
                orderNo.update({id: result["content"]["orderNo"]})
                print("3333333333", leadtime, read_shop_time(file_path))





