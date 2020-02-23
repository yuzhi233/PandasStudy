# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:07:40 2020

@author: zhoubo
"""
#%%pandas  DataFrame索引切片
import pandas as pd



origin_df =pd.read_csv('./train.csv')



#pandas取行列注意的点
# 方括号写数组，表示取行索引，对行进行操作
# 写字符串，表示的取列索引，对列进行操作


#====================取csv文件中前10行的数据===================================
df =origin_df[:10]


#===================取csv文件中某一（几）列 （一列就是series)=================== 
df2 =origin_df['SalePrice']
df2_=origin_df[:]['SalePrice']#等价于上面 

df3 =origin_df[['MSSubClass', 'LotFrontage', 'SalePrice']]#
#是按你指定的顺序取指定的列
df4 =origin_df[['LotFrontage', 'MSSubClass', 'SalePrice']]


#======================指定行和列===========================================

#两个方括号第一括号指定行 第二个指定列
df4 =origin_df[:10]['MSSubClass']#好像只能指定连续的多行和1列 这种写法


#======================按照某一列 将值进行排序 从小到大========================
# 比如这里对df3排序
df3_sorted =df3.sort_values(by ='SalePrice')
df3_max10 = df3_sorted.tail(10)#取出最后10行





