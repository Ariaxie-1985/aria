import logging

from utils.util import login_password
from api_script.jianzhao_web.talent.B_looking_for_talent import rec_talent,new_talent,talent_inspect
from utils.util import assert_equal,assert_not_equal

login_password ('bingoonchen@lagou.com', '990eb670f81e82f546cfaaae1587279a')
positionid = '7245705'



#推荐人才页面验证
def test_talentSearch():

    res = rec_talent(positionid)
    sta= res['content']['data']['page']['totalCount']
    log = logging.getLogger('test_talentSearch')
    log.info('验证推荐人才页面信息展示')

    assert_equal (1, res['state'], "推荐人才成功"," 推荐人才成功失败" )
    assert_not_equal (0, sta, "数据返回成功","未返回数据" )

#切换最新人才，谁看过我标签
def test_switch_title():
    res_newtalent = new_talent(positionid)
    res_inspect = talent_inspect(positionid)
    print(res_newtalent)
    assert_equal (1, res_newtalent['state'], "最新人才tab切换成功"," 最新人才tab切换失败" )
    assert_equal (1, res_inspect['state'], "谁看过我tab切换成功", " 谁看过我tab切换失败")



