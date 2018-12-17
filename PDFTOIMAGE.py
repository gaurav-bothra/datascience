#!/usr/bin/env python
# coding: utf-8

# In[6]:


from pdf2image import convert_from_path
pages = convert_from_path('ast_sci_data_tables_sample.pdf', 500)


# In[7]:


count = 0
for page in pages:
    page.save("out{no}.jpg".format(no=count), 'JPEG')
    count=count+1

