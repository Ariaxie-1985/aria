# coding:utf-8
# @Time  : 2019-02-18 15:29
# @Author: Xiawang

import pytest

from utils.util import login, login_home, login_home_code
from utils.util import login_password
from api_script.jianzhao_web.talent.B_looking_for_talent import rec_talent,talent_collection_list



# 非灰度公司帐号
@pytest.fixture(params=[["00852", "20181205"]])
def login_web_k8s_default(request):
    login(request.param[0], request.param[1])


@pytest.fixture()
def login_home_k8s_default():
    login_home_code('00853', 22222222)


# 灰度公司，北京，免费，开通招聘服务，职务非HR
@pytest.fixture(params=[["0086", "18850430034"]])
def login_web_k8s_143242_TL1(request):
    login(request.param[0], request.param[1])


# 灰度公司，北京，付费，开通招聘服务，职务HR
@pytest.fixture(params=[["0086", "18850430035"]])
def login_web_k8s_142373_TL1(request):
    login(request.param[0], request.param[1])


# 灰度公司，北京，付费，开通招聘服务，职务非HR
@pytest.fixture(params=[["0086", "18850430036"]])
def login_web_k8s_142373_TL2(request):
    login(request.param[0], request.param[1])


# 灰度公司，北京，付费，开通招聘服务，职务非HR
@pytest.fixture(params=[["0086", "18850430037"]])
def login_web_k8s_142373_TL3(request):
    login(request.param[0], request.param[1])


# 灰度公司，太原，免费，开通招聘服务，职务HR
@pytest.fixture(params=[["0086", "18850430030"]])
def login_web_k8s_143232_TL1(request):
    login(request.param[0], request.param[1])


# 灰度公司，无城市，免费，开通招聘服务，职务非HR
@pytest.fixture(params=[["0086", "18850430031"]])
def login_web_k8s_143235_TL1(request):
    login(request.param[0], request.param[1])


# 灰度公司，无城市，免费，未完成招聘者审核
@pytest.fixture(params=[["0086", "18850430032"]])
def login_web_k8s_143236_TL1(request):
    login(request.param[0], request.param[1])


#有一个在线职位的账号
@pytest.fixture(scope='session', params=[["bingoonchen@lagou.com", "990eb670f81e82f546cfaaae1587279a"]])
def my_login_password(request):
        login_password(request.param[0], request.param[1])


# #获取收藏人才的cueserid和resumeFetchKey
# @pytest.fixture()
# def get_collection_info():
#     res = rec_talent()
#     cueserid = res.get('data').get('page').get('resuit')[0].get('userId')
#     resumeFetchKey = res.get('data').get('page').get('resuit')[0].get('resumeFetchKey')
#     return cueserid,resumeFetchKey
#
# #获取取消收藏人才的collectionIds
# def get_uncollection_id():
#     res = talent_collection_list()
#     collectionIds = res.get('data').get('page').get('resuit')[0].get('id')
#     return collectionIds