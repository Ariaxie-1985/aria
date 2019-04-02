# -*- coding: utf8 -*-
__author__ = 'yqzhang'
from api_script.jianzhao_web.gouinH5.reward import reward
from utils.util import login, assert_equal
from api_script.jianzhao_web.gouinH5.tasks import tasks
def setup_module(module):
    pass


def teardown_module(module):
    pass

def test_reward():
    s=tasks().json()
    list=s['content']['data']['taskPage']['dayTasks']['taskList']
    for i in list:
        if i['status']=='COMPLETED':
            # print (i)
            break
            # assert_equal(1, 1, "没有可领取的任务")
    r=reward(i['taskLabel'],'TASK_GROUP_DAY',i['rCode'])
    assert_equal(1, r['state'], "领取成功")

# test_reward()