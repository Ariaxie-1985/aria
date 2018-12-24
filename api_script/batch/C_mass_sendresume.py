# coding:utf-8
from api_script.C_sendResume import get_resumeId
from util import get_code_token, form_post, get, get_header

'''
批量对同一职位发送大量简历
'''
a = 0
phone = 20160132
countryCode = '00852'
positionId = 5375318
for i in range(10):
	a += 1
	c_register_html = 'https://passport.lagou.com/register/register.html?from=c'
	register_url = 'https://passport.lagou.com/register/register.json'
	register_data = {'isValidate':'true','phone':phone+a,'phoneVerificationCode':'049281', 'challenge':111,'type':0,'countryCode':countryCode}
	register_header = get_code_token(c_register_html)
	form_post(url=register_url,headers=register_header,data=register_data)


	basicMain_html = 'https://www.lagou.com/resume/perfectresume.html?showQRCode=true'
	head_url = 'https://www.lagou.com/resume/saveHeadPic.json?headPicPath=%2Fcommon%2Fimage%2Fpc%2Fdefault_boy_headpic2.png'
	get(url=head_url)


	'''
	基本信息
	'''
	basicMain_url = 'https://www.lagou.com/resume/basicMain.json'
	basicMain_header = get_code_token(basicMain_html)
	basicMain_data = {'name':'zyq'+str(a),'birthday':'1990.10','sex':'男','email':'940238856@qq.com','userIdentity':2,'liveCity':'北京'}
	form_post(url=basicMain_url,headers=basicMain_header,data=basicMain_data)

	'''
	工作经历
	'''
	workExperience_url = 'https://www.lagou.com/workExperience/save.json'
	workExperience_header = get_code_token(basicMain_html)
	workExperience_data = {"positionType":"Python","positionType1":"开发|测试|运维类","positionType2":"后端开发","skillLabels":"Python",
	                  "department":"用户价值部","companyIndustry":"电商","companyName":"拉勾网","positionName":"Python","startDate":"2012.07",
	                  "endDate":"至今","workContent":"<p>哒哒哒哒哒哒多多多多多多多</p>","isItVisible":1}
	form_post(url=basicMain_url, headers=basicMain_header, data=basicMain_data)

	'''
	教育经历
	'''
	edu_header = get_code_token(basicMain_html)
	edu_url = 'https://www.lagou.com/educationExperience/save.json'
	edu_data = {'schoolName':'清华大学','education':'本科','professional':'计算机科学与技术','startDate':'2008','endDate':'2012'}
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
	expectJobs_data = {'city':'北京','positionType':'全职','positionName':'python后端开发','positionNameType1':'开发|测试|运维类','positionNameType2':'后端开发','salarys':'11k-12k','status':'随便看看','arrivalTime':'随时'}
	form_post(url=expextJobs_url,headers=expectJobs_header,data=expectJobs_data)


	'''
	0:附件简历，1：在线简历
	'''
	resumeId = get_resumeId(0)
	url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
	get_header(url)
	sendResume_html = 'https://www.lagou.com/jobs/' + str(positionId) + '.html'
	sendResume_url = 'https://www.lagou.com/mycenterDelay/deliverResumeBeforce.json'
	sendResume_header = get_code_token(sendResume_html)
	sendResume_data = {'positionId': positionId, 'type': 1, 'resumeId': resumeId, 'force': 'true'}
	r = form_post(url=sendResume_url, headers=sendResume_header, data=sendResume_data)



