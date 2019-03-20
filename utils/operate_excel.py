# coding:utf-8
# @Time  : 2019-03-20 16:52
# @Author: Xiawang

import pandas as pd
from pandas import DataFrame


def update_excel(file_path, companyId, contractNo):
    data = pd.read_excel(file_path,sheet_name='import')
    data['甲方id'][0] = companyId
    data['合同编号'][0] = contractNo
    r = DataFrame(data).to_excel(file_path,sheet_name='import', index=False, header=True)
    return r

