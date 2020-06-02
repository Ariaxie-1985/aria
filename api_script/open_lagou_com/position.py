# coding:utf-8
# @Time  : 2020/6/2 11:10
# @Author: Xiawang
# Description:
import datetime
import time

from utils.util import get_requests, form_post


def category_get(access_token):
    url = 'https://open.lagou.com/position/category/get'
    data = {'access_token': access_token}
    remark = '获取职位类别'
    return get_requests(url=url, data=data, remark=remark)


def company_address_list(access_token, page_no=1, page_size=20):
    url = 'https://open.lagou.com/position/address/company/list'
    data = {'access_token': access_token, 'page_no': page_no, 'page_size': page_size}
    remark = '获取公司的所有地址'
    return get_requests(url=url, data=data, remark=remark)


def company_address_district(access_token):
    url = 'https://open.lagou.com/position/address/district/get'
    data = {'access_token': access_token}
    remark = '获取省市区'
    return get_requests(url=url, data=data, remark=remark)


def company_address_create(access_token, openid, **kwargs):
    province = kwargs.get('province', '北京')
    city = kwargs.get('city', '北京')
    area = kwargs.get('area', '朝阳区')
    detail = kwargs.get('detail', '爱奇艺大厦')

    url = f'https://open.lagou.com/position/address/create?access_token={access_token}&openid={openid}'
    data = {'province': province, 'city': city, 'area': area, 'detail': detail}
    remark = '获取省市区'
    return form_post(url=url, data=data, remark=remark)


def address_query(access_token, **kwargs):
    province = kwargs.get('province', '北京')
    city = kwargs.get('city', '北京')
    area = kwargs.get('area', '朝阳区')

    url = 'https://open.lagou.com/v1/position/address/query'
    data = {'access_token': access_token, 'province': province, 'city': city, 'area': area}
    remark = '根据省市区查询公司的地址'
    return get_requests(url=url, data=data, remark=remark)


def position_create(access_token, openid, **kwargs):
    address_id = kwargs.get('address_id', 0)
    name = kwargs.get('name', '拉勾测试python后端')
    first_category_name = kwargs.get('first_category_name', '开发|测试|运维类')
    second_category_name = kwargs.get('second_category_name', '后端开发')
    third_category_name = kwargs.get('third_category_name', 'Python')
    detail = kwargs.get('detail', '肯加班拿钱少肯加班拿钱少肯加班拿钱少肯加班拿钱少肯加班拿钱少肯加班拿钱少肯加班拿钱少肯加班拿钱少肯加班拿钱少肯加班拿钱少')
    advantage = kwargs.get('advantage', '20薪,每年出国游')
    education = kwargs.get('education', '本科')
    work_year = kwargs.get('work_year', '1年')
    max_salary = kwargs.get('max_salary', 15)
    min_salary = kwargs.get('min_salary', 10)
    position_nature = kwargs.get('position_nature', '全职')
    department = kwargs.get('department', '质量保障部')

    url = f'https://open.lagou.com/v1/position/create?access_token={access_token}&openid={openid}'
    data = {'address_id': address_id, 'name': name, 'first_category_name': first_category_name,
            'second_category_name': second_category_name, 'third_category_name': third_category_name,
            'detail': detail, 'advantage': advantage, 'education': education, 'work_year': work_year,
            'max_salary': max_salary, 'min_salary': min_salary, 'position_nature': position_nature,
            'department': department}
    remark = '发布职位'
    return form_post(url=url, data=data, remark=remark)


def get_position_info(access_token, position_id):
    url = f'https://open.lagou.com/v1/position/get?access_token={access_token}&position_id={position_id}'
    remark = '获取职位信息'
    return get_requests(url=url, remark=remark)


def update_position_info(access_token, **kwargs):
    max_salary = kwargs.get('max_salary', 25)
    min_salary = kwargs.get('min_salary', 20)
    url = f'https://open.lagou.com/v1/position/update?access_token={access_token}'
    data = {'max_salary': max_salary, 'min_salary': min_salary}
    remark = '更新职位信息'
    return form_post(url=url, data=data, remark=remark)


def publish_position(access_token, position_id):
    url = f'https://open.lagou.com/v1/position/publish?access_token={access_token}'
    data = {'position_id': position_id}
    remark = '再发布职位'
    return form_post(url=url, data=data, remark=remark)


def offline_position(access_token, position_id):
    url = f'https://open.lagou.com/v1/position/offline?access_token={access_token}'
    data = {'position_id': position_id}
    remark = '下线职位'
    return form_post(url=url, data=data, remark=remark)


def refresh_position(access_token, position_id):
    url = f'https://open.lagou.com/v1/position/refresh?access_token={access_token}'
    data = {'position_id': position_id}
    remark = '刷新职位'
    return form_post(url=url, data=data, remark=remark)


def get_position_list(access_token):
    url = f'https://open.lagou.com/v1/position/list'
    today = datetime.datetime.now()
    start_time = int(str(time.mktime(time.strptime((today - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
                                                   '%Y-%m-%d %H:%M:%S')) * 1000).split(".")[0])
    end_time = time.time()
    data = {'access_token': access_token, 'start_time': start_time, 'end_time': end_time}
    remark = '获取职位列表信息'
    return get_requests(url=url, data=data, remark=remark)


def delete_position_address(access_token, address_id):
    url = f'https://open.lagou.com/v1/position/address/delete?access_token={access_token}'
    data = {'address_id': address_id}
    remark = '删除地址'
    return form_post(url=url, data=data, remark=remark)
