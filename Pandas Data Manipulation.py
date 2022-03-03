#!/usr/bin/env python
# coding: utf-8

# # Pandas Data Manipulation

# In[1]:


import os


# In[2]:


# get the current working directory
os.getcwd()


# In[3]:


#change current working directory
#os.chdir('C:\\Users\\Dell\\Desktop')


# In[4]:


# list down all objects in the current working directory
os.listdir()


# In[5]:


import pandas as pd


# In[6]:


# Go to http://www.basketball-reference.com/leagues/NBA_2015_totals.html
# click the CSV button and then copy some data to the clipboard

#BB_reference_data = pd.read_clipboard(sep=",")  # Read data from the clipboard

#BB_reference_data.ix[:, 0:10].head(5)   # Check 5 rows (10 columns only)


# In[7]:


url = "http://www.basketball-reference.com/leagues/NBA_2015_totals.html"

BB_data = pd.read_html(url)         # Read data from the specified url

df=BB_data[0].iloc[0:5,0:10]     
df# Check 5 rows (10 columns only)


# In[8]:


type(BB_data)


# In[9]:


type(df)


# In[10]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


type(df)


# In[12]:


df.dtypes


# In[13]:


df.describe()


# In[14]:


df2=pd.read_csv("dailyActivity_merged.csv")
df2.dtypes


# In[15]:


type(df2)


# In[16]:


ix=df2.dtypes[df2.dtypes=="object"].index
ix


# # Describe Numerical Data

# In[17]:


discribedDF=df2.describe() #store decsribed values into a dataframe


# In[18]:


discribedDF


# # Describe Object Data

# In[19]:


df2[ix].describe()


# # Selection operation on dataframe
# Data can be fetched from the series same as from the list

# In[20]:


df2.columns


# In[21]:


df2[['Id','TotalSteps']]


# In[22]:


df2[['TotalSteps','Id']][0:10:2]
#[start index:end index:step]


# # Select the data present on even indices in one particular column

# In[23]:


df3=df2['Id'][0::2]
df3


# In[24]:


sorted(df2['Id'][0:10:2])


# In[25]:


df3.sort_values()


# # Adding New Column to a dataframe

# In[26]:


#int is not scriptale hence astype used to data type casting, New column is added to the datframe
result=[i[0] for i in df2['Id'].astype(str)]
df2['result']=result
df2


# # Selecting Rows in dataframe using following functions
# 1. loc= named locations of the row
# 2. iloc= integer location i.e default indices of the row
# 3. ix

# In[27]:


df2.iloc[[0,1],[2,3]]#row default indices followed by column indices


# In[28]:


df2.loc[[0,1],['ActivityDate']]#row default indices followed by column indices


# In[29]:


df2.iloc[[0],[-2]]


# In[30]:


import numpy as np
#where attribute in numpy returns indices
np.where(df2['TotalDistance']==max(df2['TotalDistance']))


# In[31]:


df2.loc[np.where(df2['TotalDistance']==max(df2['TotalDistance']))]


# In[32]:


li=[1,2,3,4]
di={1:'a',2:'b',3:'c'}
se=pd.Series(li)
se


# In[33]:


se=pd.Series(li,index=['a','b','c','d'])
se


# In[34]:


se[0]


# In[35]:


se1=pd.Series(di)
se1
#Keys are considered row indices and values as the row values


# In[36]:


df=pd.DataFrame(di,li) #its must to provide the index when dictionary is passed in dataframe
df
#list is the index values and the key and value is the column name and cell value respec


# In[37]:


pwd()


# # Check if the directory has pdf then select its name and read the pdf

# In[38]:


import os
os.chdir("C:\\Users\\hp\\Downloads\\Parent\\Child1")
li=os.listdir()
print(li)
pdf=[]
for i in li:
    print(i,sep='\n')
    if(i.endswith('pdf')):
        pdf.append(i)
      
pdf


# In[39]:


pip install PyPDF2


