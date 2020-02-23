# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:16:06 2020

@author: zhoubo
"""
#%%DataFrame基础属性
import pandas as pd
import numpy as np

dict1 ={'name':['小明','小红','小刚'],'age':[20,32,19],'tel':[10086,10022,10000]}#记住对于dataFrame来说 每一行代表一个数据 每一列代表一种类型的所有数据
df =pd.DataFrame(dict1)
print(df)

#形状 shape
print(df.shape)

#数据类型 注意加s了
print(df.dtypes)

#数据维度
print(df.ndim)

#行索引 index
print(df.index)

#列索引
print(df.columns)

#对象值 values
print(df.values,type(df.values))#numpy数组
print('*'*50)


#DataFrame整体情况查询

#显示头几行 默认是5行
print(df.head(2))

#显示末尾几行 默认5
print(df.tail(1))

#显示相关信息
print(df.info())#浏览 行数 列数 列索引 列非空值个数 列类型 内存

#显示综合统计结果 计数 均值 标准差 最大值 四分位数 最小值
print(df.describe())







