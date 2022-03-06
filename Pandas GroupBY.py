#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


Reading Excel File


# In[23]:


df = pd.read_excel("C://Users//hp//Downloads//Student.xls",sheet_name="Student Survey")
df


# In[31]:


df.describe()


# In[32]:


type(df.describe()) #its a dataframe so all df functions are applicable here


# In[33]:


df2=df.describe()


# In[37]:


type(df2.loc["count"]) #its a series so can be used as series


# In[43]:


sr=df2.loc["count"]
sr


# In[41]:


sr['Age']


# In[46]:


df3=df.groupby("Store Setting").describe()
df3


# In[51]:


#df3.T or
trans=df3.transpose()
trans


# In[54]:


type(trans.loc["Age"])


# In[55]:


trans.loc["Age"].loc['count']


# # Concatenate
# df.concat(name1,name2,name3....)

# In[75]:


name1=pd.DataFrame({'A':[0,1,1],'B':[2,2,2],'C':[1,0,1]})
name1


# In[76]:


name2=pd.DataFrame({'A':[0,0,0],'B':[2,2,2]})
name2


# In[78]:


pd.concat([name1,name2])


# In[79]:


pd.concat([name1,name2],axis=1)


# In[81]:


pd.merge(left=name1,right=name2,how="inner",on="A")


# # Merge join the column keys 
# and Join use the indices

# In[83]:


pd.merge(left=name1,right=name2,how="left",on="A")


# In[107]:


df1=pd.DataFrame({'Key':[1,2,3,4],'A':[0,2,3,3],'B':[0,9,9,9]})
df1


# In[86]:


df2=pd.DataFrame({'Key':[0,2,3,8],'X':[0,2,3,3],'Y':[0,9,9,9]})
df2


# In[90]:


df4=pd.concat([df1,df2])
df4


# In[91]:


df4.fillna('Empty')


# In[93]:


df5=pd.merge(df1,df2,on='Key')#by default inner
df5


# In[94]:


df5=pd.merge(df1,df2,on='Key',how="outer")#by default inner
df5


# In[101]:


#df1.join(df2)


# In[105]:


def s(x):
    if x==0:
        return 100
    else:
        return x*10


# # df.apply(outer function name)

# In[111]:


result=df1['A'].apply(s)


# In[110]:


df1


# In[114]:


df1['result']=result
df1


# In[115]:


df1['lambda']=df1['A'].apply(lambda x: np.sqrt(x))
df1


# In[159]:


df=pd.read_csv("https://raw.githubusercontent.com/PramodShenoy/911-Calls/master/911.csv")
df


# In[142]:


df.describe()


# In[143]:


df[["title","twp"]].describe()


# # Typecast latitude to integer then perform 

# In[161]:


df["lat"]=df["lat"].astype(int)


# In[163]:


df.groupby("lat").count()


# # How many people are from same zip location

# In[171]:


df.groupby("zip")["twp"].describe()


# In[172]:


df.groupby("zip")["twp"]


# # Extract Date from timestamp

# In[179]:


df["timeStamp"].dtype


# In[202]:


import datetime as dt

df["timeStamp"] = df["timeStamp"].apply(lambda x : pd.to_datetime(str(x)))

df['dates'] = df["timeStamp"].dt.date


# In[203]:


df


# # Extract a zip where addr starts with A

# In[209]:


df["addr"]=df["addr"].astype(str)


# In[210]:


df["addr"].dtype


# In[213]:


def s(df):
    if df["addr"]=="%A%":
        df["zip"]
    


# In[214]:


df["result"]=df.apply(s)


# In[ ]:




