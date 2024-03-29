# coding:utf-8
# @Author: Xiawang
from utils.util import get_requests, get_code_token, login, form_post, login_password, get_header

'''
找人才的推荐人才和最新人才
'''


def rec_talent(positionId):
    # 推荐人才
    refer_query_talent_url = f"https://easy.lagou.com/talent/index.htm?filter=0&positionId={positionId}&pageNo=1&strongly=false&notSeen=false"
    query_talent_url = f"https://easy.lagou.com/talent/rec/1.json?positionId={positionId}&notSeen=false&strongly=false"
    query_talent_header = get_code_token(refer_query_talent_url)
    remark = f"为职位{positionId}推荐人才"
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark)


def new_talent(positionId):
    # 最新人才
    refer_query_talent_url = f"https://easy.lagou.com/talent/index.htm?positionId={positionId}&showId=&tab=newest&pageNo=1"
    query_talent_url = f"https://easy.lagou.com/talent/newest/1.json?positionId={positionId}&showId="
    query_talent_header = get_code_token(refer_query_talent_url)
    remark = "最新人才"
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark)


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
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark)


def talent_inspect(positionId):
    query_talent_url = f"https://easy.lagou.com/talent/inspect/1.json?positionId={positionId}&showId="
    refer_query_talent_url = f"https://easy.lagou.com/talent/index.htm?positionId={positionId}&showId=&tab=inspect&pageNo=1"
    query_talent_header = get_code_token(refer_query_talent_url)
    remark = "谁看过我"
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark)


def talent_search_list(positionName):
    url = 'https://easy.lagou.com/talent/search/list.json'
    refer_url = f'https://easy.lagou.com/talent/search/list.htm?pageNo=1&positionName={positionName}'
    header = get_code_token(url=refer_url)
    data = {'pageNo': 1, 'positionName': positionName, 'searchVersion': 1}
    remark = '通过职位名称来搜索人才'
    return form_post(url=url, data=data, headers=header, remark=remark)


def talent_collection_list(ip_port=None):
    url = 'https://easy.lagou.com/collection/collection/list.json'
    refer_url = f'https://easy.lagou.com/collection/index.htm?'
    header = get_code_token(url=refer_url, ip_port=ip_port)
    data = {'pageNo': 1, 'pageSize': 15}
    remark = '人才收藏列表'
    return form_post(url=url, data=data, headers=header, remark=remark, ip_port=ip_port)


def talent_collection(positionId, cueserid, resumeFetchKey):
    # 收藏人才
    refer_url = f"https://easy.lagou.com/talent/index.htm?positionId={positionId}&showId=&tab=newest&pageNo=1"
    url = f"https://easy.lagou.com/collection/collection.json?"
    header = get_code_token(refer_url)
    data = {'cuserId': cueserid, 'resumeFetchKey': resumeFetchKey}
    remark = "收藏人才"
    return form_post(url=url, data=data, headers=header, remark=remark, rd='Mandy')


def talent_uncollection(collectionIds, ip_port=None):
    # 取消收藏人才
    refer_url = f"https://easy.lagou.com/collection/index.htm?"
    url = f"https://easy.lagou.com/collection/unCollection.json?"
    header = get_code_token(refer_url, ip_port=ip_port)
    data = {'collectionIds': collectionIds}
    remark = "取消收藏人才"
    return form_post(url=url, data=data, headers=header, remark=remark, ip_port=ip_port, rd='Mandy')


def talent_pages(positionId):
    # 人才页面上下翻页
    refer_url = f"https://easy.lagou.com/talent/index.htm?positionId={positionId}&showId=&notSeen=false&strongly=false&tab=rec&pageNo=1"
    url = f"https://easy.lagou.com/talent/rec/2.json?positionId={positionId}&showId=&notSeen=false&strongly=false"
    query_talent_header = get_code_token(refer_url)
    remark = "上下翻页"
    return get_requests(url=url, headers=query_talent_header, remark=remark, rd='Mandy')


def talent_collection_count(ip_port=None):
    refer_query_talent_url = f"https://easy.lagou.com/collection/index.htm?"
    query_talent_url = f"https://easy.lagou.com/collection/count.json"
    query_talent_header = get_code_token(refer_query_talent_url, ip_port=ip_port)
    remark = "人才收藏统计"
    return get_requests(url=query_talent_url, headers=query_talent_header, remark=remark, ip_port=ip_port)


def talent_search_by_company_name_list(company_name, pageNo=1):
    url = 'https://easy.lagou.com/talent/search/list.json'
    refer_url = f'https://easy.lagou.com/talent/search/list.htm?pageNo={pageNo}&keyword={company_name}&searchVersion=1'
    header = get_header(url=refer_url)
    header.update(
        {'x-anit-forge-code': '', 'x-anit-forge-token': '', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors',
         'sec-fetch-site': 'same-origin', 'pragma': 'no-cache',
         'referer': f'https://easy.lagou.com/talent/search/list.htm?pageNo={pageNo}&searchVersion=1&companyName=%E6%9D%B0%E5%A8%81%E5%B0%94%E9%9F%B3%E4%B9%90'})
    data = {'pageNo': pageNo, 'keyword': company_name, 'searchVersion': 1}
    remark = '通过工作经历的公司名称来搜索人才'
    return form_post(url=url, data=data, headers=header, remark=remark)


if __name__ == '__main__':
    login_password(username='13033647506', password='9062e77da243687c68bf9665727b5c01')
