#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Reading the excel files and creating the dataframe 
import pandas as pd
df1 = pd.read_excel("data.xlsx", "Detail_67_1_1")
df2 = pd.read_excel("data.xlsx","Detail_67_1_1_1")


# In[14]:


df3 = pd.read_excel("data.xlsx","Detail_67_1_1_2")
df4 = pd.read_excel("data.xlsx","Detail_67_1_1_3")
df5 = pd.read_excel("data.xlsx","Detail_67_1_1_4")
df6 = pd.read_excel("data.xlsx","Detail_67_1_1_5")
df7 = pd.read_excel("data.xlsx","Detail_67_1_1_6")


# In[17]:


#Combining all the contents of detail 
pdList = [df1,df2,df3,df4,df5,df6,df7]
df_detail = pd.concat(pdList)
df_detail


# In[18]:


#Creating csv file with contents of detail
df_detail.to_csv('detail.csv')


# In[19]:


#Reading excel files and creating dataframe for contents of detailvol
import pandas as pd
df8 = pd.read_excel("data.xlsx", "DetailVol_67_1_1")
df9 = pd.read_excel("data.xlsx", "DetailVol_67_1_1_1")
df10= pd.read_excel("data.xlsx", "DetailVol_67_1_1_2")
df11= pd.read_excel("data.xlsx", "DetailVol_67_1_1_3")
df12= pd.read_excel("data.xlsx", "DetailVol_67_1_1_4")
df13= pd.read_excel("data.xlsx", "DetailVol_67_1_1_5")
df14= pd.read_excel("data.xlsx", "DetailVol_67_1_1_6")


# In[21]:


#Combining contents of detailvol by combining dataframes
pdList2 = [df8,df9,df10,df11,df12,df13,df14]
dfvol = pd.concat(pdList2) 


# In[22]:


#Creating csv file for the contents of detail vol
dfvol.to_csv('detailvol.csv')


# In[24]:


#Reading excel files and creating dataframe for detailtemp content
df15 = pd.read_excel("data_1.xlsx", "DetailTemp_67_1_1_3")
df16 = pd.read_excel("data_1.xlsx", "DetailTemp_67_1_1_4")
df17 = pd.read_excel("data_1.xlsx", "DetailTemp_67_1_1_5")
df18 = pd.read_excel("data_1.xlsx", "DetailTemp_67_1_1_6")
df19 = pd.read_excel("data.xlsx", "DetailTemp_67_1_1")
df20 = pd.read_excel("data.xlsx", "DetailTemp_67_1_1_1")
df30 = pd.read_excel("data.xlsx", "DetailTemp_67_1_1_2")


# In[25]:


#Combining detailtemp content from excel files
pdList3 = [df15,df16,df17,df18,df19,df20,df30]
dftemp = pd.concat(pdList3) 


# In[26]:


dftemp.to_csv('detailtemp.csv')


# In[ ]:




