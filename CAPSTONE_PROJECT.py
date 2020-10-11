#!/usr/bin/env python
# coding: utf-8

# ## Data Analysis
# 
# The data to be used is the one proposed with 252,861 car accidents with the categorization of severity, location and other factors that will guide us for the severity identification of each car accident. Hence dependent variable will be SEVERITYCODE.
# 
# 

# In[33]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[34]:


#Importing Dataset
filepath=r'C:\Users\abel.fernandez.alva1\Desktop\car_severity.csv'
df=pd.read_csv(filepath,low_memory=False)
df.head


# In[35]:


df.info


# In[36]:


#Unique values per column
df.nunique()


# In[37]:


#Missing Values, so we can identify how many are unknown, in order
missing_values=df.isna().sum()
count=df.count()
missing_values/count


# In[38]:


df.describe()


# In[39]:


corr = df.corr()
corr.style.background_gradient(cmap='coolwarm')


# In[40]:


df["ST_COLCODE"] = df["ST_COLCODE"].fillna(df["ST_COLCODE"].mode()[0])
df["UNDERINFL"] = df["UNDERINFL"].fillna(df["UNDERINFL"].mode()[0])
df["X"] = df["X"].fillna(df["X"].median())
df["Y"] = df["Y"].fillna(df["Y"].median())
df["LIGHTCOND"] = df["LIGHTCOND"].fillna(df["LIGHTCOND"].mode()[0])
df = df.drop(["SDOTCOLNUM","INTKEY","COLDETKEY","SEVERITYCODE.1","SPEEDING" ,"EXCEPTRSNDESC","PEDROWNOTGRNT","INATTENTIONIND","EXCEPTRSNCODE","LOCATION","INCDATE","INCDTTM","OBJECTID","REPORTNO","SDOT_COLDESC","ST_COLDESC","ST_COLCODE","SEVERITYDESC"], axis=1)
df.info()


# In[42]:


df.describe()


# In[43]:


#Making a list of all categorical variables, so it can be easy to identify when working with them
clmn = {"STATUS","ADDRTYPE","COLLISIONTYPE","JUNCTIONTYPE","UNDERINFL","WEATHER","ROADCOND","LIGHTCOND","HITPARKEDCAR"}

#Converting them into dummy variables
df = pd.get_dummies(data=df,columns=clmn,prefix=clmn)


# In[46]:


X = df.drop(["SEVERITYCODE"],axis=1)
y = df["SEVERITYCODE"]


# In[ ]:




