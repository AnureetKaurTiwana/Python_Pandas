#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd


# # Reading CSV file to binary format using pickle
# Serde Operation: object to byte code converstion in a pickle format is a serialization or write operation in binary format.
# Serialization is write operation to the 

# In[3]:


frame=pd.read_csv("data.csv")
frame
frame.to_pickle("frame_pickle")


# In[4]:


pd.read_pickle("frame_pickle")

using HDF5 format
Hierarchical Data Format (HDF)
It contains multidimensional arrays of scientific data. H5 files are commonly used in aerospace, physics, engineering, finance, academic research, genomics, astronomy, electronics instruments, and medical fields.
# In[ ]:


frame=pd.DataFrame({'a':np.random.randn(100)})
store=pd.HDFStore

