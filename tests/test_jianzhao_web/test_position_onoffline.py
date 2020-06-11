import logging

import time
from api_script.jianzhao_web.b_position.B_postposition import get_online_positions,offline_position,republish_position,my_parent_positions
from api_script.jianzhao_web.b_position.B_offlineposition import get_online_positionId
from utils.util import assert_equal,assert_not_equal

#存在一个在线职位后，下线该职位
def test_offline_position(my_login_password):
    #获取在线职位id
    positionid = get_online_positionId()
    #下线职位
    status = offline_position(positionid)
    assert_equal (1, status['state'], "职位下线成功",f"职位下线失败:{status.get('message')}" )
    # 再发布该下线的职位
    reset = republish_position()
    assert_equal (1, reset['state'], "职位再发布成功", f"职位再发布失败:{reset.get ('message')}")

    '''
    #再发布该下线的职位
    re_status = republish_position(parentPositionId )
    assert_equal (1, re_status['state'], "职位再发布成功", f"职位再发布失败:{re_status.get ('message')}")    
    assert_equal (1, re_status['state'], "职位再发布成功", f"职位再发布失败:{re_status.get ('message')}")    
    '''










