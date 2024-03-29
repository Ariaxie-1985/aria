# coding:utf-8
# @Author: Xiawang

'''
批量注册并生成简历完整度81分的C端账号
'''
import time
from multiprocessing import Process
from utils.util import form_post, get_code_token, get_requests, login
from faker import Faker

fake = Faker("zh_CN")


def registe_c(phone, countryCode, userIdentity, kwargs={}):
    '''
    C端注册并生成简历
    :param phone: int, 注册手机号
    :param countryCode: str, 手机号归属地
    :param userIdentity: int, 是否学生，1学生, 2非学生
    :param kwargs:
    :return:
    '''
    if isinstance(kwargs, dict):
        name = kwargs.get('name', fake.name())
        birthday = kwargs.get('birthday', '1995.10')
        liveCity = kwargs.get('liveCity', '北京')
        joinWorkTime = kwargs.get('joinWorkTime', '2018.07')
        education = kwargs.get('education', '本科')
        startDate = kwargs.get('startDate', '2009')
        endDate = kwargs.get('endDate', '2013')
        city = kwargs.get('city', '北京')
        positionType = kwargs.get('positionType', '全职')
        positionName = kwargs.get('positionName', '机器学习')
        positionNameType1 = kwargs.get('positionNameType1', '开发|测试|运维类')
        positionNameType2 = kwargs.get('positionNameType2', '人工智能')
        salarys = kwargs.get('salarys', '10k-20k')

    # 注册
    c_register_html = 'https://passport.lagou.com/register/register.html?from=c'
    register_url = 'https://passport.lagou.com/register/register.json'
    register_data = {'isValidate': 'true', 'phone': phone, 'phoneVerificationCode': '049281', 'challenge': 111,
                     'type': 0, 'countryCode': countryCode}
    register_header = get_code_token(c_register_html)
    remark = "注册C端用户"
    r1 = form_post(url=register_url, headers=register_header, data=register_data, remark=remark)

    basicMain_html = 'https://www.lagou.com/resume/perfectresume.html?showQRCode=true'
    remark = '创建简历的初始页面'
    get_requests(url=basicMain_html, remark=remark)

    head_url = 'https://www.lagou.com/resume/saveHeadPic.json?headPicPath={}'.format(
        '/common/image/pc/default_boy_headpic2.png')
    remark = "上传头像"
    get_requests(url=head_url, remark=remark)

    if userIdentity == 2:
        # 基本信息
        basicMain_url = 'https://www.lagou.com/resume/basicMain.json'
        basicMain_header = get_code_token(basicMain_html)
        basicMain_data = {'name': name, 'birthday': birthday, 'sex': '男',
                          'email': '{}@testlagou.com'.format(phone),
                          'userIdentity': userIdentity, 'liveCity': liveCity, 'joinWorkTime': joinWorkTime}
        remark = "添加基本信息"
        r2 = form_post(url=basicMain_url, headers=basicMain_header, data=basicMain_data, remark=remark)

        # 工作经历
        workExperience_url = 'https://www.lagou.com/workExperience/save.json'
        workExperience_header = get_code_token(basicMain_html)
        workExperience_data = {"positionType": "机器学习", "positionType1": "开发|测试|运维类", "positionType2": "人工智能",
                               "skillLabels": "机器学习", "requestSource": 1,
                               "department": "大数据智能中心", "companyIndustry": "电商", "companyName": "拉勾网",
                               "positionName": "机器学习", "startDate": "2012.07",
                               "endDate": "2019.03", "workContent": "<p>哒哒哒哒哒哒多多多多多多多</p>", "isItVisible": 1}
        remark = "添加工作经历"
        r3 = form_post(url=workExperience_url, headers=workExperience_header, data=workExperience_data, remark=remark)
    else:
        # 基本信息
        basicMain_url = 'https://www.lagou.com/resume/basicMain.json'
        basicMain_header = get_code_token(basicMain_html)
        basicMain_data = {'name': name, 'birthday': birthday, 'sex': '男',
                          'email': '{}@testlagou.com'.format(phone),
                          'userIdentity': userIdentity, 'liveCity': liveCity}
        remark = "添加基本信息"
        r2 = form_post(url=basicMain_url, headers=basicMain_header, data=basicMain_data, remark=remark)

    # 教育经历
    edu_header = get_code_token(basicMain_html)
    edu_url = 'https://www.lagou.com/educationExperience/save.json'
    edu_data = {'schoolName': '清华大学', 'education': education, 'professional': '计算机科学与技术', 'startDate': startDate,
                'endDate': endDate}
    remark = "添加教育经历"
    r4 = form_post(url=edu_url, headers=edu_header, data=edu_data, remark=remark)

    # 个人名片
    personal_url = 'https://www.lagou.com/resume/personalCard.json'
    personal_header = get_code_token(basicMain_html)
    personal_data = {'myRemark': '<p>哈哈哈哈</p>', 'socialAccountJson': '[]', 'abilityLabels': '执行力'}
    remark = "添加个人名片"
    r5 = form_post(url=personal_url, headers=personal_header, data=personal_data, remark=remark)

    # 求职意向
    expextJobs_url = 'https://www.lagou.com/expectJobs/expectJobs.json'
    expectJobs_header = get_code_token(basicMain_html)
    expectJobs_data = {'city': city, 'positionType': positionType, 'positionName': positionName,
                       'positionNameType1': positionNameType1,
                       'positionNameType2': positionNameType2, 'salarys': salarys, 'status': '随便看看',
                       'arrivalTime': '随时'}
    remark = "添加求职意向"
    r6 = form_post(url=expextJobs_url, headers=expectJobs_header, data=expectJobs_data, remark=remark, rd='征桂')

    # 改善简历的头像和基本名片
    refer_myresume_html = 'https://www.lagou.com/resume/myresume.html'
    myresume_url = 'https://www.lagou.com/resume/saveHeadPic.json?headPicPath=%2Fcommon%2Fimage%2Fpc%2Fdefault_boy_headpic2.png'
    # myresume_header = get_code_token(refer_myresume_html)
    remark = "改善简历的头像和基本名片"
    # r7 = form_post(url=myresume_url, headers=myresume_header, remark=remark)
    r7 = {'success': True}

    # 完善个人信息
    basic_url = 'https://www.lagou.com/resume/basic.json'
    # myresume_header = get_code_token(refer_myresume_html)
    basic_data = {'liveCity': '北京', 'birthday': '1990.09', 'name': '周杰伦', 'email': '940238856@qq.com',
                  'sex': '男', 'type': 1, 'userIdentity': userIdentity, "phone": str(countryCode) + str(phone)}
    remark = "完善个人信息"
    # r8 = form_post(url=basic_url, headers=myresume_header, data=basic_data, remark=remark)
    r8 = {'success': True}

    if userIdentity == 2:
        return [r1, r2, r3, r4, r5, r6, r7, r8]
    else:
        return [r1, r2, r4, r5, r6, r7, r8]


