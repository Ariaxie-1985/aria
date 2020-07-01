import logging

import pytest

from utils.util import login_password
from api_script.jianzhao_web.talent.B_looking_for_talent import rec_talent,new_talent,talent_inspect
from utils.util import assert_equal,assert_not_equal
from api_script.jianzhao_web.talent.B_looking_for_talent import rec_talent,talent_collection_list,talent_collection,talent_uncollection,talent_pages


#推荐人才页面验证
@pytest.mark.parametrize ("positionid", [("6946522")])
def test_talentSearch(my_login_password,positionid):
    res = rec_talent(positionid)
    sta = res.get('content').get('data').get('page').get('totalCount')
    assert_equal (1, res['state'], "推荐人才成功",f"推荐人才成功失败:{res.get('message')}",te='陈梦丹')
    assert_not_equal (0, sta, "数据返回成功","未返回数据" )

#切换最新人才，谁看过我标签
@pytest.mark.parametrize ("positionid", [("6946522")])
def test_switch_title(positionid):
    res_newtalent = new_talent(positionid)
    #print(res_newtalent)
    res_inspect = talent_inspect(positionid)
    #print(res_inspect)
    assert_equal (1, res_newtalent['state'], "最新人才tab切换成功",f"最新人才tab切换失败:{res_newtalent.get('message')}",te='陈梦丹')
    assert_equal (1, res_inspect['state'], "谁看过我tab切换成功", f"谁看过我tab切换失败:{res_inspect.get('message')}",te='陈梦丹')

#验证收藏的操作
@pytest.mark.parametrize ("positionid", [("6946522")])
def test_collection(positionid):
    #获取收藏人才的cueserid和resumeFetchKey
    res = rec_talent(positionid)
    cueserid = res.get('content').get('data').get('page').get('result')[0].get('userId')
    resumeFetchKey = res.get('content').get('data').get('page').get('result')[0].get('resumeFetchKey')
    get_res = talent_collection(positionid,cueserid,resumeFetchKey)
    assert_equal (1, get_res.get('state'), "收藏成功",f"收藏失败，失败原因:{get_res.get('message')}",te='陈梦丹')

# 验证取消收藏的操作
def test_uncollection():
    # 获取收藏人才的collectionIds
    res = talent_collection_list()
    collectionIds = res.get('content').get('data').get('page').get('result')[0].get('id')
    get_res = talent_uncollection(collectionIds)
    a = get_res.get('state')
    assert_equal(1, get_res.get('state'), "取消收藏成功", f"取消收藏失败，失败原因:{get_res.get('message')}",te='陈梦丹')

# 上下翻页验证
@pytest.mark.parametrize("positionId", [('6946522')])
def test_pages(positionId):
    get_res = talent_pages(positionId)
    assert_equal(1, get_res.get('state'), "翻页成功", f"翻页失败，失败原因:{get_res.get('message')}",te='陈梦丹')










