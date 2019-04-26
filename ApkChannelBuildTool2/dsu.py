# -*- coding: utf8 -*-
import re
import os

re_digits = re.compile(r'(\d+)')


def emb_numbers(s):
    pieces = re_digits.split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces


def sort_strings_with_emb_numbers(alist):
    aux = [(emb_numbers(s), s) for s in alist]
    aux.sort()
    return [s for __, s in aux]


def sort_strings_with_emb_numbers2(alist):
    return sorted(alist, key=emb_numbers)


def CEF(path):
    """
    CLean empty files, 清理空文件夹和空文件
    :param path: 文件路径，检查此文件路径下的子文件
    :return: None
    """
    files = os.listdir(path)  # 获取路径下的子文件(夹)列表
    for file in files:
        print('Traversal at', file)
        if os.path.isdir(file):  # 如果是文件夹
            if not os.listdir(file):  # 如果子文件为空
                os.rmdir(file)  # 删除这个空文件夹
        elif os.path.isfile(file):  # 如果是文件
            if os.path.getsize(file) == 0:  # 文件大小为0
                os.remove(file)  # 删除这个文件
    print(path, 'Dispose over!')
