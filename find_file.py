# -*- coding: utf-8 -*-
'''
@File  : find_file.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/20 0020 10:57
'''

import sys,glob,os

L=os.listdir('d:\\')
base_path='d:\\'

def f(x):
    if os.path.isdir(os.path.join(base_path, x)):
        return x
    else:
        pass
l=map(f,L)
print(L)
li=list(l)
print(li)
List=[]
for lis in li:
    print(lis)
for i in range(len(li)):
    if li[i]:
        List.append(li[i])
print(List)

import xlrd
