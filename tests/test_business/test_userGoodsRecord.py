# coding:utf-8
# @Time  : 2019-05-22 11:09
# @Author: Xiawang
from api_script.business.userGoodsRecord import queryParentUser, sendApplyAssignGoodsWithNum, pendingApplyRecords, \
    countPendingApplyRecords, addAccountFromApply, allocateGoodsFromApply
from utils.util import assert_equal
import random
import pytest

applyForSubAccount = 2
test_queryParentUser_result = 2
@pytest.importorskip('test_userGoodsRecord.py', reason="等招聘线-添加和分配流程优化上线后再执行")

def test_queryParentUser(login_k8s_default_20021215):
    res = queryParentUser()
    global parentId, applybaseGoods
    len_data = len(res['content']['data']['data'])
    flag = random.randint(0, len_data - 1)
    parentId = res['content']['data']['data'][flag]['userid']
    applybaseGoods_list = [i for i in res['content']['data']['data'][flag]['applyModelList'] if
                           i['allocatableNum'] - i['applyNum'] > 10]
    applybaseGoods = applybaseGoods_list[random.randint(0, len(applybaseGoods_list) - 1)]
    global test_queryParentUser_result
    test_queryParentUser_result = assert_equal(True, len(res['content']['data']['data'][flag]['applyModelList']) > 0,
                                               '有付费权益可申请')


def test_sendApplyAssignGoodsWithNum():
    global applyForSubAccount, applybaseGoods
    applyForSubAccount = random.randint(0, 1)  # 1：申请成为子账号，0：仅申请权益
    applybaseGoods['applyNum'] = 10
    r = sendApplyAssignGoodsWithNum(parentId, applyForSubAccount, applybaseGoods)
    assert_equal(1, r['state'], '申请提交成功')


def test_countPendingApplyRecords(login_web_k8s_default):
    res = countPendingApplyRecords()
    assert_equal(1, res['state'], '查询成功')


def test_pendingApplyRecords():
    res = pendingApplyRecords()
    global applyRecordId
    applyRecordId = res['content']['data']['recordList'][0]['applyRecordId']
    assert_equal(1, res['state'], '查询成功')


@pytest.mark.skipif(applyForSubAccount == 0, reason='仅申请付费权益,非子账号')
def test_addAccountFromApply():
    res = addAccountFromApply(applyRecordId)
    assert_equal(1, res['state'], '添加子账号成功')


# @pytest.mark.skipif(applyForSubAccount == 0, reason='')
def test_allocateGoodsFromApply():
    global applybaseGoods
    applybaseGoods['allocateNum'] = 10
    res = allocateGoodsFromApply(applyRecordId, applybaseGoods)
    assert_equal(1, res['state'], '分配付费权益成功')
