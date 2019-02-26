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



@pytest.mark.skip(reason="有问题, 暂不执行")
def test_MySchedule(login_web_k8s_default):
	'''
	查询我的排期，包括共享职位
	  发送商机线索
	  查询未来28天排期
	:return:
	'''
	# MySchedule(100014641)
	SendBusiness(100014641)
	ScheduleList(100014641)

# def test_OrderResumes():
#     '''
#         1、分页查询简历
#     2、生成或获取简历公开查看链接
#     生成或获取简历公开查看链接(Alanzhang)
#       简历详情查询
#     :return:
#     '''
#     # orderResumes(100014641)
#     checkOrderResumes(100014641)
#     viewOrderResume(100014641)
#     viewOrderResumeid(100014641)
# def test_OrderResumes():
#     '''
#     获得简历id
#     设置为待沟通
#     安排面试时间
#     修改面试时间
#     标记为录用
#     转移到已入职
#     淘汰
#     :return:
#     '''
#     ResumeID(100014641)
#     OrderResumeState(100014641)
#     Interview(100014641)
#     reviseOrderResumesTime(100014641)
#     luyong(100014641)
# def test_TopCard():
#     '''
#     获取职位id
#     使用置顶卡，既添加置顶卡排期
#     置顶卡操作前，弹窗判断
#     置顶卡操作下线或取消预订
#     :return:
#     '''
#     PositionId()
#     TopCard(100014641)
#     offlineWin(100014641)
#     OperateSchedule(100014641)
