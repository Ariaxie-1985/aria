# coding:utf-8

# 注册C端-生成简历

import requests
import re
import random
import json
# 全局变量
User_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"

session = requests.session()

# 注册C端前提取header的token、code、cookie的JSESSIONID

html = session.get('https://passport.lagou.com/register/register.html?from=c', verify=False)
JSESSIONID = html.headers['Set-Cookie']
soup = BeautifulSoup(html.text, 'lxml')
keyWord = soup.find_all(text=re.compile("window.X_Anti_Forge_Token"))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
token_values = keyWord_value[4]
keyWord = soup.find_all(text=re.compile('window.X_Anti_Forge_Code'))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
code_values = keyWord_value[-3]

# C端注册
register_url = "https://passport.lagou.com/register/register.json"
register_data = {"isValidate" : "true", "phone" : 20000119, "phoneVerificationCode": "049281", "challenge": 111,"type": 0,"countryCode": "00852"}
register_header = {"X-Anit-Forge-Code":code_values, "X-Anit-Forge-Token":token_values}
register = session.post(url=register_url, data=register_data,headers=register_header, verify=False)


# 提取token和code
perfectresume_url = "https://www.lagou.com/resume/perfectresume.html"
perfectresume = session.get(url=perfectresume_url, verify=False)
soup = BeautifulSoup(perfectresume.text, 'lxml')
keyWord = soup.find_all(text=re.compile("window.X_Anti_Forge_Token"))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
token_values_1 = keyWord_value[4]
keyWord = soup.find_all(text=re.compile('window.X_Anti_Forge_Code'))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
code_values_1 = keyWord_value[-3]

# 简历-填写头像
saveHeadPic_url = "https://www.lagou.com/resume/saveHeadPic.json?headPicPath=/common/image/pc/default_boy_headpic2.png"
# saveHeadPic_data = {"headPicPath" : "/common/image/pc/default_boy_headpic2.png"}
saveHeadPic_header = {"X-Anit-Forge-Code":code_values_1, "X-Anit-Forge-Token":token_values_1}
basicMain = session.get(url=saveHeadPic_url, headers=saveHeadPic_header, verify=False)

# 简历-填写基本信息
basicMain_url = "https://www.lagou.com/resume/basicMain.json"
basicMain_data = {"name" : "王宸1","birthday" : "1990.07","sex" : "男","email" : "test2018@sina.com", "userIdentity" : 2, "joinWorkTime" : "2012.08", "liveCity" : "北京"}
basicMain_header = {"X-Anit-Forge-Code":code_values_1, "X-Anit-Forge-Token":token_values_1}
basicMain = session.post(url=basicMain_url, data=basicMain_data,headers=basicMain_header, verify=False)

# 提取token和code
perfectresume_url = "https://www.lagou.com/resume/perfectresume.html"
perfectresume = session.get(url=perfectresume_url, verify=False)
soup = BeautifulSoup(perfectresume.text, 'lxml')
keyWord = soup.find_all(text=re.compile("window.X_Anti_Forge_Token"))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
token_values_2 = keyWord_value[4]
keyWord = soup.find_all(text=re.compile('window.X_Anti_Forge_Code'))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
code_values_2 = keyWord_value[-3]

# 简历-填写工作经历
workExperience_url = "https://www.lagou.com/workExperience/save.json"
workExperience_data = {"positionType" : "Java", "positionType1" : "开发|测试|运维类", "positionType2" : "后端开发", "skillLabels" : "服务器端,Java,数据库","department": "技术工程部","companyIndustry" : "企业服务","companyName" : "拉勾网","positionName" : "Java","startDate" : "2012.08","endDate" : "至今","workContent" : "<p>为了APIAPPMysqlRedisMQZKHTTPMotan<br></p>","isItVisible": 1}
workExperience_header = {"X-Anit-Forge-Code":code_values_2, "X-Anit-Forge-Token":token_values_2}
workExperience = session.post(url=workExperience_url, data=workExperience_data,headers=workExperience_header, verify=False)
workExperience = workExperience.json()
resume_id = workExperience['content']['resume']['id']

# 提取token和code
perfectresume_url = "https://www.lagou.com/resume/perfectresume.html"
perfectresume = session.get(url=perfectresume_url, verify=False)
soup = BeautifulSoup(perfectresume.text, 'lxml')
keyWord = soup.find_all(text=re.compile("window.X_Anti_Forge_Token"))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
token_values_3 = keyWord_value[4]
keyWord = soup.find_all(text=re.compile('window.X_Anti_Forge_Code'))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
code_values_3 = keyWord_value[-3]

# 简历-填写教育经历
educationExperience_url = "https://www.lagou.com/educationExperience/save.json"
educationExperience_data = {"schoolName" : "北京理工大学", "education" : "本科", "professional" : "计算机科学与技术", "startDate" : 2008,"endDate" : 2012}
educationExperience_header = {"X-Anit-Forge-Code":code_values_3, "X-Anit-Forge-Token":token_values_3}
educationExperience = session.post(url=educationExperience_url, data=educationExperience_data,headers=educationExperience_header, verify=False)

# 提取token和code
perfectresume_url = "https://www.lagou.com/resume/perfectresume.html"
perfectresume = session.get(url=perfectresume_url, verify=False)
soup = BeautifulSoup(perfectresume.text, 'lxml')
keyWord = soup.find_all(text=re.compile("window.X_Anti_Forge_Token"))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
token_values_4 = keyWord_value[4]
keyWord = soup.find_all(text=re.compile('window.X_Anti_Forge_Code'))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
code_values_4 = keyWord_value[-3]

# 简历-填写个人名片
personalCard_url = "https://www.lagou.com/resume/personalCard.json"
personalCard_data = {"myRemark" : "<p>本人有6年工作经验，意向电商或高并发<br></p>","socialAccountJson" :[{"accountUrl":"https://github.com/123"}],"abilityLabels": "个人能力,团队精神,自驱动"}
personalCard_header = {"X-Anit-Forge-Code":code_values_4, "X-Anit-Forge-Token":token_values_4}
personalCard = session.post(url=personalCard_url, data=personalCard_data,headers=personalCard_header, verify=False)

# 提取token和code
perfectresume_url = "https://www.lagou.com/resume/perfectresume.html"
perfectresume = session.get(url=perfectresume_url, verify=False)
soup = BeautifulSoup(perfectresume.text, 'lxml')
keyWord = soup.find_all(text=re.compile("window.X_Anti_Forge_Token"))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
token_values_5 = keyWord_value[4]
keyWord = soup.find_all(text=re.compile('window.X_Anti_Forge_Code'))[0]
keyWord_value = re.split(r'[;\s\']\s*', keyWord)
code_values_5 = keyWord_value[-3]

# 简历-填写求职意向
personalCard_url = "https://www.lagou.com/expectJobs/expectJobs.json"
personalCard_data = {"id": resume_id,"city" : "北京","positionType" : "全职","positionName" : "Java", "positionNameType1" : "开发|测试|运维类", "positionNameType2" : "后端开发", "salarys" : "15k-20k","status" : "随便看看","arrivalTime" : "2周 -1个月"}
personalCard_header = {"X-Anit-Forge-Code":code_values_5, "X-Anit-Forge-Token":token_values_5}
personalCard = session.post(url=personalCard_url, data=personalCard_data,headers=personalCard_header, verify=False)


