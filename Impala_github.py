#!/usr/bin/env python
# coding: utf-8

# In[1]:


import jaydebeapi
import os


# In[2]:


#provide the required details
url =  'jdbc:impala://<ip>:<port>/default;AuthMech=1;KrbRealm=<Relam>;KrbHostFQDN=<FQDN>;KrbServiceName=<Service>'
driver = 'com.cloudera.impala.jdbc.Driver'


# In[3]:


DIR = os.getcwd() + '/lib/'


# In[4]:


jarFile = [
    DIR + 'ImpalaJDBC42.jar',
]


# In[5]:


conn = jaydebeapi.connect(driver, url, ['', ''], jarFile)


# In[6]:


cursor = conn.cursor()


# In[7]:


sql="SQL"
cursor.execute(sql)
results = cursor.fetchall()


# In[8]:


import pandas as pd


# In[9]:


df = pd.read_sql(sql, conn)


# In[10]:


df.head()


# In[16]:


cursor.close()


# In[17]:


conn.close()


# In[ ]:




