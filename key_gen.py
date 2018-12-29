# # -*- coding: utf-8 -*-
# '''
# @File  : qqq.py
# @Author: 王治本
# @Contact : 568898699@qq.com
# @Date  : 2018/12/19 0019 10:37
# '''
# import string
# import random
#
# KEY_LEN=20
# KEY_ALL=100
#
# def base_str():
#     return (string.ascii_letters+string.digits)
#
# def key_gen():
#     keylist=[random.choice(base_str()) for i in range(KEY_LEN)]
#     return ("".join(keylist))
# def print_key(func):
#     def _print_key(num):
#         for i in func(num):
#             print(i)
#     return _print_key
# @print_key
# def key_num(num,result=None):
#     if result is None:
#         result = []
#     for i in range(num):
#         result.append(key_gen())
#     return result
#
#
# if __name__ == '__main__':
#     # print_key(KEY_ALL)
#     key_num(KEY_ALL)
#

import string
import random

KEY_LEN=20
KEY_ALL=100
def base_str():
    return (string.ascii_letters+string.digits)
def key_gen():
    list=[random.choice(base_str()) for i in range(KEY_LEN)]
    return ''.join(list)
def print_key(func):
    def _print_key(num):
        for i in range(num):
            print(i)
    return  _print_key

@print_key
def key_num(num,result=None):
    if result is None:
        result =[]
    for i in range(num):
        result.append(key_gen())
    return result

