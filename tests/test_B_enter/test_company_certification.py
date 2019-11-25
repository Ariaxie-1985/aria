from api_script.jianzhao_web.b_basic.toB_comleteInfo_3 import company_auth, completeInfo
import pytest
import json

from utils.util import assert_equal, get_code_token, login


def company_certification():
    company_auth()
    completeInfo()

if __name__ == '__main__':
    login('00852', '24482062')
    company_certification()
