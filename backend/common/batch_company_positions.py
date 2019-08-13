# coding:utf-8
# @Time  : 2019-06-25 12:01
# @Author: Xiawang

'''
根据每个商圈的所有工作地址发布职位
1.连接数据库，创建游标
2.获取数据并加工
3.执行请求、输出日志
'''
import json
import random

import pymysql
from pathos.multiprocessing import ProcessingPool as newPool

from backend.common.data import provider_data, prodiver_sh_address, demo_data, provider_gz_data
from utils.util import form_post, get_code_token, login, json_post


def get_data(city):
    def connect_db():  # 闭包, 保证数据库配置的安全性
        db = pymysql.connect(
            host='10.1.200.166',
            port=3306,
            user='lagouro',
            passwd='Q12_#*s#$opIx',
            db='testing_platform',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = db.cursor()
        return db, cursor

    db, cursor = connect_db()
    db.ping(reconnect=True)
    cursor.execute('select id,biz_area from t_work_address where city = "{}" limit 200'.format(city))
    return cursor.fetchall()


def process_data(db_data):
    '''
    将有商圈的 address_id 去重放入 list 中
    :param db_data: list
    '''
    id_area_data = []
    for biz_areas in db_data:
        try:
            biz_area = json.loads(biz_areas['biz_area'])
        except:
            continue
        if not bool(biz_area) == False or biz_area == '""':
            address_id = biz_areas['id']
            id_area_data.append(int(address_id))
    return list(set(id_area_data))


def run(phone_list, address_list):
    error = 0
    success = 0
    pool = newPool()
    res_list = pool.map(post_position, phone_list, address_list)
    for index, value in enumerate(res_list):
        if 'state' not in value[0] or value[0]['state'] != 1:
            error = error + 1
            continue

        if value[0]['state'] == 1:
            success = success + 1

        if len(address_list) % 1000 == 0:
            print('发布职位完成 {} 个'.format(index + 1))
    print('~~~~~~~~~~~~~~~~~~~~~~' * 8)
    print('成功发布职位 {} 个'.format(success))
    print('失败发布职位 {} 个'.format(error))


def post_position(phone, addressId):
    '''
    批量发布职位
    :param sum: 发布职位个数
    :return: 发布职位的请求

    '''
    login('00853', phone)
    count = 0
    posit_list = [('开发|测试|运维类', '后端开发', 'Java', '高级Java'), ('开发|测试|运维类', '移动前端开发', 'IOS', '高级IOS'),
                  ('开发|测试|运维类', '移动前端开发', 'Android', '高级Android')]
    # for i in range(3):
    posit = random.randint(0, 2)
    try:
        refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
        Position_header = get_code_token(refer_createPosition_url)
        createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
        createPosition_data = {**{'isSchoolJob': '1',
                                  'channelTypes': 'LAGOU',
                                  'department': '用户价值部',
                                  'jobNature': '全职',
                                  'salaryMin': '10',
                                  'salaryMax': '12',
                                  'education': '本科',
                                  'workAddressId': addressId,
                                  'positionBrightPoint': '20薪',
                                  'workYear': '应届毕业生',
                                  'channels': '108',
                                  'recommend': True,
                                  'extraInfor': '[{"labels":[{"id":"1","name":"电商"}]}]',
                                  'positionDesc': '<p>脑洞大，创意达，能吃苦。脑洞大，创意达，能吃苦。脑洞大，创意达，能吃苦。脑洞大</p>',
                                  'labels': '[{"id":"1","name":"电商"}]',
                                  'parentExtraInfo': '{}',
                                  "useEnergyCard": False},
                               "firstType": posit_list[posit][0],
                               "positionType": posit_list[posit][1],
                               "positionThirdType": posit_list[posit][2],
                               "positionName": "校招需求" + posit_list[posit][3]}
    except:
        pass

    remark = "批量发布职位成功"
    r = form_post(
        url=createPosition_url,
        data=createPosition_data,
        headers=Position_header,
        remark=remark)
    try:
        if r['state'] == 1:
            count += 1
    except:
        pass

    return {'count': count}


def setup_data(phone):
    phone_list = []
    # url_b = 'http://10.1.200.141:9004/entry/registration'
    url_b = 'http://127.0.0.1:9004/entry/registration'
    data_b = {
        "countryCode": "00852",
        "phone": phone,
        "type": 'b'
    }
    r1 = json_post(url=url_b, headers={}, data=data_b, remark='注册B端')
    if r1['state'] == 1:
        url = 'http://127.0.0.1:9004/jianzhao/company/registration'
        data = {
            "countryCode": "00852",
            "phone": phone
        }
        r = json_post(url=url, headers={}, data=data, remark='创建公司')
        if r.get('state', 0) == 1:
            phone_list.append(phone)
    return phone_list


def run_setup():
    phone_list = [x + 1 for x in range(60000000, 90000000)]
    pool = newPool()
    res_list = pool.map(setup_data, phone_list)
    return res_list


postype = [{'firstType': '开发|测试|运维类', 'positionType': '人工智能', 'positionThirdType': '机器学习', 'positionName': '机器学习'},
           {'firstType': '产品|需求|项目类', 'positionType': '产品经理', 'positionThirdType': '产品经理', 'positionName': '产品经理'},
           {'firstType': '设计类', 'positionType': '交互', 'positionThirdType': '交互设计师', 'positionName': 'UI设计'},
           {'firstType': '运营|编辑|客服类', 'positionType': '运营', 'positionThirdType': '用户运营', 'positionName': '用户运营'},
           {'firstType': '市场|商务类', 'positionType': '市场|营销', 'positionThirdType': '市场营销', 'positionName': '市场营销'},
           {'firstType': '销售类', 'positionType': '销售', 'positionThirdType': '销售经理', 'positionName': '销售经理'},
           {'firstType': '综合职能|高级管理', 'positionType': '人力资源', 'positionThirdType': 'HRBP', 'positionName': 'HRBP'},
           {'firstType': '金融类', 'positionType': '互联网金融', 'positionThirdType': '金融产品经理', 'positionName': '金融产品经理'},
           {'firstType': '非互联网职位', 'positionType': '生产|加工|制造', 'positionThirdType': '技工', 'positionName': '模具工'}]


def post_position_city(sum, addressId):
    '''
    批量发布职位
    :param sum: 发布职位个数
    :return: 发布职位的请求

    '''
    reslist = []
    login('00852', 20181205)
    for i in range(sum):
        position_info = postype[random.randint(0, 8)]
        firstType = position_info['firstType']
        positionType = position_info['positionType']
        positionThirdType = position_info['positionThirdType']
        positionName = position_info['positionName']
        refer_createPosition_url = "https://easy.lagou.com/position/multiChannel/createPosition.htm"
        Position_header = get_code_token(refer_createPosition_url)
        createPosition_url = "https://easy.lagou.com/parentPosition/multiChannel/create.json"
        createPosition_data = {**{'isSchoolJob': '1',
                                  'channelTypes': 'LAGOU',
                                  'department': '111',
                                  'jobNature': '全职',
                                  'salaryMin': '11',
                                  'salaryMax': '12',
                                  'education': '不限',
                                  'workAddressId': addressId,
                                  'positionBrightPoint': '11111',
                                  'workYear': '应届毕业生',
                                  'channels': '108',
                                  'recommend': True,
                                  'extraInfor': '[{"labels":[{"id":"1","name":"电商"}]}]',
                                  'positionDesc': '<p>111111111111111111111111111111111111111111111</p>',
                                  'labels': '[{"id":"1","name":"电商"}]',
                                  'parentExtraInfo': '{}',
                                  "useEnergyCard": False},
                               "firstType": firstType,
                               "positionType": positionType,
                               "positionThirdType": positionThirdType,
                               "positionName": positionName + str(random.randint(10, 110))}

        remark = "批量发布职位" + str(sum) + "个成功"
        r = form_post(
            url=createPosition_url,
            data=createPosition_data,
            headers=Position_header,
            remark=remark)
        reslist.append(r)
    return reslist


if __name__ == '__main__':
    # db_data = get_data('成都')
    # print(db_data)
    # phone_list = run_setup()
    # sum_list = [i for i in range(100)]
    # print(sum_list)
    # address_list = process_data(db_data)
    # print(len(address_list))
    # pool = newPool()

    # b_phone_list = pool.map(post_position_city, sum_list, address_list)

    # run(b_phone_list, address_list)
    # setup_data(18900208)
    # data = provider_gz_data()
    data = [{'phone': '20033290', 'companyId': 147882, 'id': 747626, 'userId': 100022939}, {'phone': '20033291', 'companyId': 147883, 'id': 747627, 'userId': 100022940}, {'phone': '20033292', 'companyId': 147884, 'id': 747628, 'userId': 100022941}, {'phone': '20033293', 'companyId': 147885, 'id': 747629, 'userId': 100022942}, {'phone': '20033294', 'companyId': 147886, 'id': 747630, 'userId': 100022943}, {'phone': '20033295', 'companyId': 147887, 'id': 747631, 'userId': 100022944}, {'phone': '20033297', 'companyId': 147889, 'id': 747632, 'userId': 100022946}, {'phone': '20033298', 'companyId': 147890, 'id': 747633, 'userId': 100022947}, {'phone': '20033299', 'companyId': 147891, 'id': 747634, 'userId': 100022948}, {'phone': '20033300', 'companyId': 147892, 'id': 747635, 'userId': 100022949}, {'phone': '20033301', 'companyId': 147893, 'id': 747636, 'userId': 100022950}, {'phone': '20033302', 'companyId': 147894, 'id': 747637, 'userId': 100022951}, {'phone': '20033303', 'companyId': 147895, 'id': 747638, 'userId': 100022952}, {'phone': '20033304', 'companyId': 147896, 'id': 747639, 'userId': 100022953}, {'phone': '20033305', 'companyId': 147897, 'id': 747640, 'userId': 100022954}, {'phone': '20033306', 'companyId': 147898, 'id': 747641, 'userId': 100022955}, {'phone': '20033308', 'companyId': 147900, 'id': 747642, 'userId': 100022957}, {'phone': '20033309', 'companyId': 147901, 'id': 747643, 'userId': 100022958}, {'phone': '20033310', 'companyId': 147902, 'id': 747644, 'userId': 100022959}, {'phone': '20033311', 'companyId': 147903, 'id': 747645, 'userId': 100022960}, {'phone': '20033312', 'companyId': 147904, 'id': 747646, 'userId': 100022961}, {'phone': '20033313', 'companyId': 147905, 'id': 747647, 'userId': 100022962}, {'phone': '20033314', 'companyId': 147906, 'id': 747648, 'userId': 100022963}, {'phone': '20033315', 'companyId': 147907, 'id': 747649, 'userId': 100022964}, {'phone': '20033316', 'companyId': 147908, 'id': 747650, 'userId': 100022965}, {'phone': '20033317', 'companyId': 147909, 'id': 747651, 'userId': 100022966}, {'phone': '20033318', 'companyId': 147910, 'id': 747652, 'userId': 100022967}, {'phone': '20033319', 'companyId': 147911, 'id': 747653, 'userId': 100022968}, {'phone': '20033320', 'companyId': 147912, 'id': 747654, 'userId': 100022969}, {'phone': '20033321', 'companyId': 147913, 'id': 747655, 'userId': 100022970}, {'phone': '20033322', 'companyId': 147914, 'id': 747656, 'userId': 100022971}, {'phone': '20033323', 'companyId': 147915, 'id': 747657, 'userId': 100022972}, {'phone': '20033324', 'companyId': 147916, 'id': 747658, 'userId': 100022973}, {'phone': '20033325', 'companyId': 147917, 'id': 747659, 'userId': 100022974}, {'phone': '20033326', 'companyId': 147918, 'id': 747660, 'userId': 100022975}, {'phone': '20033327', 'companyId': 147919, 'id': 747661, 'userId': 100022976}, {'phone': '20033328', 'companyId': 147920, 'id': 747662, 'userId': 100022977}, {'phone': '20033329', 'companyId': 147921, 'id': 747663, 'userId': 100022978}, {'phone': '20033330', 'companyId': 147922, 'id': 747664, 'userId': 100022979}, {'phone': '20033331', 'companyId': 147923, 'id': 747665, 'userId': 100022980}, {'phone': '20033332', 'companyId': 147924, 'id': 747666, 'userId': 100022981}, {'phone': '20033333', 'companyId': 147925, 'id': 747667, 'userId': 100022982}, {'phone': '20033334', 'companyId': 147926, 'id': 747668, 'userId': 100022983}, {'phone': '20033335', 'companyId': 147927, 'id': 747669, 'userId': 100022984}, {'phone': '20033336', 'companyId': 147928, 'id': 747670, 'userId': 100022985}, {'phone': '20033337', 'companyId': 147929, 'id': 747671, 'userId': 100022986}, {'phone': '20033338', 'companyId': 147930, 'id': 747672, 'userId': 100022987}, {'phone': '20033339', 'companyId': 147931, 'id': 747673, 'userId': 100022988}, {'phone': '20033340', 'companyId': 147932, 'id': 747674, 'userId': 100022989}, {'phone': '20033341', 'companyId': 147933, 'id': 747675, 'userId': 100022990}, {'phone': '20033342', 'companyId': 147934, 'id': 747676, 'userId': 100022991}, {'phone': '20033343', 'companyId': 147935, 'id': 747677, 'userId': 100022992}, {'phone': '20033344', 'companyId': 147936, 'id': 747678, 'userId': 100022993}, {'phone': '20033346', 'companyId': 147938, 'id': 747679, 'userId': 100022995}, {'phone': '20033347', 'companyId': 147939, 'id': 747680, 'userId': 100022996}, {'phone': '20033348', 'companyId': 147940, 'id': 747681, 'userId': 100022997}, {'phone': '20033349', 'companyId': 147941, 'id': 747682, 'userId': 100022998}, {'phone': '20033350', 'companyId': 147942, 'id': 747683, 'userId': 100022999}, {'phone': '20033351', 'companyId': 147943, 'id': 747684, 'userId': 100023000}, {'phone': '20033352', 'companyId': 147944, 'id': 747685, 'userId': 100023001}, {'phone': '20033353', 'companyId': 147945, 'id': 747686, 'userId': 100023002}, {'phone': '20033354', 'companyId': 147946, 'id': 747687, 'userId': 100023003}, {'phone': '20033355', 'companyId': 147947, 'id': 747688, 'userId': 100023004}, {'phone': '20033356', 'companyId': 147948, 'id': 747689, 'userId': 100023005}, {'phone': '20033357', 'companyId': 147949, 'id': 747690, 'userId': 100023006}, {'phone': '20033358', 'companyId': 147950, 'id': 747691, 'userId': 100023007}, {'phone': '20033359', 'companyId': 147951, 'id': 747692, 'userId': 100023008}, {'phone': '20033360', 'companyId': 147952, 'id': 747693, 'userId': 100023009}, {'phone': '20033361', 'companyId': 147953, 'id': 747694, 'userId': 100023010}, {'phone': '20033362', 'companyId': 147954, 'id': 747695, 'userId': 100023011}, {'phone': '20033363', 'companyId': 147955, 'id': 747696, 'userId': 100023012}, {'phone': '20033364', 'companyId': 147956, 'id': 747697, 'userId': 100023013}, {'phone': '20033365', 'companyId': 147957, 'id': 747698, 'userId': 100023014}, {'phone': '20033366', 'companyId': 147958, 'id': 747699, 'userId': 100023015}, {'phone': '20033367', 'companyId': 147959, 'id': 747700, 'userId': 100023016}, {'phone': '20033368', 'companyId': 147960, 'id': 747701, 'userId': 100023017}, {'phone': '20033369', 'companyId': 147961, 'id': 747702, 'userId': 100023018}, {'phone': '20033370', 'companyId': 147962, 'id': 747703, 'userId': 100023019}, {'phone': '20033371', 'companyId': 147963, 'id': 747704, 'userId': 100023020}, {'phone': '20033372', 'companyId': 147964, 'id': 747705, 'userId': 100023021}, {'phone': '20033373', 'companyId': 147965, 'id': 747706, 'userId': 100023022}, {'phone': '20033374', 'companyId': 147966, 'id': 747707, 'userId': 100023023}, {'phone': '20033375', 'companyId': 147967, 'id': 747708, 'userId': 100023024}, {'phone': '20033376', 'companyId': 147968, 'id': 747709, 'userId': 100023025}, {'phone': '20033377', 'companyId': 147969, 'id': 747710, 'userId': 100023026}, {'phone': '20033378', 'companyId': 147970, 'id': 747711, 'userId': 100023027}, {'phone': '20033379', 'companyId': 147971, 'id': 747712, 'userId': 100023028}, {'phone': '20033380', 'companyId': 147972, 'id': 747713, 'userId': 100023029}, {'phone': '20033381', 'companyId': 147973, 'id': 747714, 'userId': 100023030}, {'phone': '20033382', 'companyId': 147974, 'id': 747715, 'userId': 100023031}, {'phone': '20033383', 'companyId': 147975, 'id': 747716, 'userId': 100023032}, {'phone': '20033384', 'companyId': 147976, 'id': 747717, 'userId': 100023033}, {'phone': '20033385', 'companyId': 147977, 'id': 747718, 'userId': 100023034}, {'phone': '20033386', 'companyId': 147978, 'id': 747719, 'userId': 100023035}, {'phone': '20033387', 'companyId': 147979, 'id': 747720, 'userId': 100023036}, {'phone': '20033388', 'companyId': 147980, 'id': 747721, 'userId': 100023037}, {'phone': '20033389', 'companyId': 147981, 'id': 747722, 'userId': 100023038}, {'phone': '20033390', 'companyId': 147982, 'id': 747723, 'userId': 100023039}, {'phone': '20033391', 'companyId': 147983, 'id': 747724, 'userId': 100023040}, {'phone': '20033392', 'companyId': 147984, 'id': 747725, 'userId': 100023041}, {'phone': '20033393', 'companyId': 147985, 'id': 747726, 'userId': 100023042}, {'phone': '20033394', 'companyId': 147986, 'id': 747727, 'userId': 100023043}, {'phone': '20033395', 'companyId': 147987, 'id': 747728, 'userId': 100023044}, {'phone': '20033396', 'companyId': 147988, 'id': 747729, 'userId': 100023045}, {'phone': '20033397', 'companyId': 147989, 'id': 747730, 'userId': 100023046}, {'phone': '20033398', 'companyId': 147990, 'id': 747731, 'userId': 100023047}, {'phone': '20033399', 'companyId': 147991, 'id': 747732, 'userId': 100023048}, {'phone': '20033400', 'companyId': 147992, 'id': 747733, 'userId': 100023049}, {'phone': '20033401', 'companyId': 147993, 'id': 747734, 'userId': 100023050}, {'phone': '20033402', 'companyId': 147994, 'id': 747735, 'userId': 100023051}, {'phone': '20033403', 'companyId': 147995, 'id': 747736, 'userId': 100023052}, {'phone': '20033404', 'companyId': 147996, 'id': 747737, 'userId': 100023053}, {'phone': '20033405', 'companyId': 147997, 'id': 747738, 'userId': 100023054}, {'phone': '20033406', 'companyId': 147998, 'id': 747739, 'userId': 100023055}, {'phone': '20033407', 'companyId': 147999, 'id': 747740, 'userId': 100023056}, {'phone': '20033408', 'companyId': 148000, 'id': 747741, 'userId': 100023057}, {'phone': '20033409', 'companyId': 148001, 'id': 747742, 'userId': 100023058}]
    for da in data:
        r = post_position(da['phone'], da['id'])
        da.update(r)
    print(data)
