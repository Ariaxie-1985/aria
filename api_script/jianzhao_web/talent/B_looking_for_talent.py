# coding:utf-8
# @Author: Xiawang
from utils.util import get_requests, get_code_token, login, form_post

'''
找人才的推荐人才和最新人才
'''


def rec_talent(positionId):
    # 推荐人才
    refer_query_talent_url = f"https://easy.lagou.com/talent/index.htm?filter=0&positionId={positionId}&pageNo=1&strongly=false&notSeen=false"
    query_talent_url = f"https://easy.lagou.com/talent/rec/1.json?positionId={positionId}&notSeen=false&strongly=false"
    query_talent_header = get_code_token(refer_query_talent_url)
    remark = f"为职位{positionId}推荐人才"
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark).json()


def new_talent(positionId):
    # 最新人才
    refer_query_talent_url = f"https://easy.lagou.com/talent/index.htm?positionId={positionId}&showId=&tab=newest&pageNo=1"
    query_talent_url = f"https://easy.lagou.com/talent/newest/1.json?positionId={positionId}&showId="
    query_talent_header = get_code_token(refer_query_talent_url)
    remark = "最新人才"
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark).json()


def talent_get_experiences(positionId, show_id, cUserIds):
    url = 'https://easy.lagou.com/talent/search/getExperiences.json'
    refer_url = f'https://easy.lagou.com/talent/index.htm?positionId={positionId}&showId=&tab=newest&pageNo=1&show_id={show_id}'
    header = get_code_token(url=refer_url)
    data = {'cUserIds': cUserIds, 'type': 'NEWEST'}
    remark = '获取推荐人才的教育经历'
    return form_post(url=url, data=data, headers=header, remark=remark)


def talent_get_action_labels(positionId, show_id, cUserIds):
    url = 'https://easy.lagou.com/talent/search/actionLabels.json'
    refer_url = f'https://easy.lagou.com/talent/index.htm?positionId={positionId}&showId=&tab=newest&pageNo=1&show_id={show_id}'
    header = get_code_token(url=refer_url)
    data = {'cUserIds': cUserIds, 'type': 'NEWEST'}
    remark = '获取推荐人才的简历动态'
    return form_post(url=url, data=data, headers=header, remark=remark)


def talent_hunting(positionId):
    # 猎头人才
    query_talent_url = f"https://easy.lagou.com/talent/hunting.json?positionId={positionId}&pageNo=1"
    refer_query_talent_url = f"https://easy.lagou.com/talent/index.htm?positionId={positionId}&showId=&tab=inspect&pageNo=1"
    query_talent_header = get_code_token(refer_query_talent_url)
    remark = "人才猎手"
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark).json()


def talent_inspect(positionId):
    query_talent_url = f"https://easy.lagou.com/talent/inspect/1.json?positionId={positionId}&showId="
    refer_query_talent_url = f"https://easy.lagou.com/talent/index.htm?positionId={positionId}&showId=&tab=inspect&pageNo=1"
    query_talent_header = get_code_token(refer_query_talent_url)
    remark = "谁看过我"
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark).json()


def talent_search_list(positionName):
    url = 'https://easy.lagou.com/talent/search/list.json'
    refer_url = f'https://easy.lagou.com/talent/search/list.htm?pageNo=1&positionName={positionName}'
    header = get_code_token(url=refer_url)
    data = {'pageNo': 1, 'positionName': positionName, 'searchVersion': 1}
    remark = '通过职位名称来搜索人才'
    return form_post(url=url, data=data, headers=header, remark=remark)


def talent_collection_list():
    url = 'https://easy.lagou.com/collection/collection/list.json'
    refer_url = f'https://easy.lagou.com/collection/index.htm?'
    header = get_code_token(url=refer_url)
    data = {'pageNo': 1, 'pageSize': 15}
    remark = '人才收藏列表'
    return form_post(url=url, data=data, headers=header, remark=remark)


def talent_collection_count():
    refer_query_talent_url = f"https://easy.lagou.com/collection/index.htm?"
    query_talent_url = f"https://easy.lagou.com/collection/count.json"
    query_talent_header = get_code_token(refer_query_talent_url)
    remark = "人才收藏统计"
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark).json()


if __name__ == '__main__':
    # 登录
    a = 1
    b = f"我是第{a}名"
    print(b)
