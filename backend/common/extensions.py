# coding:utf-8
# @Time  : 2019-08-03 21:44
# @Author: Xiawang
from flask import make_response
from playhouse.shortcuts import model_to_dict


def convert_json(table_model, id):
    table_model = table_model.get_by_id(id)
    result = model_to_dict(table_model)
    for k, v in result.items():
        if isinstance(v, dict):
            v['update_time'] = v['update_time'].strftime("%Y-%m-%d %H:%M:%S")
            v['create_time'] = v['create_time'].strftime("%Y-%m-%d %H:%M:%S")
    result['update_time'] = result['update_time'].strftime("%Y-%m-%d %H:%M:%S")
    result['create_time'] = result['create_time'].strftime("%Y-%m-%d %H:%M:%S")
    return result


def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    resp = make_response(data, code)
    resp.headers.extend(headers or {})

    return resp




if __name__ == '__main__':
    # print(check_password(1, '12345678'))
    # from common.new_models import TestSheet, User

    # t = TestSheet.select().order_by(TestSheet.create_time.desc()).paginate(1, 10)
    # r = PaginatedQuery(t,paginate_by=1).get_page_count()
    # r = PaginatedQuery(t, paginate_by=1, page_var=2).get_object_list()
    # testsheet_data = convert_json(TestSheet, r.id)
    # print(r)
    pass
