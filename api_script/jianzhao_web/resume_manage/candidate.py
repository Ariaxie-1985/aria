# coding:utf-8
# @Time  : 2019-01-25 11:34
# @Author: Xiawang
from utils.util import get_code_token, form_post, get_header, json_post, login


def can_new_list():
	url = "https://easy.lagou.com/can/new/list.json"
	header = get_code_token(
		"https://easy.lagou.com/can/index.htm?stage=NEW&pageNo=1&can=true&needQueryAmount=true&newDeliverTime=0")
	data = {
		"stage": "NEW",
		"pageNo": 1,
		"can": True,
		"needQueryAmount": True,
		"newDeliverTime": 0
	}
	remark = "获取简历列表"
	return form_post(url=url, data=data, headers=header, remark=remark)


def can_new_createFilter():
	url = "https://easy.lagou.com/can/new/createFilter.json"
	header = get_code_token(
		"https://easy.lagou.com/can/index.htm?stage=NEW&pageNo=1&can=true&needQueryAmount=true&newDeliverTime=0&plusTypes=2%2C1&channels=108")
	data = {
		"name": "1",
		"newDeliverTime": "0",
		"channels": "108",
		"plusTypes": "2,1",
		"famousCompany": "0",
		"stages": "NEW"
	}
	remark = "创建候选人筛选器"
	return form_post(url=url, data=data, headers=header, remark=remark)


def can_new_myfilters():
	url = "https://easy.lagou.com/can/new/myfilters.json"
	header = get_code_token(
		"https://easy.lagou.com/can/index.htm?pageNo=1&needQueryAmount=true&can=true&stage=NEW&newDeliverTime=0&channels=108&plusTypes=2%2C1&famousCompany=false")
	remark = "获取候选人筛选器"
	return form_post(url=url, headers=header, remark=remark)


def resume_deleteResumeFilter(resumeFilterId):
	url = "https://easy.lagou.com/resume/deleteResumeFilter.json"
	header = get_code_token(
		"https://easy.lagou.com/can/index.htm?pageNo=1&needQueryAmount=true&can=true&stage=NEW&newDeliverTime=0&channels=108&plusTypes=2%2C1&famousCompany=false")
	data = {
		"resumeFilterId": resumeFilterId
	}
	remark = "删除候选人筛选器"
	return form_post(url=url, data=data, headers=header, remark=remark)


def can_recommend(resumeId, parentPositionId):
	url = "https://easy.lagou.com/can/recommend.json"
	header = get_code_token(
		"https://easy.lagou.com/can/new/index.htm?can=true&stage=NEW&needQueryAmount=true&newDeliverTime=0&pageNo=1")
	data = {
		"resumeId": resumeId,
		"parentPositionId": parentPositionId
	}
	remark = "推荐候选人到职位"
	return form_post(url=url, data=data, headers=header, remark=remark)


def can_batch_recommend(resumeIds, parentPositionId):
	url = "https://easy.lagou.com/can/batch/recommend.json"
	header = get_code_token(
		"https://easy.lagou.com/can/new/index.htm?can=true&stage=NEW&needQueryAmount=true&newDeliverTime=0&pageNo=1")
	data = {
		"resumeIds": resumeIds,
		"parentPositionId": parentPositionId
	}
	remark = "批量推荐候选人到职位"
	return form_post(url=url, data=data, headers=header, remark=remark)


def resume_uploadLocalResume(positionId, file_Path):
	url = "https://easy.lagou.com/resume/uploadLocalResume.json"
	header = get_header("https://easy.lagou.com/resume/uploadLocalResume.htm")
	data = {'channelId': "-1", 'autoCandidate': '1', "positionId": positionId,
	        "id": "WU_FILE_0", "name": "uploadLocalresume.pdf", "type": "application/pdf",
	        "lastModifiedDate": "Wed Apr 25 2018 18:43:40 GMT+0800 (中国标准时间)",
	        "size": "53296"}
	files = {'file': open(file_Path, 'rb')}
	remark = "上传简历"
	return form_post(url=url, data=data, files=files, headers=header, remark=remark)


def resume_uploadCandidateson(phone,parentPositionId, file_Path):
	url = "https://easy.lagou.com/resume/uploadCandidate.json"
	header = get_header("https://easy.lagou.com/resume/uploadLocalResume.htm")
	data = {'channelId': "-1", 'phone': phone, "parentPositionId": parentPositionId,
	        "candidateName": "初心哥", "email": "{}@sina.com".format(phone), "description": "有潜力的候选人"}
	files = {'file': open(file_Path, 'rb')}
	remark = "上传候选人"
	return form_post(url=url, data=data, files=files, headers=header, remark=remark)


def multiChannel_myCompanyParentPositions():
	url = "https://easy.lagou.com/parentPosition/multiChannel/myCompanyParentPositions.json"
	header = get_code_token(
		"https://easy.lagou.com/can/new/index.htm?can=true&stage=NEW&needQueryAmount=true&newDeliverTime=0&pageNo=1")
	remark = "获取所在公司的父职位-parentPositionId"
	return form_post(url=url, headers=header, remark=remark)


