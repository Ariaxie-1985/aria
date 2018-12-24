# coding:utf-8

from api_script.util import get_code_token, form_post, get
'''
注册
'''
phone = 12140008
countryCode = '00853'

c_register_html = 'https://passport.lagou.com/register/register.html?from=c'
register_url = 'https://passport.lagou.com/register/register.json'
register_data = {'isValidate':'true','phone':phone,'phoneVerificationCode':'049281', 'challenge':111,'type':0,'countryCode':countryCode}
register_header = get_code_token(c_register_html)
form_post(url=register_url,headers=register_header,data=register_data)


basicMain_html = 'https://www.lagou.com/resume/perfectresume.html?showQRCode=true'
head_url = 'https://www.lagou.com/resume/saveHeadPic.json?headPicPath=%2Fcommon%2Fimage%2Fpc%2Fdefault_boy_headpic2.png'
# head_header = get_code_token(basicMain_html)
get(url=head_url)


'''
基本信息
'''	
basicMain_url = 'https://www.lagou.com/resume/basicMain.json'
basicMain_header = get_code_token(basicMain_html)
basicMain_data = {'name':'zyq','birthday':'1995.10','sex':'男','email':'940238856@qq.com','userIdentity':1,'liveCity':'北京'}
form_post(url=basicMain_url,headers=basicMain_header,data=basicMain_data)
'''
教育经历
'''
edu_header = get_code_token(basicMain_html)
edu_url = 'https://www.lagou.com/educationExperience/save.json'
edu_data = {'schoolName':'清华大学','education':'本科','professional':'计算机科学与技术','startDate':'2009','endDate':'2013'}
form_post(url=edu_url,headers=edu_header,data=edu_data)

'''
个人名片
'''
personal_url = 'https://www.lagou.com/resume/personalCard.json'
personal_header = get_code_token(basicMain_html)
personal_data = {'myRemark':'<p>哈哈哈哈</p>','socialAccountJson':'[]','abilityLabels':'执行力'}
form_post(url=personal_url,headers=personal_header,data=personal_data)


expextJobs_url = 'https://www.lagou.com/expectJobs/expectJobs.json'
expectJobs_header = get_code_token(basicMain_html)
expectJobs_data = {'id':3791864,'city':'北京','positionType':'全职','positionName':'Java','positionNameType1':'开发|测试|运维类','positionNameType2':'后端开发','salarys':'15k-20k','status':'随便看看','arrivalTime':'随时'}
form_post(url=expextJobs_url,headers=expectJobs_header,data=expectJobs_data)

