
from api_script.jianzhao_web.b_basic.toB_saveHR_1 import b_register, saveHR, saveCompany, submit, add_saveCompany, submit_new
from api_script.jianzhao_web.b_basic.b_upload import upload_permit
from faker import Faker
import pytest
import time
import json

from utils.util import assert_equal

fake = Faker("zh_CN")
countryCode, phone = "00852", str(20000000 + int(str(time.time()).split('.')[1]))
company_name = fake.company() + str(20000000 + int(str(time.time()).split('.')[1]))
name = fake.name()
@pytest.mark.parametrize("name", [(fake.name())])
def test_create_company_info(name):
    register = b_register(phone, countryCode)
    if register['state'] == 1:
        personal_msg_save_and_creat_company = saveHR('拉勾测试公司全称{}'.format(company_name), name, 'ariaxie@lagou.com')
        if personal_msg_save_and_creat_company['state'] == 1:
            company_msg_save = saveCompany('公司简称{}'.format(company_name))
            assert_equal(1, company_msg_save['state'], "校验公司是否新建成功")
        else:
            assert_equal(1, personal_msg_save_and_creat_company['state'], "校验HR信息是否保存成功")
    else:
        assert_equal(1, register['state'], "校验B端用户注册是否成功")

def test_personal_certificate():
    upload_p = upload_permit()
    if upload_p['state'] == 1:
        personal_certificate_submit = submit_new()
        assert_equal(1,personal_certificate_submit['state'], "校验提交招聘者身份审核是否成功")
    else:
        assert_equal(1, upload_p['state'], "校验提交身份信息是否成功")



if __name__ == '__main__':
    test_create_company_info(name)
    test_personal_certificate()
