# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:37:56 2020

@author: zhoubo
"""

#%%series读取外部数据
import pandas as pd

#读取csv中的数据
df =pd.read_csv('./train.csv')#读取的df类型就是下面要说的DataFrame
print(df)


#%%DataFrame 二维  是Series的容器
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(12).reshape(3,4))

# DataFrame对象既有行索引，又有列索引
# 行索引，表明不同行，横向索引，叫index，0轴，axis=0
# 列索引，表名不同列，纵向索引，叫columns，1轴，axis=1


#替换默认的 index 和columns
df2 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns =list('efgh'))


#通过字典创建DataFrame
dict1 ={'name':['小明','小红','小刚'],'age':[20,32,19],'tel':[10086,10022,10000]}#记住对于dataFrame来说 每一行代表一个数据 每一列代表一种类型的所有数据
df3 =pd.DataFrame(dict1)
print(df3)

#通过列表里放字典创建DataFrame 反正遵循原则 每一行是一个数据 （一个数据有不同指标构成）
list1 =[{'name':'小红','age':18,'tel':10000},{'name':'小明','tel':10086},{'name':'小刚','age':18,'tel':10011}]
df4 =pd.DataFrame(list1)
print(df4)#如果缺失某项数据  会变成nan
