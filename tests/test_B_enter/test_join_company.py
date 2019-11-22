from api_script.jianzhao_web.b_basic.toB_saveHR_1 import saveHR, b_register,add_saveCompany, submit_new
from api_script.jianzhao_web.b_basic.b_upload import upload_permit
from faker import Faker
import pytest
import time
import json

from utils.util import assert_equal

fake = Faker("zh_CN")
countryCode, phone = "00852", str(20000000 + int(str(time.time()).split('.')[1]))
company_name = fake.company()
name = fake.name()
@pytest.mark.parametrize("name", [(fake.name())])
def test_join_company():
    register = b_register('13901122266', '0086')
    if register['state'] == 1:
        personal_msg_save = saveHR("XM02", name, 'ariaxie@lagou.com')
        if personal_msg_save['state'] == 1:
            personal_msg_save_and_join_company = add_saveCompany()
            if personal_msg_save_and_join_company['state'] == 1:
                upload_p = upload_permit()
                personal_certificate_submit = submit_new()
            else:
                assert_equal(1, personal_msg_save_and_join_company['state'], "校验加入公司是否成功")
        else:
                assert_equal(1, personal_msg_save['state'], "校验个人信息是否保存成功")
    else:
        assert_equal(1, register['state'], "校验是否注册成功")

# register = b_register('13901122230', '0086')
# personal_msg_save = saveHR("拉勾测试-XM", name, 'ariaxie@lagou.com')
# personal_msg_save_and_join_company = add_saveCompany()
# upload_p = upload_permit()
# personal_certificate_submit = submit_new()






if __name__ == '__main__':
    test_join_company()

