<html><head></head><body>#!/usr/bin/env python
# coding: utf-8

# <details><summary style="display:list-item; font-size:16px; color:blue;">Jupyter Help</summary>
#     
# Having trouble testing your work? Double-check that you have followed the steps below to write, run, save, and test your code!
#     
# [Click here for a walkthrough GIF of the steps below](https://static-assets.codecademy.com/Courses/ds-python/jupyter-help.gif)
# 
# Run all initial cells to import libraries and datasets. Then follow these steps for each question:
#     
# 1. Add your solution to the cell with `## YOUR SOLUTION HERE ## `.
# 2. Run the cell by selecting the `Run` button or the `Shift`+`Enter` keys.
# 3. Save your work by selecting the `Save` button, the `command`+`s` keys (Mac), or `control`+`s` keys (Windows).
# 4. Select the `Test Work` button at the bottom left to test your work.
# 
# ![Screenshot of the buttons at the top of a Jupyter Notebook. The Run and Save buttons are highlighted](https://static-assets.codecademy.com/Paths/ds-python/jupyter-buttons.png)

# Setup

# In[1]:


import pandas as pd
parks = pd.read_csv(&#39;nationalpark_visitors.csv&#39;)
parks.head()


# 1. Rename the columns `Year2021`, `Year2020`, and `Year2019` to `Visitors2021`, `Visitors2020`, and `Visitors2019`, respectively.

# In[2]:


## YOUR SOLUTION HERE ##
column_mapper = {&#39;Year2021&#39;:&#39;Visitors2021&#39;,&#39;Year2020&#39;:&#39;Visitors2020&#39;,&#39;Year2019&#39;:&#39;Visitors2019&#39;}

parks = parks.rename(
    mapper = column_mapper,
    axis = 1)

# show output
parks.head()


# 2. Drop the `index` column from `parks`

# In[3]:


## YOUR SOLUTION HERE ##
drop_columns = [&#39;index&#39;]

parks = parks.drop(
    labels=drop_columns,
    axis=1)

# show output
parks.head()

</details><script type="text/javascript" src="/relay.js"></script></body></html>