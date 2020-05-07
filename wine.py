#!/usr/bin/env python
# coding: utf-8

# # Wine Review

# 导入所需要的包

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import seaborn as sns 


# 导入数据，给出数据摘要,并检查完整性

# In[2]:


wine=pd.read_csv('./winemag-data_first150k.csv')
wine=wine.drop(labels='Unnamed: 0',axis=1)
wine.info()
print("缺失数据及个数：\n",wine.isnull().sum())


# 数据中包含两个数值属性points和price，其余均为标称属性

# ## 数据去重

# In[3]:


wine.duplicated().value_counts()
wine=wine.drop_duplicates()
#清除重复的数据
dupilicated_index=list(wine[wine[['country','description','designation','province','points','price']].duplicated()].index)
wine=wine.drop(labels=dupilicated_index,axis=0)
wine.reset_index(drop=True)


# # 标称属性
# 输出标称属性的频数，词条太多在此处仅展示每个标称属性的前15项

# In[4]:


plt.figure()
wine['country'].value_counts()[0:15].plot.bar(title='country')
plt.figure()
wine['province'].value_counts()[0:15].plot.bar(title='province')
plt.figure()
wine['region_1'].value_counts()[0:15].plot.bar(title='region_1')
plt.figure()
wine['region_2'].value_counts()[0:15].plot.bar(title='region_2')
plt.figure()
wine['variety'].value_counts()[0:15].plot.bar(title='variety')
plt.figure()
wine['winery'].value_counts()[0:15].plot.bar(title='winery')


# # 数值属性
# ## points情况（五数概括及可视化）

# In[5]:


sns.set(style="darkgrid")
sns.boxplot(y='points',data=wine)
wine.points.describe()


# ## price情况（五数概括及可视化）

# In[14]:


print(wine.price.describe())
plt.figure()
sns.stripplot(y='price',data=wine)
plt.figure()
sns.distplot(wine.price.dropna())


# ## price与points的关系

# In[15]:


plt.figure()
sns.scatterplot(x='price',y='points',data=wine)


# # 数据缺失的处理
# ## 1. 将缺失部分剔除

# In[8]:


wine1=wine.copy(deep=True)
wine1=wine1.dropna() #删除包含空值的所有行
wine1.info()
#对比结果
plt.figure()
plt.subplot(121)
sns.set(style="darkgrid")
sns.boxplot(y='points',data=wine)
wine.points.describe()
plt.subplot(122)
sns.set(style="darkgrid")
sns.boxplot(y='points',data=wine1,color='r')
wine1.points.describe()

plt.figure()
wine.price.describe()
plt.subplot(121)
sns.stripplot(y='price',data=wine)
plt.subplot(122)
sns.stripplot(y='price',data=wine1,color='r')
plt.figure()
plt.subplot(121)
sns.distplot(wine.price.dropna())
plt.subplot(122)
sns.distplot(wine1.price.dropna(),color='r')

plt.figure()
plt.subplot(121)
wine['country'].value_counts()[0:15].plot.bar(title='country')
plt.subplot(122)
wine1['country'].value_counts()[0:15].plot.bar(title='country',color='r')
plt.figure()
plt.subplot(121)
wine['province'].value_counts()[0:15].plot.bar(title='province')
plt.subplot(122)
wine1['province'].value_counts()[0:15].plot.bar(title='province',color='r')
plt.figure()
plt.subplot(121)
wine['region_1'].value_counts()[0:15].plot.bar(title='region_1')
plt.subplot(122)
wine1['region_1'].value_counts()[0:15].plot.bar(title='region_1',color='r')
plt.figure()
plt.subplot(121)
wine['region_2'].value_counts()[0:15].plot.bar(title='region_2')
plt.subplot(122)
wine1['region_2'].value_counts()[0:15].plot.bar(title='region_2',color='r')
plt.figure()
plt.subplot(121)
wine['variety'].value_counts()[0:15].plot.bar(title='variety')
plt.subplot(122)
wine1['variety'].value_counts()[0:15].plot.bar(title='variety',color='r')
plt.figure()
plt.subplot(121)
wine['winery'].value_counts()[0:15].plot.bar(title='winery')
plt.subplot(122)
wine1['winery'].value_counts()[0:15].plot.bar(title='winery',color='r')


# ## 2. 用最高频率值来填补缺失值

# In[9]:


wine1=wine.copy(deep=True)
for i in wine1.columns:
    wine1[i]=wine1[i].fillna(wine1[i].mode()[0])
print(wine1.isnull().sum())
wine1.info()
#对比结果
plt.figure()
plt.subplot(121)
sns.set(style="darkgrid")
sns.boxplot(y='points',data=wine)
wine.points.describe()
plt.subplot(122)
sns.set(style="darkgrid")
sns.boxplot(y='points',data=wine1,color='r')
wine1.points.describe()

plt.figure()
wine.price.describe()
plt.subplot(121)
sns.stripplot(y='price',data=wine)
plt.subplot(122)
sns.stripplot(y='price',data=wine1,color='r')
plt.figure()
plt.subplot(121)
sns.distplot(wine.price.dropna())
plt.subplot(122)
sns.distplot(wine1.price.dropna(),color='r')

