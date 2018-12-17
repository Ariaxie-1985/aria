# coding:utf-8

from util import form_post,get_code_token, login

username = 20181205
password = "f71ab0f4a3fd1f5691bdb30ea6a9748c"
r = login("00852",username)


# 发布职位-拉勾渠道
refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
Position_header = get_code_token(refer_createPosition_url)
createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
createPosition_data = {"isSchoolJob": 0,"channelTypes":"LAGOU","firstType":"产品|需求|项目类","positionType":"产品经理",
                       "positionThirdType": "产品经理","positionName": "拉勾测试产品经理1","department":"用户价值部",
                       "jobNature":"全职","salaryMin": 8, "salaryMax": 15, "workYear":"不限","education":"本科",
                       "positionBrightPoint":"六险一金","positionDesc":"<p>负责运营策划的产品方案设计利用相</p>",
                       "workAddressId":466562,"labels":'[{"id":"11","name":"企业服务"},{"id":"384","name":"用户研究"}]',
                       "extraInfor":'[{"labels":[{"id":"11","name":"企业服务"},{"id":"384","name":"用户研究"}] }]',
                       "channels":108, "useEnergyCard":"false","parentExtraInfo":'{}',"recommend":"false"}
data = 'isSchoolJob=0&channelTypes=LAGOU&firstType=产品|需求|项目类&positionType=产品经理&positionThirdType=产品经理&positionName=拉勾测试产品经理2&department=用户价值部&jobNature=全职&salaryMin=15&salaryMax=20&workYear=3-5年&education=本科&positionBrightPoint=16薪&positionDesc=<p>技术水平能力高技术水平能力高技术水平能力高技术水平能力高</p>&workAddressId=191863&labels=[{"id":"382","name":"产品设计"},{"id":"385","name":"需求分析"}]&extraInfor=[{"labels":[{"id":"382","name":"产品设计"},{"id":"385","name":"需求分析"}]}]&channels=108&useEnergyCard=false&parentExtraInfo={}&recommend=false&undefined='
form_post(createPosition_url, data.encode('utf-8'),Position_header)