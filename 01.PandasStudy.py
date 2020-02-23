# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:55:09 2020

@author: zhoubo
"""

# pandas常用数据类型
# series 一维，带标签数组
#%%
import pandas as pd


# 默认索引是0开始
t= pd.Series([1,2,3])
print(t)
print(type(t))

#可以指定索引
t2 =pd.Series([1,23,2,2,1],index =list('abcde'))
print(t2)


# 通过字典创建Series
temp_dict={'name':'小红','age':20,'tel':10086}
t3 =pd.Series(temp_dict)
print(t3)

import string

# 用string里的一个方法生成A-Z
a={string.ascii_uppercase[i]:i for i in range(10)}
print(pd.Series(a))
a=pd.Series(a,list(string.ascii_uppercase[5:15]))#如果重新指定index，新的index中的值对应旧的，新的index与旧的index不一样的 值替换成nan
print(a)


#%%修改dtype
import pandas as pd
t= pd.Series([1,2,3])
print(t)
t =t.astype(float)
print(t.dtype)




