# In[40]:


import PyPDF2


# In[41]:


from PyPDF2 import PdfFileReader


# In[42]:


# Initilizing Object :

reader = PdfFileReader("C:\\Users\\hp\\Downloads\\Parent\\Child1\\Direction Sense Test.pdf")
# Printing Number of Pages in PDF File :

print("Number of Pages :  ", reader.getNumPages())

print("------------------------------------------")


# In[43]:


# Reading the file :

pages = reader.getNumPages()

for i in range(0, pages):
    print("Page Number : ", i+1)

    print("------------------------------------------")

    pageObj = reader.getPage(i)

    print(pageObj.extractText())


# # How to read docx file

# In[44]:


pip install docx


# In[45]:



from docx import opendocx, getdocumenttext


# In[ ]:


li=os.listdir()
print(li)

for i in li:
    print(i,sep='\n')
    if(i.endswith('docx')):
        doc=i
      
doc


# In[ ]:


from cStringIO import StringIO
def document_to_text(filename, file_path):
    cmd = ['antiword', file_path]
    p = Popen(cmd, stdout=PIPE)
    stdout, stderr = p.communicate()
    return stdout.decode('ascii', 'ignore')

print document_to_text(doc,'C:\\Users\\hp\\Downloads\\Parent\\Child1\\'+doc)


# In[ ]:


pwd()


# # Drop a row and column
# drop(names index only/no default index)
# drop(name) #by default axis=0 i.e Row it will drop, inplace=False so the chnage will not be permanent in the dataframe
# drop(column name, axis=1,inplace=True) #permanent chnage in dataframe, column is dropped

# In[ ]:


df


# In[ ]:


df.drop(1) #row is dropped


# In[ ]:


df.drop(1,axis=1) #column is dropped


# In[ ]:


df.drop(1,axis=1,inplace=True) #column is dropped permanently


# In[ ]:


df


# In[ ]:


matrix_data=np.matrix('10,12,14;11,12,50;11,2,22')
row_labels=['r1','r2','r3']
col_labels=['age','id','marks']
matrix_data


# In[ ]:


df=pd.DataFrame(matrix_data,row_labels,col_labels)
df


# In[ ]:


df[df['age']<11]


# # Set index, reset index, using a column as an index column in the dataframe
# 1. reset_index(....,drop=True,inplace=True) #drop=True will drop the old index, inplace=True will make changes in the original dataframe
# 2. set_index(column name)
# 3. split will split string into a list
# 

# In[ ]:


name="anu money karamjeet"
name=name.split()
name


# In[ ]:


df['name']=name


# In[ ]:


df


# In[ ]:


df.reset_index()


# In[ ]:


df.reset_index(drop=True,inplace=True)
df


# In[ ]:


df.set_index('name',inplace=True)
df


# # Multi Indexing

# In[52]:


outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
higher_index=list(zip(outside,inside))
print("tuple pair after zip","\n","-"*45)
higher_index


# In[53]:


higher_index=pd.MultiIndex.from_tuples(higher_index)
higher_index


# In[54]:


import random
df1=pd.DataFrame(data=random.random(),index=higher_index,columns=['A','B','C'])
df1


# In[67]:


df1.loc['G1'].iloc[[0],[0,2]]


# In[64]:


outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
inside2=['a','b','c','d','e','f']
higher_index2=list(zip(outside,inside,inside2))


# In[65]:


higher_index2=pd.MultiIndex.from_tuples(higher_index2)
higher_index2


# In[66]:


df2=pd.DataFrame(data=random.random(),index=higher_index2,columns=['A','B','C'])
df2


# In[69]:


df3=pd.DataFrame({'A':[1,np.nan,2,3],'B':[0,4,np.nan,0],'C':[np.nan,np.nan,9,0]})
df3


# In[71]:


df3.dropna(axis=0)


# In[73]:


df3.dropna(thresh=3) #keep the rows with atleast 3 non nan values


# In[ ]:




