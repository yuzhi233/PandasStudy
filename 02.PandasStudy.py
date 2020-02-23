# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 13:39:03 2020

@author: zhoubo
"""

#%% pandas索引和切片
import pandas as pd

#对于Series来说：

t =pd.Series({'name':'xiaohong','age':18,'telphone':1008611})
print('t\n',t)
print('*'*50)


# 通过索引index取值
print(t['age'])
print('*'*50)
#注意索引取的是 字典的  值
print(t[0],t[2])#按行

# 取连续行
print(t[:2])
print('*'*50)

# 取不连续多行     索引的中括号里再来个中括号（传入列表）  
print(t[[0,2]])#取第1，3行
print('*'*50)
print(t[['age','telphone']])#列表里传 需要的index 拿出指定的行
print('*'*50)


#用bool操作取相应的行
t2 =pd.Series([i for i in range(10)])
print('t2:\n',t2)
print('*'*50)


print(t2<5)#返回的bool量
print(t2[t2<5])#取出符合条件的行

#对于一个陌生的Series 如何知道index和values呢 

#============================索引操作==========================================

# -------------------------对于刚才的字典生成的series---------------------------
print(t.index)#Index(['name', 'age', 'telphone'], dtype='object')

print(type(t.index))#<class 'pandas.core.indexes.base.Index'>

#t.index是一个可迭代序列
for i in t.index:
    print(i)
#可以list()成列表
print(list(t.index))

#--------------------------对于数字series--------------------------------------
print(t2.index)# RangeIndex(start=0, stop=10, step=1) 与上面些许不同


#=============================values操作========================================

print(t.values)
print(type(t.values))#<class 'numpy.ndarray'>  value值的类型是 np 中的array类型
































