# coding:utf-8
# @Time  : 2019-01-27 16:22
# @Author: cloudyyuan
from api_script.zhaopin_app.OrderResume_app.MySchedule import SendBusiness, ScheduleList
from api_script.zhaopin_app.OrderResume_app.OrderResumePage import OrderResumespage, OrderResumespageStage, NotReadCount
from api_script.zhaopin_app.OrderResume_app.OrderResumes import orderResumes, checkOrderResumes, viewOrderResume, \
    viewOrderResumeid
from api_script.zhaopin_app.OrderResume_app.ResumeState import ResumeID, OrderResumeState, Interview, \
    reviseOrderResumesTime, luyong
from api_script.zhaopin_app.OrderResume_app.TopCard import offlineWin, OperateSchedule, PositionId
from utils.util import get_app_header,form_post,get_requests,assert_equal,login,get_code_token
from api_script.zhaopin_app.OrderResume_app import MySchedule,OrderResumePage,OrderResumes,ResumeState,TopCard
from utils.util import login
def test_TopCard():
    '''
    获取职位id
    使用置顶卡，既添加置顶卡排期
    置顶卡操作前，弹窗判断
    置顶卡操作下线或取消预订
    :return:
    '''
    PositionId()
    TopCard(100014641)
    offlineWin(100014641)
    OperateSchedule(100014641)
