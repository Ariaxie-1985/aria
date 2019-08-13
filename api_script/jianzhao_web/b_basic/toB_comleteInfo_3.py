# coding:utf-8
# @Author: Xiawang
import time

from utils.util import get_code_token, form_post, get_requests, login, get_header
import re


# B端申请认证公司
def company_auth():
    # com_header = get_header("https://easy.lagou.com/dashboard/index.htm?from=c_index")headers=com_header
    get_requests("https://easy.lagou.com/bstatus/auth/index.htm")
    com_step1_url = "https://hr.lagou.com/corpCenter/company/auth/step1.html"
    auth_file_url = "https://hr.lagou.com/corpCenter/company/auth/file.json"
    auth_file_data = {"fileUrl": "i/audio1/M00/01/C5/CgHIk1wQzSaAcR09AAqex8SeJls235.JPG"}
    auth_file_header = get_code_token(com_step1_url)
    remark = "上传营业执照"
    return form_post(url=auth_file_url, data=auth_file_data, headers=auth_file_header, remark=remark)


def completeInfo(**kwargs):
    if kwargs.get('detailAddress', None) == None:
        kwargs = {}
    detailAddress = kwargs.get('detailAddress', '州维多利广场')
    provinceId = kwargs.get('provinceId', 548)
    cityId = kwargs.get('cityId', 763)
    districtId = kwargs.get('districtId', 2048)
    businessArea = kwargs.get('businessArea', "天河城,沙河,体育中心")
    companyLng = kwargs.get('companyLng', "113.32104999")
    companyLat = kwargs.get('companyLat', "23.135011")

    com_step2_url = "https://hr.lagou.com/corpCenter/company/auth/step2.html"
    com_html = get_requests(com_step2_url)
    comAuthId = re.findall('userId: "(.*?)"', com_html.text, re.S)[0]
    completeInfo_url = "https://hr.lagou.com/corpCenter/company/auth/completeInfo.json"
    completeInfo_data = {"id": comAuthId, "logo": "i/audio1/M00/01/C6/CgHIk1wSFMeAeIoaAAB1mvl2DME518.JPG",
                         "officialWebsite": "www.lagou.com", "fullIntro": "愿天下没有难找的工作", "shortIntro": "一天就能找到满意的工作",
                         "detailAddress": detailAddress, "provinceId": provinceId, "cityId": cityId,
                         "districtId": districtId, "businessArea": businessArea, "companyLng": companyLng,
                         "companyLat": companyLat}
    completeInfo_header = get_code_token(com_step2_url)
    remark = "验证B端申请认证公司是否成功"
    return form_post(url=completeInfo_url, data=completeInfo_data, headers=completeInfo_header, remark=remark)


def completeInfo_process(detailAddress=None, provinceId=None, cityId=None, districtId=None, businessArea=None,
                         companyLng=None, companyLat=None):
    r1 = company_auth()
    if r1.get('state', 0) == 1:
        r2 = completeInfo(detailAddress=detailAddress, provinceId=provinceId, cityId=cityId, districtId=districtId,
                          businessArea=businessArea, companyLng=companyLng, companyLat=companyLat)
        return r1, r2


if __name__ == '__main__':
    login('00852', '20190819')
    completeInfo_process()
