#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


data = pd.read_csv("/Users/sett/Downloads/cost_of_living_us.csv")


# In[4]:


data


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


import seaborn as sns


# In[11]:


plt.plot(data['housing_cost'],data['food_cost'])
plt.title('line chart')
plt.xlabel('housing cost')
plt.ylabel('food cost')


# In[58]:


plt.plot(data['housing_cost'])
plt.plot(data['food_cost'])
plt.title('double line chart')
plt.xlabel('housing_cost')
plt.ylabel('food_cost')


# In[59]:


plt.bar(data['housing_cost'],data['food_cost'])
plt.title("bar plot")
plt.xlabel('housing_cost')
plt.ylabel('food_cost')
plt.show()


# In[73]:


plt.bar(data['housing_cost'],data['food_cost'])
plt.bar(data['areaname'],data['housing_cost'], bottom=data['food_cost'])
plt.title('double bar chart')
plt.xlabel('area name')
plt.ylabel('housing_cost')


# In[ ]:




