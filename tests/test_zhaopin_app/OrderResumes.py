# coding:utf-8
# @Time  : 2019-01-27 16:22
# @Author: cloudyyuan
import pytest

from api_script.zhaopin_app.OrderResume_app.MySchedule import SendBusiness, ScheduleList
from api_script.zhaopin_app.OrderResume_app.OrderResumePage import OrderResumespage, OrderResumespageStage, NotReadCount
from api_script.zhaopin_app.OrderResume_app.OrderResumes import orderResumes, checkOrderResumes, viewOrderResume, \
	viewOrderResumeid
from api_script.zhaopin_app.OrderResume_app.ResumeState import ResumeID, OrderResumeState, Interview, \
	reviseOrderResumesTime, luyong
from api_script.zhaopin_app.OrderResume_app.TopCard import offlineWin, OperateSchedule, PositionId
from utils.util import get_app_header, form_post, get_requests, assert_equal, login, get_code_token
from api_script.zhaopin_app.OrderResume_app import MySchedule, OrderResumePage, OrderResumes, ResumeState, TopCard
from utils.util import login

# pytest.skip("有问题, 暂不执行")

@pytest.mark.skip(reason="有问题, 暂不执行")
def test_OrderResumes(login_web_k8s_default):
	'''
	获得简历id
	设置为待沟通
	安排面试时间
	修改面试时间
	标记为录用
	转移到已入职
	淘汰
	:return:
	'''
	ResumeID(100014641)
	OrderResumeState(100014641)
	Interview(100014641)
	reviseOrderResumesTime(100014641)
	luyong(100014641)
