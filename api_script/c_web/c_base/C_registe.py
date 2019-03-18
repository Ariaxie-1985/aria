# coding:utf-8

from utils.util import get_code_token, form_post, get_requests, login

'''
注册
'''


def register(countryCode, phone):
    c_register_html = 'https://passport.lagou.com/register/register.html?from=c'
    register_url = 'https://passport.lagou.com/register/register.json'
    register_data = {'isValidate': 'true', 'phone': phone, 'phoneVerificationCode': '049281', 'challenge': 111,
                     'type': 0, 'countryCode': countryCode}
    register_header = get_code_token(c_register_html)
    return form_post(url=register_url, headers=register_header, data=register_data, remark='注册')


'''
头像
'''


def perfectresume():
    basicMain_html = 'https://www.lagou.com/resume/perfectresume.html'
    remark = '创建简历的初始页面'
    get_requests(url=basicMain_html, remark=remark)

    head_url = 'https://www.lagou.com/resume/saveHeadPic.json?headPicPath={}'.format(
        '/common/image/pc/default_boy_headpic2.png')
    remark = "上传头像"
    get_requests(url=head_url, remark=remark)


'''
基本信息
'''


def basicMain(userIdentity):
    basicMain_html = 'https://www.lagou.com/resume/perfectresume.html'
    basicMain_url = 'https://www.lagou.com/resume/basicMain.json'
    basicMain_header = get_code_token(basicMain_html)
    basicMain_data = {'name': 'zyq', 'birthday': '1995.10', 'sex': '男', 'email': '940238856@qq.com', 'userIdentity': userIdentity,
                      'liveCity': '北京', 'joinWorkTime': '2011.05'}
    return form_post(url=basicMain_url, headers=basicMain_header, data=basicMain_data, remark='基本信息')


'''
工作经历
'''


def workExperience():
    basicMain_html = 'https://www.lagou.com/resume/perfectresume.html'
    workExperience_url = "https://www.lagou.com/workExperience/save.json"
    workExperience_data = {"positionType": "Java", "positionType1": "开发|测试|运维类", "positionType2": "后端开发",
                           "skillLabels": "服务器端,Java,数据库", "department": "技术工程部", "companyIndustry": "企业服务",
                           "companyName": "拉勾网", "positionName": "Java", "startDate": "2012.08", "endDate": "至今",
                           "workContent": "<p>为了APIAPPMysqlRedisMQZKHTTPMotan<br></p>", "isItVisible": 1}
    workExperience_header = get_code_token(basicMain_html)
    return form_post(url=workExperience_url, headers=workExperience_header, data=workExperience_data, remark='工作经历')


'''
教育经历
'''


def educationExperience():
    basicMain_html = 'https://www.lagou.com/resume/perfectresume.html'
    edu_header = get_code_token(basicMain_html)
    edu_url = 'https://www.lagou.com/educationExperience/save.json'
    edu_data = {'schoolName': '清华大学', 'education': '本科', 'professional': '计算机科学与技术', 'startDate': '2009',
                'endDate': '2013'}
    return form_post(url=edu_url, headers=edu_header, data=edu_data, remark='教育经历')


'''
个人名片
'''


def personalCard():
    basicMain_html = 'https://www.lagou.com/resume/perfectresume.html'
    personal_url = 'https://www.lagou.com/resume/personalCard.json'
    personal_header = get_code_token(basicMain_html)
    personal_data = {'myRemark': '<p>哈哈哈哈</p>', 'socialAccountJson': '[]', 'abilityLabels': '执行力'}
    form_post(url=personal_url, headers=personal_header, data=personal_data, remark='个人名片')


'''
求职意向
'''


def expectJobs():
    basicMain_html = 'https://www.lagou.com/resume/perfectresume.html'
    expextJobs_url = 'https://www.lagou.com/expectJobs/expectJobs.json'
    expectJobs_header = get_code_token(basicMain_html)
    expectJobs_data = {'city': '北京', 'positionType': '全职', 'positionName': '机器学习', 'positionNameType1': '开发|测试|运维类',
                       'positionNameType2': '人工智能', 'salarys': '10k-20k', 'status': '随便看看', 'arrivalTime': '随时'}
    form_post(url=expextJobs_url, headers=expectJobs_header, data=expectJobs_data, remark='求职意向')
