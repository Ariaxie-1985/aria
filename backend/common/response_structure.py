# coding:utf-8
# @Time  : 2019-09-03 14:47
# @Author: Xiawang
# Description:
from backend.common.new_models import User


class ResponseStructure:

    def set_username(self, data, id, user):
        # todo 重构， **kwargs
        result = User.get_or_none(User.id == id)
        if result:
            data[user] = result.username
        else:
            data[user] = None
        return data

