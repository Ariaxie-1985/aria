from api_script.jianzhao_web.b_basic.toB_saveHR_1 import saveHR, b_register,add_saveCompany
from faker import Faker
import pytest
import time
import json

from utils.util import assert_equal

fake = Faker("zh_CN")
countryCode, phone = "00852", str(20000000 + int(str(time.time()).split('.')[1]))
company_name = fake.name()
def test_join_company_2():
    register = b_register(phone, contryCode)
    if register['state'] == 1:
        personal_msg_save_and_join_company = add_saveCompany()
            if personal_msg_save_and_join_company['state'] == 1:
                upload_p = upload_permit()
                    if upload_p['state'] == 1:
                        personal_certificate_submit = submit_new()
                        assert_equal(1, personal_certificate_submit['state'], "校验提交招聘者身份审核是否成功")
                    else:
                        assert_equal(1, upload_p['state'], "校验提交身份信息是否成功")

            else:
                assert_equal(1, personal_msg_save_and_join_company['state'], "校验加入公司是否成功")
    else:
        assert_equal(1, register['state'], "校验B端用户注册是否成功")


if __name__ == '__main__':
    test_join_company_2()