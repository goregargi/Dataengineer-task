#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Data visualization for distributin of the dataset detailvoldownsampled
import pandas as pd
import numpy as np

DataFrame = pd.read_csv('detailvoldownsample.csv')
df = pd.DataFrame(np.random.rand(10,2),columns=['Auxiliary channel TU1 U(V)','Gap of Voltage'])
df.plot.bar()


# In[9]:


#We observe the barplot here for the distribution of the auxillary channel TU1 U(v) and the gap of voltage


# In[15]:


import pandas as pd
import numpy as np

DataFrame = pd.read_csv('detailvoldownsample.csv')
df = pd.DataFrame(np.random.rand(10, 2), columns=['Auxiliary channel TU1 U(V)', 'Gap of Voltage'])
df.plot.box()


# In[20]:


# Here we observe the boxplot of the distribution of the dataset 


# In[22]:


# Scatter plot 

import pandas as pd
import numpy as np

DataFrame = pd.read_csv('detailvoldownsample.csv')
df = pd.DataFrame(np.random.rand(50, 2), columns=['Auxiliary channel TU1 U(V)', 'Gap of Voltage' ])
df.plot.scatter(x='Auxiliary channel TU1 U(V)', y='Gap of Voltage')


#Scattter plot shows the distibution of gap of volatage and the auxiliary channel values the lot shows scattering almost equally for the two columns 


# In[ ]:




