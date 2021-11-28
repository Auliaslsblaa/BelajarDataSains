#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[44]:


file='E:\\SEMESTER V\\Data Sains\\shades.csv'
dataset=pd.read_csv(file)
dataset.head()


# In[6]:


#Mencari Merk dan produk yang memiliki penjualan terbanyak (BEST SELLER)


# In[13]:


data1=dataset[['brand', 'product']] #menampilkan data yang diperlukan
data1.head()


# In[14]:


data1.isna().sum() #menghitung missing value


# In[16]:


data1.describe() #statistika deskriptif data


# In[17]:


import statistics


# In[45]:


data1_GROUPBY_brand = data1.groupby("brand")


# In[46]:


data1_GROUPBY_brand["brand"].count()


# In[36]:


data1_GROUPBY_product = data1.groupby("product")


# In[37]:


data1_GROUPBY_product["product"].count()


# In[39]:


data1_GROUPBY_brand_product = data1.groupby(["brand", "product"])


# In[40]:


data1_GROUPBY_brand_product["product"].count()


# In[ ]:





# In[ ]:




