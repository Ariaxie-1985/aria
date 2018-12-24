# coding:utf-8

from api_script.util import form_post,get_code_token, login
import random,time

# 批量发布职位-拉勾渠道
username = 20181205
r = login("00852",username)
j = 0
postype = [{'firstType':'开发|测试|运维类','positionType':'人工智能','positionThirdType':'机器学习','positionName':'机器学习'+str(j)},
           {'firstType':'产品|需求|项目类','positionType':'产品经理','positionThirdType':'产品经理','positionName':'产品经理'+str(j)},
           {'firstType':'设计类','positionType':'交互','positionThirdType':'交互设计师','positionName':'UI设计'+str(j)},
           {'firstType':'运营|编辑|客服类','positionType':'运营','positionThirdType':'用户运营','positionName':'用户运营'+str(j)},
           {'firstType':'市场|商务类','positionType':'市场|营销','positionThirdType':'市场营销','positionName':'市场营销'+str(j)},
           {'firstType':'销售类','positionType':'销售','positionThirdType':'销售经理','positionName':'销售经理'+str(j)},
           {'firstType':'综合职能|高级管理','positionType':'人力资源','positionThirdType':'HRBP','positionName':'HRBP'+str(j)},
           {'firstType':'金融类','positionType':'互联网金融','positionThirdType':'金融产品经理','positionName':'金融产品经理'+str(j)},
           {'firstType':'非互联网职位','positionType':'生产|加工|制造','positionThirdType':'技工','positionName':'模具工'+str(j)}]

# 发布职位个数
sum = 2

for i in range(sum):
    time.sleep(1)
    a = random.randint(0,7)
    j = i
    postype_t = postype[a]
    refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
    Position_header = get_code_token(refer_createPosition_url)
    createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
    createPosition_data = {**{'isSchoolJob':'1','channelTypes':'LAGOU','department':'111','jobNature':'全职',
        'salaryMin':'11','salaryMax':'12','education':'不限','positionBrightPoint':'11111',
        'positionDesc':'<p>111111111111111111111111111111111111111111111</p>','workAddressId':'191880',
        'labels':'[{"id":"1","name":"电商"}]','extraInfor':'[{"labels":[{"id":"1","name":"电商"}]}]',
        'channels':'108','useEnergyCard':'false','recommend':'false',"useEnergyCard":"false"}, **postype_t}
    form_post(createPosition_url, createPosition_data,Position_header)
