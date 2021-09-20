#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyqrcode
import png
from pyqrcode import QRCode
name = "https://github.com/Gauravkumario"
name_qr = pyqrcode.create(name)
name_qr.svg("name.svg",scale = 10)
name_qr.png("name.png",scale = 10)


# In[ ]:




