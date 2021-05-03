#!/usr/bin/env python
# coding: utf-8

# In[27]:


#Reading the csv file named detail.csv having detail contents 
import pandas as pd
import numpy as np

df = pd.read_csv(
    'detail.csv', 
    parse_dates=['Absolute Time'], 
    index_col=['Absolute Time']
)

               


# In[37]:


#Downsampling the file to sample/minute
df2 = df.resample('1Min').sum()
df2


# In[36]:


#Creating downsampled csv file for detailcontent
df2.to_csv('detaildownsample.csv')


# In[39]:


import pandas as pd
import numpy as np

df = pd.read_csv('detailvol.csv')
df.head()


# In[40]:


#Reading csv file for detailvol content
import pandas as pd
import numpy as np

df = pd.read_csv(
    'detailvol.csv', 
    parse_dates=['Realtime'], 
    index_col=['Realtime']
)


# In[41]:


#Downsampling to sample per minute
df2 = df.resample('1Min').sum()
df2


# In[42]:


#Creating downsample csv file for detail vol content
df2.to_csv('detailvoldownsample.csv')


# In[43]:


import pandas as pd
import numpy as np

df = pd.read_csv(
    'detailtemp.csv', 
    parse_dates=['Realtime'], 
    index_col=['Realtime']
)


# In[44]:


df2 = df.resample('1Min').sum()
df2


# In[45]:


df2.to_csv('detailTempDownsampled.csv')


# In[ ]:




