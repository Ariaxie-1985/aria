# coding:utf-8

from util import form_post,get_code_token, login

username = 20181205
r = login("00852",username)


# 发布职位-拉勾渠道
refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
Position_header = get_code_token(refer_createPosition_url)
createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
createPosition_data = {'isSchoolJob':'1','channelTypes':'LAGOU','firstType':'开发|测试|运维类','positionType':'后端开发',
        'positionThirdType':'Java','positionName':'python后端开发2','department':'111','jobNature':'全职',
        'salaryMin':'11','salaryMax':'12','education':'不限','positionBrightPoint':'11111',
        'positionDesc':'<p>111111111111111111111111111111111111111111111</p>','workAddressId':'191880',
        'labels':'[{"id":"1","name":"电商"}]','extraInfor':'[{"labels":[{"id":"1","name":"电商"}]}]',
        'channels':'108','useEnergyCard':'false','recommend':'false',"useEnergyCard":"false"}
form_post(createPosition_url, createPosition_data,Position_header)