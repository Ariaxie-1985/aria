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


pytest.skip("有问题, 暂不执行")


def test_OrderResumes(login_web_k8s_default):
	'''
		1、分页查询简历
	2、生成或获取简历公开查看链接
	生成或获取简历公开查看链接(Alanzhang)
	  简历详情查询
	:return:
	'''
	orderResumes(100014641)
	checkOrderResumes(100014641)
	viewOrderResume(100014641)
	viewOrderResumeid(100014641)
