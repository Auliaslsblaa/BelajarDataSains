#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file = 'https://raw.githubusercontent.com/alamhanz/pandas_journey/main/mydata/food_delivery_datasets.csv' # merujuk link data csv
dataset = pd.read_csv(file, sep=',') #membuka data csv
dataset.head()


# In[52]:


#ID CUSTOMER DENGAN ORDER TERBANYAK


# In[44]:


data1=dataset[['date_time', 'cust_id']] #menampilkan data yang diperlukan
data1.head()


# In[45]:


data1.isna().sum() #menghitung missing value


# In[46]:


df_cust_id = data1[data1['cust_id']>0] #filter data customer 
df_cust_id.head()


# In[48]:


df_cust_id['cust_id'].mode() #mencari customer dengan order terbanyak


# In[53]:


#Menghitung Biaya Kirim per waktu pengiriman


# In[54]:


data2=dataset[['eta_seconds', 'delivery_fee']] #menampilkan data yang diperlukan
data2.head()


# In[55]:


data2.isna().sum() #menghitung missing value


# In[57]:


data2.describe() #statistika deskriptif data


# In[60]:


mean_eta_seconds=data2['eta_seconds'].mean() #menghitung rata rata waktu pengiriman


# In[62]:


mean_delivery_fee=data2['delivery_fee'].mean() #menghitung rata rata ongkos kirim


# In[64]:


mean_delivery_fee/mean_eta_seconds

