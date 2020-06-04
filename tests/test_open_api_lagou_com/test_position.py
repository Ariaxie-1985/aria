# coding:utf-8
# @Time  : 2020/6/3 11:14
# @Author: Xiawang
# Description:
import time

import pytest

from api_script.entry.deliver.deliver import get_resume_info, deliver_create
from api_script.open_lagou_com.position import category_get, company_address_district, company_address_create, \
    address_query, company_address_list, position_create, get_position_info, update_position_info, get_position_list, \
    offline_position, refresh_position, publish_position, delete_position_address
from utils.util import assert_equal


@pytest.mark.incremental
class TestPosition:
    def test_category_get(self, get_access_token):
        res = category_get(get_access_token)
        assert_equal(0, res.get('code'), '获取职位类别请求成功', '获取职位类别请求失败')
        assert_equal("开发|测试|运维类", res['data']['categories']['categories'][0]['name'], '职位类别验证通过', '职位类别验证失败')

    def test_company_address_district(self, get_access_token):
        res = company_address_district(get_access_token)
        assert_equal(0, res.get('code'), '获取省市区请求成功', '获取省市区请求失败')
        assert_equal("北京", res['data']['districtinfos'][0]['district_name'], '一级省验证通过', '一级省验证失败')

    def test_company_address_create(self, get_access_token, get_openid):
        res = company_address_create(access_token=get_access_token, openid=get_openid)
        assert_equal(0, res.get('code'), '创建地址请求成功', '创建地址请求失败')
        global address_id
        address_id = res['data']['address_id']
        assert_equal(True, bool(address_id), '地址创建验证通过', '地址创建验证失败')

    def test_address_query(self, get_access_token):
        res = address_query(access_token=get_access_token)
        assert_equal(0, res.get('code'), '查询地址请求成功', '查询地址请求失败')
        assert_equal(address_id, res['data']['addresses'][0]['address_id'], '查询创建的地址用例通过', f'查询创建的地址{address_id}用例失败')

    def test_company_address_list(self, get_access_token):
        res = company_address_list(access_token=get_access_token)
        assert_equal(0, res.get('code'), '查询地址请求成功', '查询地址请求失败')
        assert_equal(address_id, res['data']['addresses'][0]['address_id'], '查询创建的地址用例通过', '查询创建的地址用例失败')

    def test_position_create(self, get_access_token, get_openid):
        res = position_create(access_token=get_access_token, openid=get_openid, address_id=address_id)
        assert_equal(0, res.get('code'), '创建职位请求成功', '创建职位请求失败')
        global position_id, jd_id
        position_id = res['data']['id']
        jd_id = res['data']['jd_url'].split('/')[-1]
        assert_equal(True, bool(position_id), '创建职位用例通过', '创建职位用例失败')

    def test_get_create_position_info(self, get_access_token):
        res = get_position_info(access_token=get_access_token, position_id=position_id)
        assert_equal(0, res.get('code'), '获取创建的职位信息请求成功', '获取创建的职位信息请求失败')
        assert_equal(position_id, res['data']['position']['position_id'], '查询创建的职位信息用例通过',
                     f'查询创建的职位{position_id}信息用例失败')

    def test_get_resume_info(self, c_login_app):
        r = get_resume_info(userToken=c_login_app[0])
        global resumeId, resumeType
        resumeId = r['content'][0]['resumeId']
        resumeType = r['content'][0]['resumeType']
        assert_equal(1, r.get('state'), "校验获取简历信息成功")

    def test_deliver_create(self, c_login_app):
        r = deliver_create(positionId=jd_id, resumeId=resumeId, resumeType=resumeType, H9=True, isTalk=False,
                           userToken=c_login_app[0])
        assert_equal(1, r.get('state'), "校验投递简历成功！")

    def test_update_position_info(self, get_access_token):
        res = update_position_info(access_token=get_access_token, position_id=position_id, address_id=address_id)
        assert_equal(0, res.get('code'), '更改职位信息请求成功', '更改职位信息请求失败')
        assert_equal(position_id, res['data']['id'], '更改职位信息用例通过', f'更改职位{position_id}信息用例失败')

    def test_get_update_position_info(self, get_access_token):
        time.sleep(1)
        res = get_position_info(access_token=get_access_token, position_id=position_id)
        assert_equal(0, res.get('code'), '更改职位信息请求成功', '更改职位信息请求失败')
        assert_equal(20, res['data']['position']['min_salary'], '更改职位的最小薪资信息用例通过', f'更改职位的最小薪资{position_id}信息用例失败')
        assert_equal(25, res['data']['position']['max_salary'], '更改职位的最大薪资信息用例通过', f'更改职位的最大薪资{position_id}信息用例失败')

    @pytest.mark.parametrize('status', [('ONLINE'), ('OFFLINE')])
    def test_get_position_list(self, get_access_token, status):
        time.sleep(1)
        res = get_position_list(access_token=get_access_token, status=status)
        assert_equal(0, res.get('code'), '获取职位列表信息请求成功', '获取职位列表信息请求失败')
        for position in res['data']['positions']:
            if status == 'ONLINE':
                assert_equal('NORMAL', position['status'], '获取在线职位用例通过', '获取在线职位用例失败')
            else:
                assert_equal(status, position['status'], '获取已下线职位用例通过', '获取已下线职位用例失败')

    def test_offline_position(self, get_access_token):
        res = offline_position(access_token=get_access_token, position_id=position_id)
        assert_equal(0, res.get('code'), '下线职位请求成功', f'下线职位{position_id}请求失败')

    def test_publish_position(self, get_access_token):
        res = publish_position(access_token=get_access_token, position_id=position_id)
        assert_equal(0, res.get('code'), '发布已下线职位请求成功', f'发布已下线职位{position_id}请求失败')

    def test_refresh_position(self, get_access_token):
        res = refresh_position(access_token=get_access_token, position_id=position_id)
        assert_equal(30040, res.get('code'), '一小时之内不可重复刷新职位请求成功', f'一小时之内不可重复刷新职位{position_id}请求失败')

    def test_delete_position_address(self, get_access_token):
        res = delete_position_address(access_token=get_access_token, address_id=address_id)
        assert_equal(0, res.get('code'), '删除地址请求成功', f'删除地址{address_id}请求失败')
