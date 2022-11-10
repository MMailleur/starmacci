
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd 


# In[8]:


def urlname(str):
    url = requests.get("https://swapi.dev/api/" + str)
    return url 


# In[9]:


urlname("people")


# In[14]:


def json(url) :
    json_data = url.json()
    return json_data


# In[18]:


json(urlname("people"))


# In[19]:


def todataframe(json_data):
    pd_data = pd.DataFrame(json_data)
    return pd_data


# In[20]:


todataframe(json(urlname("people")))


# In[ ]:

def planets():
    data= todataframe(json(urlname("planets"))['results'])
    return data



