#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install chart-studio


# In[4]:


pip install cufflinks


# In[34]:


import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot,plot
init_notebook_mode(connected=True) 


# In[35]:


import pandas as pd


# In[36]:


covid_data = pd.read_csv('05-22-2020.csv')


# In[37]:


covid_data.head(60)


# In[38]:


ABV = ["AL", "AK", "AS","AZ", "AR", "CA", "CO", "CT",  "DE", "DP", "DC","FL", "GA", "GP", "GM",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND","NI", "OH", "OK", "OR", "PA", "PR" , "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT","VI", "VA", "WA", "WV", "WI", "WY"]


# In[39]:


covid_data['ABV'] = ABV


# In[40]:


covid_data.head()


# In[113]:


data = dict(
        type = 'choropleth',
        colorscale = 'reds',
        locations = covid_data['ABV'],
        locationmode = 'USA-states',
        reversescale = False,
        z = covid_data['Confirmed'],
        marker = dict(line = dict(color = 'rgb(12,12,12)',width = 3)),
        text = covid_data['Province_State'],
        colorbar = {'title' : 'Confirmed'},
        
      ) 

layout = dict(title = 'Confirmed Covid-19 Cases', 
                geo = dict(scope = 'usa')
             )


# In[114]:


choromap = go.Figure(data = [data],layout = layout)


# In[115]:


plot(choromap)


# In[79]:


pip install Pillow


# In[80]:


from PIL import Image 


# In[81]:


pip install opencv-python


# In[82]:


pip install matplotlib


# In[116]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[117]:


image = cv2.imread('Covid19_choropleth.png')


# In[118]:


print('Image type: ', type(image),
      'Image Dimensions : ', image.shape)


# In[119]:


image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
plt.imshow(image_copy)


# In[120]:


white = np.array([255, 255, 255])
white2 = np.array([255, 255, 255])


# In[121]:


mask = cv2.inRange(image_copy,white,white2)
plt.imshow(mask, cmap = 'gray')


# In[122]:


masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]
plt.imshow(masked_image)


# In[123]:


background_image = cv2.imread('coronavirus-CDCimage.png')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

crop_background = background_image[0:450, 0:700]

crop_background[mask == 0] = [0, 0, 0]

plt.imshow(crop_background)


# In[124]:


final_image = crop_background + masked_image
plt.imshow(final_image)


# In[ ]:




