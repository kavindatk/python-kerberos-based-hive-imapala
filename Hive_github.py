#!/usr/bin/env python
# coding: utf-8

# In[6]:


import jaydebeapi
import os


# In[7]:


url = "jdbc:hive2://<ip>:<port>/default;AuthMech=1;KrbRealm=<Relam>;KrbHostFQDN=<FQDN>;KrbServiceName=<service>"
dirver = 'com.cloudera.hive.jdbc41.HS2Driver'


# In[8]:


DIR = os.getcwd() + '/lib/'


# In[9]:


jarFile = [
    DIR + 'HiveJDBC41.jar',
]


# In[10]:


conn = jaydebeapi.connect(dirver, url, ['', ''], jarFile)


# In[11]:


cursor = conn.cursor()


# In[12]:


sql="SQL"
cursor.execute(sql)
results = cursor.fetchall()


# In[13]:


import pandas as pd


# In[14]:


df = pd.read_sql(sql, conn)


# In[15]:


df.head()


# In[16]:


cursor.close()


# In[17]:


conn.close()


# In[ ]:




