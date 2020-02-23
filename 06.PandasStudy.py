# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:06:25 2020

@author: zhoubo
"""

#%% pandas 之 loc
#是经过pandas优化的选择方式

import pandas as pd
import numpy as np


#=========================================loc通过标签获取数据=================================
t=pd.DataFrame(np.arange(12).reshape(3,4),index =list('abc'),columns =list('WXYZ'))


#取值指定的索引值 行索引'a' 列索引'Z' t.loc[行,列]
print(t.loc['a','Z'])
print(t.loc['a']['Z'])
print(type(t.loc['a','Z']))#numpy类型


#取整行
print(t.loc['a'])
print(t.loc['a',:])#这俩写法一样
print('*'*50)

#取整列
print(t.loc[:,'Z'])


#取连续多行多列
print('取连续多行多列')
print(t.loc['a':'b','Z'])#这里注意'a':'b'是包含a和b   跟列表索引不太一样


#取任意多行多列
print('*'*50)
print(t.loc[['a','b'],['X','Y']])



#%%=======================================iloc通过位置来获取数据========================
import pandas as pd
import numpy as np
t=pd.DataFrame(np.arange(12).reshape(3,4),index =list('abc'),columns =list('WXYZ'))

#获取值
print(t.iloc[0,0])



#取某一行
print(t.iloc[2,:])#第三行！

#某一列
print(t.iloc[:,2])#第三列！

print("*"*50)

#获取指定行，指定列
print(t.iloc[:,[1,2]])#获取第2列和第3列

print(t.iloc[[0,2],[1,2]])#获取第1行第3行，第2列第3列

#获取连续多行
print(t.iloc[1:,1:])#从第2行到最后 从第2列到最后

