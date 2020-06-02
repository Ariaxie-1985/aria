# coding:utf-8
# @Time  : 2020/6/2 10:31
# @Author: Xiawang
# Description:
import pytest

from api_script.open_lagou_com.authority import open_authority_token


@pytest.fixture(scope='session')
def get_access_token():
    res = open_authority_token(appid='b1a5rsdsi7qukd3x', secret='2lvvus0lztf692u4vt9hqxare5qbm9ap',
                               grant_type='client_credential')

    return res.get('access_token')
