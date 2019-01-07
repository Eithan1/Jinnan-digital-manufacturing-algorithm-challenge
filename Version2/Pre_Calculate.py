# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:34:44 2019

@author: Van
"""
import datetime
import pandas as pd
import re

#取出列数据，寻找分号并替换为逗号，忽略掉NaN,删除掉中文汉字‘分’
def Semicolon_Replace(Data_in):
    Data_out = pd.Series([])
    for i in range(len(Data_in)):
        if(not isinstance(Data_in[i],float)):
            temp = re.findall(r"\d{1,2}",Data_in[i])
            if(len(temp) == 4):
                Data_out.loc[i] = temp[0]+':'+temp[1]+'-'+temp[2]+':'+temp[3]
                Data_out.loc[i] = re.sub(r'24:','0:',Data_out[i])
            else:
                Data_out.loc[i] = float('nan')
        else:
            Data_out.loc[i] = Data_in[i]
    return Data_out

#时间长度求解
def Duration(Data):
    for i in range(len(Data)):
        if(not isinstance(Data[i],float)):
            timearr1 = Data[i].split('-')
            timearr0 = datetime.datetime.strptime(timearr1[0],'%H:%M')
            timearr1 = datetime.datetime.strptime(timearr1[1],'%H:%M')
            Data[i] = (timearr1 - timearr0).seconds / 60
        else:
            continue

#时间点编码
def Time_Code(Data_in, col):
    Data_temp = pd.Series([])
    for i in range(len(Data_in)):
        if (not isinstance(Data_in[i], float)):
            temp = re.findall(r"\d{1,2}", Data_in[i])
            if (len(temp) < 4):
                Data_temp.loc[i] = int(temp[0])
            else:
                Data_temp.loc[i] = -1
        else:
            Data_temp.loc[i] = -1
    Data_out = pd.get_dummies(Data_temp, prefix=col)#One-hot coding

    return Data_out

# data_train = pd.read_csv("jinnan_round1_train_20181227.csv", encoding = 'gbk')
# data_test = pd.read_csv("jinnan_round1_testA_20181227.csv", encoding = 'gbk')
# data_all = pd.concat((data_train, data_test), axis=0, sort=False,ignore_index=True) #sort=False不改变原先列顺序
#data_all = data_all.reset_index(drop=True)
# samples = data_all.pop('样本id')
# test = pd.Series([])
# a=data_all['A5']
# test = Time_Code(a)
# data_all['A5'] = Pre_Calculate.Time_Code(data_all['A5'])
# data_all['A5'] = Pre_Calculate.Time_Code(data_all['A5'])
# data_all['A5'] = Pre_Calculate.Time_Code(data_all['A5'])