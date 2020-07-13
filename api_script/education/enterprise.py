from utils.util import login_password, get_requests, json_post


def get_lagou_user_id_study():
    get_staff_study_state = 'https://gate.lagou.com/v1/neirong/edu/enterprise/getStaffsByStudyState?studyState=STUDY&phone=&name=&pageNo=1&pageSize=20&enterpriseId=2'
    response = get_requests(url=get_staff_study_state, headers={'x-l-req-header': '{deviceType:1}'}, rd='马坤鹏')
    return response


def get_lagou_user_id_remove():
    get_staff_study_state = ' https://gate.lagou.com/v1/neirong/edu/enterprise/getStaffsByStudyState?studyState=REMOVE&phone=&name=&pageNo=1&pageSize=20&enterpriseId=2'
    response = get_requests(url=get_staff_study_state, headers={'x-l-req-header': '{deviceType:1}'}, rd='马坤鹏')
    return response


def del_user(staff_id):
    del_user_url = f'https://gate.lagou.com/v1/neirong/edu/enterprise/delStaff?staffId={staff_id}&enterpriseId=2'
    response = get_requests(url=del_user_url, headers={'x-l-req-header': '{deviceType:1}'}, rd='马坤鹏')
    return response


def remove_user(staff_id):
    remove_user_url = f'https://gate.lagou.com/v1/neirong/edu/enterprise/addOrRomveStaff?staffId={staff_id}&studyState=REMOVE'
    response = get_requests(url=remove_user_url, headers={'x-l-req-header': '{deviceType:1}'}, rd='马坤鹏')
    return response


def add_user(user_name, code, phone, email, position, enterprise_id, is_show):
    add_user_url = 'https://gate.lagou.com/v1/neirong/edu/enterprise/addStaffs'
    data = [{"staffName": user_name, "code": code, "phone": phone,
             "email": email, "position": position, "enterpriseId": enterprise_id,
             "isShow": is_show}]
    header = {'x-l-req-header': '{deviceType:1}'}
    remark = "添加员工成功"
    response = json_post(url=add_user_url, data=data, headers=header, remark=remark, rd='马坤鹏')
    return response


def search_staff(enterprise_id):
    search_referer_url = 'https://kaiwu.lagou.com/enterprise/index.html'
    get_requests(search_referer_url)
    search_url =f'https://gate.lagou.com/v1/neirong/edu/enterprise/getStaffsByStudyState?studyState=STUDY&phone=&name=自动化测试&pageNo=1&pageSize=20&{enterprise_id}'
    response = get_requests(url=search_url, headers={'x-l-req-header': '{deviceType:1}'}, rd='马坤鹏')
    return response

def search_staff_after_remove(enterprise_id):
    search_referer_url = 'https://kaiwu.lagou.com/enterprise/index.html'
    get_requests(search_referer_url)
    search_url = 'https://gate.lagou.com/v1/neirong/edu/enterprise/getStaffsByStudyState?studyState=REMOVE&phone=&name=&pageNo=1&pageSize=20&enterpriseId=2&t=1594290060305'
    response = get_requests(url=search_url, headers={'x-l-req-header': '{deviceType:1}'}, rd='马坤鹏')
    return response


def enterprise_login():
    login_password('13252477137', '990eb670f81e82f546cfaaae1587279a')
    url = 'https://passport.lagou.com/ajaxLogin/frameGrant.html?fl=2&service=https%3A%2F%2Fkaiwu.lagou.com%2Fenterprise%2Findex.html%23%2Findex&osc=PASSPORT._pscb(1)&ofc=PASSPORT._pfcb(1)&pfurl=https%3A%2F%2Fkaiwu.lagou.com%2Fenterprise%2Findex.html%23%2Findex'
    get_requests(url, headers={'referer': 'https://kaiwu.lagou.com/enterprise/index.html'}, rd='马坤鹏')
    search_referer_url = 'https://kaiwu.lagou.com/enterprise/index.html'
    get_requests(search_referer_url)
