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


# 1. Calculate a 30% discount to the Grand Canyon and assign it to the variable `amount_saved`. 

# In[3]:


## YOUR SOLUTION HERE ##
amount_saved = 80 * 0.30

# show output
amount_saved


# 2. Compute the percent change in visitors to Zion National Park from 2019 to 2020. Assign the percent to the variable `percentchange_2020`.

# In[6]:


## YOUR SOLUTION HERE ##
percentchange_2020 =  (3591254 - 4488268.0) / 4488268.0 * 100

# show output
percentchange_2020


# 3. Round `percentchange_2020` to two decimal places and assign the rounded percent to a new variable `rounded_percent`.

# In[7]:


## YOUR SOLUTION HERE ##
rounded_percent = round(percentchange_2020, 2)

# show output
rounded_percent

</details><script type="text/javascript" src="/relay.js"></script></body></html>