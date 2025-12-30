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


# 1. Calculate the change in visitors from 2019 to 2020 by subtracting `Visitors2019` from `Visitors2020`. Assign the result to a new column `Change2020`.

# In[2]:


## YOUR SOLUTION HERE ##
parks[&#39;Change2020&#39;] = parks[&#39;Visitors2020&#39;] - parks[&#39;Visitors2019&#39;]

# show output
parks[[&#39;Visitors2020&#39;,&#39;Visitors2019&#39;,&#39;Change2020&#39;]].head()


# 2. Create a `PercentChange2020` column by dividing `Change2020` by `Visitors2019` multiplied by `100`.

# In[3]:


## YOUR SOLUTION HERE ##
parks[&#39;PercentChange2020&#39;] = parks[&#39;Change2020&#39;] / parks[&#39;Visitors2019&#39;] * 100
# show output
parks[[&#39;Visitors2020&#39;,&#39;Visitors2019&#39;,&#39;Change2020&#39;,&#39;PercentChange2020&#39;]].head()


# 3. Modify the `PercentChange2020` column by rounding the percent values to `2` decimal places.

# In[10]:


## YOUR SOLUTION HERE ##
parks[&#39;PercentChange2020&#39;] = round(parks[&#39;PercentChange2020&#39;], 2)

# show output - we&#39;ve called .describe() to see an overall picture of the percent change from 2019 to 2020
parks[&#39;PercentChange2020&#39;].describe()

</details><script type="text/javascript" src="/relay.js"></script></body></html>