
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


# In[25]:

def fonctionfinale(str) :
    dataf = todataframe(json(urlname(str)))
    return dataf























































# Species
urlname("species")
def json(species) :
    json_data = species.json()
    return json_data
json(urlname("species"))
def todataframe(json_data):
    pd_data = pd.DataFrame(json_data)
    return pd_data
todataframe(json(urlname("species")))
def species():
df_species = todataframe(json(urlname("species"))['results'])
return data
