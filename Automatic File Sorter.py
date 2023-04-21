#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[73]:


import os, shutil


# In[74]:


path = r"C:/Users/Camron Durrant/OneDrive/Pictures/Test Folder/"


# In[75]:


file_name = os.listdir(path)


# In[83]:


folder_names = ['csv files', 'image files', 'text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])


# In[97]:


for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file )
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file )
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file )
    else:
        print("There are files in this path that were not moved!")
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




