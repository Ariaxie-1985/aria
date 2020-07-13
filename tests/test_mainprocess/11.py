# a =  -1
# if a >3:
#     print(a)
# else:
#     print("a不大于3")
# orderNo = {}
# a = 3
# id = [1,2,3,4,5]
# for i in id:
#     orderNo.update({i:a})
# print(orderNo)
from utils.read_file import read_shop_time, record_shop_time,record_shop_order,read_shop_order
import pytest, os, ast
orderNo= {}
order = {1: 3, 2: 3, 3: 3, 4: 3}
file_path = os.getcwd()

# a = 3
# id = [1,2,3,4,5]
# for i in id:
#     orderNo.update({i:a})
#     b =list(order.keys())
#     if i not in b:
#         order.update({i:a})
a = read_shop_order(file_path)
b=list(a.keys())
print(b)








