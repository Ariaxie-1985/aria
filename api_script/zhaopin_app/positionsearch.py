# coding:utf-8
# @Time  : 2019-03-07 10:55
# @Author: Xiawang
import json

from utils.util import get_app_header, json_post, get_requests

host = "http://10.1.200.220:32040"
headers = get_app_header(100014641)


def searchPosition(keyword, sort):
    '''

    :return:
    '''
    url = host + "/positionsearch/searchPosition"
    data = {
        # "businessZone": businessZone,
        # "city": city,
        # "companySizes": [companySizes],
        # "district": district,
        # "education": [
        #     education
        # ],
        # "financeStage": [
        #     financeStage
        # ],
        # "hiTag": hiTag,
        # "industryField": [
        #     industryField
        # ],
        # "isAd": isAd,
        # "jobNature": [
        #     jobNature
        # ],
        "keyword": keyword,
        # "keywordSource": 0,
        # "lastShowCompanyId": "",
        # "longitudeAndLatitude": "",
        # "nearByKilometers": nearByKilometers,
        # "pageNo": 1,
        # "pageSize": 20,
        # "refreshHiTagList": False,
        # "salaryLower": 10000,
        # "salaryUpper": 20000,
        # "shieldDeliveyCompany": False,
        # "showId": "",
        "sort": sort,
        # "subwayLineName": "",
        # "subwayStation": subwayStation,
        # "workExperience": [
        #     workExperience
        # ]
    }
    c_headers = {"X-L-REQ-HEADER": {"deviceType": "150", "appVersion": "70800", "reqVersion": "70800"}}
    c_headers["X-L-REQ-HEADER"] = json.dumps(c_headers["X-L-REQ-HEADER"])
    header = dict(headers)
    header.update(c_headers)
    remark = "搜索职位或公司"
    return json_post(url=url, data=data, headers=header, remark=remark)


def hr_getHRCard(id, tagType):
    '''
    :param id: str, hrId 批量id查询,一次最多查询20条
    :param tagType: str, hr标签类型，不赋值表示不要标签，0表示所有标签，1表示简历处理标签，2表示聊天意愿标签
    :return:
    '''
    url = host + "/buser/hr/getHRCard?id={}&tagType={}".format(id, tagType)
    remark = "HR信息获取"
    return get_requests(url=url, headers=headers, remark=remark)


def getPromotionPositions(keyword, city, lastShowCompanyId):
    '''

    :param keyword: str, 关键词
    :param city: str, 城市
    :param lastShowCompanyId: int, 曝光活动 二号广告位上次已展示过的公司id，无则不传
    :return:
    '''
    if not (lastShowCompanyId == None):
        url = host + "/promotion/getPromotionPositions?keyword={}&city={}&lastShowCompanyId={}".format(keyword, city,
                                                                                                       lastShowCompanyId)
    else:
        url = host + "/promotion/getPromotionPositions?keyword={}&city={}".format(keyword, city)
    remark = "全民升职季"
    return get_requests(url=url, headers=headers, remark=remark)
