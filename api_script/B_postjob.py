# coding:utf-8

from util import form_post,get_code_token

username = "0085220181205"
password = "f71ab0f4a3fd1f5691bdb30ea6a9748c"
login_html = 'https://www.lagou.com/frontLogin.do'
login_url = 'https://passport.lagou.com/login/login.json'
login_data = {'isValidate': 'true', 'username': username, "password":password}
login_header = get_code_token(login_html)
form_post(url=login_url, data=login_data, headers=login_header)


# 发布职位-拉勾渠道
refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
Position_header = get_code_token(refer_createPosition_url)
createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
createPosition_data = {"isSchoolJob": 0,"channelTypes":"LAGOU","firstType":"产品|需求|项目类","positionType":"产品经理",
                       "positionThirdType": "产品经理","positionName": "拉勾测试产品经理1","department":"用户价值部", "jobNature":"全职",
                       "salaryMin": 8, "salaryMax": 15, "workYear":"不限","education":"本科","positionBrightPoint":"六险一金",
                       "positionDesc":"负责运营策划的产品方案设计利用相","workAddressId":466562,
                       "labels":[{"id":"11","name":"企业服务"},{"id":"384","name":"用户研究"}],"extraInfor":[{"labels":[{"id":"11","name":"企业服务"},{"id":"384","name":"用户研究"}]}],
                       "channels":108, "useEnergyCard":"false","parentExtraInfo":{},"recommend":"false"}
form_post(createPosition_url, createPosition_data,Position_header)