def c_register(phone, countryCode):
    c_register_html = 'https://passport.lagou.com/register/register.html?from=c'
    register_url = 'https://passport.lagou.com/register/register.json'
    register_data = {'isValidate': 'true', 'phone': phone, 'phoneVerificationCode': '049281', 'challenge': 111,
                     'type': 0, 'countryCode': countryCode}
    register_header = get_code_token(c_register_html)
    remark = "注册C端用户"
    return form_post(url=register_url, headers=register_header, data=register_data, remark=remark)


def create_resume(phone, countryCode, userIdentity, kwargs={}):
    if isinstance(kwargs, dict):
        name = kwargs.get('name', fake.name())
        birthday = kwargs.get('birthday', '1995.10')
        liveCity = kwargs.get('liveCity', '北京')
        joinWorkTime = kwargs.get('joinWorkTime', '2018.07')
        education = kwargs.get('education', '本科')
        startDate = kwargs.get('startDate', '2009.09')
        endDate = kwargs.get('endDate', '2013.07')
        city = kwargs.get('city', '北京')
        positionType = kwargs.get('positionType', '全职')
        positionName = kwargs.get('positionName', '机器学习')
        positionNameType1 = kwargs.get('positionNameType1', '开发|测试|运维类')
        positionNameType2 = kwargs.get('positionNameType2', '人工智能')
        salarys = kwargs.get('salarys', '10k-20k')
        isUnifiedEntrance = kwargs.get('isUnifiedEntrance', 1)

    r1 = login(countryCode, phone)

    basicMain_html = 'https://www.lagou.com/resume/perfectresume.html?showQRCode=true'
    remark = '创建简历的初始页面'
    get_requests(url=basicMain_html, remark=remark)

    head_url = 'https://www.lagou.com/resume/saveHeadPic.json?headPicPath={}'.format(
        '/common/image/pc/default_boy_headpic2.png')
    remark = "上传头像"
    get_requests(url=head_url, remark=remark)

    if userIdentity == 2:
        # 基本信息
        basicMain_url = 'https://www.lagou.com/resume/basicMain.json'
        basicMain_header = get_code_token(basicMain_html)
        basicMain_data = {'name': name, 'birthday': birthday, 'sex': '男',
                          'email': '{}@testlagou.com'.format(phone),
                          'userIdentity': userIdentity, 'liveCity': liveCity, 'joinWorkTime': joinWorkTime}
        remark = "添加基本信息"
        r2 = form_post(url=basicMain_url, headers=basicMain_header, data=basicMain_data, remark=remark)

        # 工作经历
        workExperience_url = 'https://www.lagou.com/workExperience/save.json'
        workExperience_header = get_code_token(basicMain_html)
        workExperience_data = {"positionType": "机器学习", "positionType1": "开发|测试|运维类", "positionType2": "人工智能",
                               "skillLabels": "机器学习",
                               "department": "大数据智能中心", "companyIndustry": "电商", "companyName": "拉勾网",
                               "positionName": "机器学习", "startDate": "2012.07", "requestSource": 1,
                               "endDate": "2019.03", "workContent": "<p>哒哒哒哒哒哒多多多多多多多</p>", "isItVisible": 1}
        remark = "添加工作经历"
        r3 = form_post(url=workExperience_url, headers=workExperience_header, data=workExperience_data, remark=remark)
    else:
        # 基本信息
        basicMain_url = 'https://www.lagou.com/resume/basicMain.json'
        basicMain_header = get_code_token(basicMain_html)
        basicMain_data = {'name': name, 'birthday': birthday, 'sex': '男',
                          'email': '{}@testlagou.com'.format(phone),
                          'userIdentity': userIdentity, 'liveCity': liveCity}
        remark = "添加基本信息"
        r2 = form_post(url=basicMain_url, headers=basicMain_header, data=basicMain_data, remark=remark)

    # 教育经历
    edu_header = get_code_token(basicMain_html)
    edu_url = 'https://www.lagou.com/educationExperience/save.json'
    edu_data = {'schoolName': '清华大学', 'education': education, 'professional': '计算机科学与技术', 'startDate': startDate,
                'endDate': endDate, 'isUnifiedEntrance': isUnifiedEntrance}
    remark = "添加教育经历"
    r4 = form_post(url=edu_url, headers=edu_header, data=edu_data, remark=remark)

    # 个人名片
    personal_url = 'https://www.lagou.com/resume/personalCard.json'
    personal_header = get_code_token(basicMain_html)
    personal_data = {'myRemark': '<p>哈哈哈哈</p>', 'socialAccountJson': '[]', 'abilityLabels': '执行力'}
    remark = "添加个人名片"
    r5 = form_post(url=personal_url, headers=personal_header, data=personal_data, remark=remark)

    # 求职意向
    expextJobs_url = 'https://www.lagou.com/expectJobs/expectJobs.json'
    expectJobs_header = get_code_token(basicMain_html)
    expectJobs_data = {'city': city, 'positionName': positionName,
                       'positionNameType1': positionNameType1,
                       'positionNameType2': positionNameType2, 'salarys': salarys, 'status': '积极找工作',
                       'arrivalTime': '随时'}
    remark = "添加求职意向"
    r6 = form_post(url=expextJobs_url, headers=expectJobs_header, data=expectJobs_data, remark=remark)

    # 改善简历的头像和基本名片
    r7 = {'success': True}

    # 完善个人信息
    r8 = {'success': True}

    if userIdentity == 2:
        return [r1, r2, r3, r4, r5, r6, r7, r8]
    else:
        return [r1, r2, r4, r5, r6, r7, r8]


'''
if __name__ == '__main__':
    a = 0
    phone = 19900000  # 手机号
    countryCode = '00852'  # 区号
    userIdentity = 2  # 值只能是1学生或2非学生
    for i in range(3):
        time.sleep(1)
        p = Process(target=registe_c, args=(phone + a, countryCode, userIdentity,))
        a += 1
        p.start()
        p.join()
'''
