# Login Kerberos Based Hive & Impala cluster using Python

<picture>
  <img alt="kerberos logo" src="https://miro.medium.com/v2/resize:fit:1006/1*agsHkPjE9N5uC-HkrUW9mg.png" width="300" height="150">
</picture>


<picture>
  <img alt="hive and impala logo" src="https://miro.medium.com/v2/resize:fit:819/1*EUfJs-gRAsUcrkJ7giXgww.png" width="300" height="150">
</picture>

<picture>
  <img alt="pythonlogo" src="https://miro.medium.com/v2/resize:fit:1358/1*RzxZF0mmXAsMLrIzAWYDSg.png" width="300" height="150">
</picture>





In this article, I am explaining how to log in and extract data from a Kerberos-based authenticated Hive/Impala cluster using Python. Before we move further, I would like to mention the tools I am going to use for this tutorial. To extract data from the Hive/Impala cluster, I am using Jupyter Notebook, MIT Kerberos authentication tool, and Cloudera JDBC drivers. I have provided the required links below. The first step is to obtain Kerberos tickets using MIT Kerberos authentication software

  1. Jupyter Notebook (https://www.anaconda.com/download)
  2. MIT Kerberos Tool (https://web.mit.edu/kerberos/dist/)
  3. Cloudera JDBC driver (https://www.cloudera.com/downloads.html)


## Code 

#### Import required libraries 

```python
import jaydebeapi
import os
import pandas as pd
````
#### Define Driver and Url

```python
url =  'jdbc:impala://<ip>:<port>/default;AuthMech=1;KrbRealm=<Relam>;KrbHostFQDN=<FQDN>;KrbServiceName=<Service>'
driver = 'com.cloudera.impala.jdbc.Driver'


DIR = os.getcwd() + '/lib/'

jarFile = [
    DIR + 'ImpalaJDBC42.jar',
]
```

#### Connect to Cluster 

```python
conn = jaydebeapi.connect(driver, url, ['', ''], jarFile)

#Open curser for fetch data

cursor = conn.cursor()

sql="SQL Code"
cursor.execute(sql)
results = cursor.fetchall()

#Convert output to Pandas dataframe

df = pd.read_sql(sql, conn)

#Print top 10

df.head(10)

```

#### Close connection

```python
cursor.close()
conn.close()

```