plt.figure()
plt.subplot(121)
wine['country'].value_counts()[0:15].plot.bar(title='country')
plt.subplot(122)
wine1['country'].value_counts()[0:15].plot.bar(title='country',color='r')
plt.figure()
plt.subplot(121)
wine['province'].value_counts()[0:15].plot.bar(title='province')
plt.subplot(122)
wine1['province'].value_counts()[0:15].plot.bar(title='province',color='r')
plt.figure()
plt.subplot(121)
wine['region_1'].value_counts()[0:15].plot.bar(title='region_1')
plt.subplot(122)
wine1['region_1'].value_counts()[0:15].plot.bar(title='region_1',color='r')
plt.figure()
plt.subplot(121)
wine['region_2'].value_counts()[0:15].plot.bar(title='region_2')
plt.subplot(122)
wine1['region_2'].value_counts()[0:15].plot.bar(title='region_2',color='r')
plt.figure()
plt.subplot(121)
wine['variety'].value_counts()[0:15].plot.bar(title='variety')
plt.subplot(122)
wine1['variety'].value_counts()[0:15].plot.bar(title='variety',color='r')
plt.figure()
plt.subplot(121)
wine['winery'].value_counts()[0:15].plot.bar(title='winery')
plt.subplot(122)
wine1['winery'].value_counts()[0:15].plot.bar(title='winery',color='r')


# ## 3. 通过属性的相关关系来填补缺失值

# In[12]:


#通过拉格朗日插值法填充缺失值
wine1=wine.copy(deep=True)
for i in wine1.columns:
    wine1[i]=wine1[i].interpolate(method='linear')
#删除剩余值
wine1=wine1.dropna()

print(wine1.isnull().sum())
wine1.info()

#对比结果
plt.figure()
plt.subplot(121)
sns.set(style="darkgrid")
sns.boxplot(y='points',data=wine)
wine.points.describe()
plt.subplot(122)
sns.set(style="darkgrid")
sns.boxplot(y='points',data=wine1,color='r')
wine1.points.describe()

plt.figure()
wine.price.describe()
plt.subplot(121)
sns.stripplot(y='price',data=wine)
plt.subplot(122)
sns.stripplot(y='price',data=wine1,color='r')
plt.figure()
plt.subplot(121)
sns.distplot(wine.price.dropna())
plt.subplot(122)
sns.distplot(wine1.price.dropna(),color='r')

plt.figure()
plt.subplot(121)
wine['country'].value_counts()[0:15].plot.bar(title='country')
plt.subplot(122)
wine1['country'].value_counts()[0:15].plot.bar(title='country',color='r')
plt.figure()
plt.subplot(121)
wine['province'].value_counts()[0:15].plot.bar(title='province')
plt.subplot(122)
wine1['province'].value_counts()[0:15].plot.bar(title='province',color='r')
plt.figure()
plt.subplot(121)
wine['region_1'].value_counts()[0:15].plot.bar(title='region_1')
plt.subplot(122)
wine1['region_1'].value_counts()[0:15].plot.bar(title='region_1',color='r')
plt.figure()
plt.subplot(121)
wine['region_2'].value_counts()[0:15].plot.bar(title='region_2')
plt.subplot(122)
wine1['region_2'].value_counts()[0:15].plot.bar(title='region_2',color='r')
plt.figure()
plt.subplot(121)
wine['variety'].value_counts()[0:15].plot.bar(title='variety')
plt.subplot(122)
wine1['variety'].value_counts()[0:15].plot.bar(title='variety',color='r')
plt.figure()
plt.subplot(121)
wine['winery'].value_counts()[0:15].plot.bar(title='winery')
plt.subplot(122)
wine1['winery'].value_counts()[0:15].plot.bar(title='winery',color='r')


# ## 4. 通过数据对象之间的相似性来填补缺失值

# In[13]:


#使用最相似数据的填补
wine1=wine.copy(deep=True)
for i in wine1.columns:
    wine1[i]=wine1[i].interpolate(method='nearest')
#删除剩余值
wine1=wine1.dropna()
print(wine1.isnull().sum())
wine1.info()

#对比结果
plt.figure()
plt.subplot(121)
sns.set(style="darkgrid")
sns.boxplot(y='points',data=wine)
wine.points.describe()
plt.subplot(122)
sns.set(style="darkgrid")
sns.boxplot(y='points',data=wine1,color='r')
wine1.points.describe()

plt.figure()
wine.price.describe()
plt.subplot(121)
sns.stripplot(y='price',data=wine)
plt.subplot(122)
sns.stripplot(y='price',data=wine1,color='r')
plt.figure()
plt.subplot(121)
sns.distplot(wine.price.dropna())
plt.subplot(122)
sns.distplot(wine1.price.dropna(),color='r')

plt.figure()
plt.subplot(121)
wine['country'].value_counts()[0:15].plot.bar(title='country')
plt.subplot(122)
wine1['country'].value_counts()[0:15].plot.bar(title='country',color='r')
plt.figure()
plt.subplot(121)
wine['province'].value_counts()[0:15].plot.bar(title='province')
plt.subplot(122)
wine1['province'].value_counts()[0:15].plot.bar(title='province',color='r')
plt.figure()
plt.subplot(121)
wine['region_1'].value_counts()[0:15].plot.bar(title='region_1')
plt.subplot(122)
wine1['region_1'].value_counts()[0:15].plot.bar(title='region_1',color='r')
plt.figure()
plt.subplot(121)
wine['region_2'].value_counts()[0:15].plot.bar(title='region_2')
plt.subplot(122)
wine1['region_2'].value_counts()[0:15].plot.bar(title='region_2',color='r')
plt.figure()
plt.subplot(121)
wine['variety'].value_counts()[0:15].plot.bar(title='variety')
plt.subplot(122)
wine1['variety'].value_counts()[0:15].plot.bar(title='variety',color='r')
plt.figure()
plt.subplot(121)
wine['winery'].value_counts()[0:15].plot.bar(title='winery')
plt.subplot(122)
wine1['winery'].value_counts()[0:15].plot.bar(title='winery',color='r')

