import logging

from utils.util import login_password
from api_script.jianzhao_web.talent.B_looking_for_talent import rec_talent,new_talent,talent_inspect
from utils.util import assert_equal,assert_not_equal

positionid = '7245705'
#推荐人才页面验证

def test_talentSearch(c_login_password):
    res = rec_talent(positionid)
    sta = res.get('content').get('data').get('page').get('totalCount')
    assert_equal (1, res['state'], "推荐人才成功",f"推荐人才成功失败:{res.get('message')}" )
    assert_not_equal (0, sta, "数据返回成功","未返回数据" )

#切换最新人才，谁看过我标签
def test_switch_title():
    res_newtalent = new_talent(positionid)
    #print(res_newtalent)
    res_inspect = talent_inspect(positionid)
    #print(res_inspect)
    assert_equal (1, res_newtalent['state'], "最新人才tab切换成功",f"最新人才tab切换失败:{res_newtalent .get('message')}" )
    assert_equal (1, res_inspect['state'], "谁看过我tab切换成功", f"谁看过我tab切换失败:{res_inspect.get('message')}")



