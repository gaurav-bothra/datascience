#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


df = pd.DataFrame()


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[80]:


img = cv2.imread('output9_par.jpg', 0)


# In[104]:


img = cv2.resize(img, (1024,1224))


# In[105]:


plt.imshow(img, cmap='gray')


# In[106]:


text = pytesseract.image_to_string(img)


# In[107]:


l = text.split('\n')


# In[108]:


for i in l:
    if i == '':
        l.remove(i)


# In[109]:


s = "\n".join(l[0:])
print(s)


# In[110]:


para = s.split(" ")


# In[111]:


d = {}


# In[112]:


for i in range (len(para)):
    if para[i] in d.keys():
        newList  = d[para[i]]
        newList.append(i)
        d[para[i]] = newList
    else:
        d[para[i]] = [i]


# In[116]:


d


# In[115]:


for i in d["Time"]:
    if para[i] == "Time":
        print(True)
    else:
        print(False)

