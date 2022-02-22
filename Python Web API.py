#!/usr/bin/env python
# coding: utf-8

# API Application programming interface
# It is a connection between computers or between computer programs. It is a type of software interface, offering a service to other pieces of software
# ![image.png](attachment:image.png)

# In[6]:


import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)

#code 200 means this request is giving the response


# In[3]:


type(resp)


# In[8]:


data = resp.json()
data


# In[9]:



data[2]['user']['id']


# In[11]:


import pandas as pd 
issues = pd.DataFrame(data)
issues.head()


# In[ ]:




