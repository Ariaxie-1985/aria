# coding:utf-8
from api_script.util import get_code_token, form_post, get_header, login, get
import re


# B端登录
username = 20000215
r = login("00852",username)

# B端申请认证公司
referer_com_url = "https://easy.lagou.com/bstatus/auth/index.htm"
headers = get_header(referer_com_url)
com_step1_url = "https://hr.lagou.com/corpCenter/company/auth/step1.html"
auth_file_url = "https://hr.lagou.com/corpCenter/company/auth/file.json"
auth_file_data = {"fileUrl":"i/audio1/M00/01/C5/CgHIk1wQzSaAcR09AAqex8SeJls235.JPG"}
auth_file_header = get_code_token(com_step1_url)
form_post(url=auth_file_url, data=auth_file_data, headers=auth_file_header)


com_step2_url = "https://hr.lagou.com/corpCenter/company/auth/step2.html"
com_html = get(com_step2_url)
comAuthId = re.findall('userId: "(.*?)"', com_html.text, re.S)[0]
completeInfo_url = "https://hr.lagou.com/corpCenter/company/auth/completeInfo.json"
completeInfo_data = {"id":comAuthId, "logo":"i/audio1/M00/01/C6/CgHIk1wSFMeAeIoaAAB1mvl2DME518.JPG", "officialWebsite":"www.lagou.com","fullIntro":"愿天下没有难找的工作","shortIntro":"一天就能找到满意的工作","detailAddress":"海置创投大厦4层","provinceId":1,"cityId":5,"districtId":2005,"businessArea":"苏州街","companyLng":"116.307747","companyLat":"39.982128"}
completeInfo_header = get_code_token(com_step2_url)
form_post(url=completeInfo_url, data=completeInfo_data, headers=completeInfo_header)

