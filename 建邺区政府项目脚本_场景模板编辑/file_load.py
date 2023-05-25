# !/usr/bin/env/ python
# -*- coding: utf-8 -*-
# @Time : 2023/2/25 17:23
# Author : zhaoning
# File : file_load.py
import os

import pandas as pd

# def read_data(path='./bc_data.csv',sheet_name=0):
#     data = pd.read_excel(path,sheet_name)
#     return data
#
def get_csv_data(filename,dir='./'):
    fname = os.path.join(dir,filename)
    f = open(fname,encoding='UTF-8')
    data = pd.read_csv(f)
    f.close()
    return data

def read_by_rows(n,filename):
    df = get_csv_data(filename)
    data = df.iloc[n]
    return data
def get_data_by_rows(n,m,filename):
    data = read_by_rows(n,filename)
    return data[m]

def read_by_colums(colums_name,filename):
    df = get_csv_data(filename)
    data = df[colums_name]
    return data


#
# list = []
# uuid = read_by_colums('uuid',filename='bc_data.csv')
# # print(uuid[1])
# for i in range(len(uuid)):
#     list.append(uuid[i])
# print(list)