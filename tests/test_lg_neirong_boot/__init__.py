# coding:utf-8
# @Time  : 2019-01-29 11:38
# @Author: Xiawang
a = {
    "state": 1,
    "message": "操作成功",
    "content": {
        "positionTypes": [
            {
                "positionTypeName": "全部",
                "code": 0,
                "isExsit": 1
            },
            {
                "positionTypeName": "技术",
                "code": 1,
                "isExsit": 0
            },
            {
                "positionTypeName": "产品",
                "code": 2,
                "isExsit": 1
            },
            {
                "positionTypeName": "设计",
                "code": 3,
                "isExsit": 0
            },
            {
                "positionTypeName": "运营",
                "code": 4,
                "isExsit": 0
            },
            {
                "positionTypeName": "市场",
                "code": 5,
                "isExsit": 0
            },
            {
                "positionTypeName": "销售",
                "code": 6,
                "isExsit": 0
            },
            {
                "positionTypeName": "职能",
                "code": 7,
                "isExsit": 0
            },
            {
                "positionTypeName": "其他",
                "code": 8,
                "isExsit": 0
            },
            {
                "positionTypeName": "校招",
                "code": 9,
                "isExsit": 0
            }
        ],
        "expectPositionType": 1
    },
    "uiMessage": None
}

print(bool(a['content']['positionTypes']))
