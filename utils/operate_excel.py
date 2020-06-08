# coding:utf-8
# @Time  : 2019-03-20 16:52
# @Author: Xiawang
import pathlib
import pandas as pd
from pandas import DataFrame

pd.set_option('mode.chained_assignment', None)


# def update_excel(file_path, companyId, contractNo):
#     data = pd.read_excel(file_path, sheet_name='import')
#     data['甲方id'][0] = companyId
#     data['合同编号'][0] = contractNo
#     r = DataFrame(data).to_excel(file_path, sheet_name='import', index=False, header=True)
#     return r


def update_excel(file_path, companyId, contractNo):
    pd.ExcelWriter(file_path)
    if not pathlib.Path(file_path):
        assert False
    if 'import1.xls' in file_path:
        data = pd.DataFrame(data={'甲方id': [companyId], '联系人': ['wangxia'],
                                  '电话': ['17744444444'], '邮箱': ['anan@lagou.com'],
                                  '合同编号': [contractNo]})
    elif 'import2.xls' in file_path:
        data = pd.DataFrame(data={'甲方id': [companyId], '合同编号': [contractNo],
                                  '合同名称': ['ice的拉勾加'], '是否开票': ['是'],
                                  '新老客户': ['老客户'], '所属人': ['martin'],
                                  '所属人2': [''], '所属TL': ['stone'],
                                  '所属城市': ['北京'], '合同金额': ['9000'],
                                  '折扣金额':['9000'],'回款':['9000'],
                                  '合同登记时间': ['2020/3/20  00:00:00'], '合同签约时间': ['2020/3/20  00:00:00'],
                                  '合同终止时间': ['2029/3/20  00:00:00'], '合同回传时间': ['2020/3/30  00:00:00'],
                                  '回款期限': ['10日'], '合同状态': ['无合同，邮箱确认'], '合同详细状态': ['好了'],
                                  '折扣': [''], '备注': [''], '关联公司': ['']
                                  })
    DataFrame(data).to_excel(file_path, sheet_name='import', index=False)


if __name__ == '__main__':
    # create_excel()
    pass
