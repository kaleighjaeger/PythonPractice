<html><head></head><body>#!/usr/bin/env python
# coding: utf-8

# # Explore Laptop Repair Data
# 
# - [View Solution Notebook](./solution.html)
# - [View Project Page](https://www.codecademy.com/projects/practice/explore-laptop-repair-data-with-python)

# ## Task Group 1 -  Import and Inspect

# ### Task 1 
# 
# Import `pandas` using the alias `pd`.

# In[2]:


import pandas as pd


# ### Task 2
# 
# Import the dataset in `laptops.csv` and assign to the variable `laptops`.

# In[3]:


laptops = pd.read_csv(&#39;laptops.csv&#39;)


# ### Task 3
# 
# Display the first five lines of the `laptops` DataFrame.

# In[4]:


laptops.head()


# ### Task 4
# 
# Display the data types of the `laptops` DataFrame columns.

# In[5]:


laptops.dtypes


# ## Task Group 2 -  Explore Numeric Columns

# ### Task 5
# 
# Let&#39;s take a look at the ages of laptops being brought in for repair. Use a series method to display the minimum, maximum, and other summary statistics for the `age` column. Do you notice anything interesting?

# In[6]:


laptops[&#39;age&#39;].describe()


# ### Task 6
# 
# The other numeric column is `event_year`. Use a pandas method to determine the earliest and latest years in the dataset.

# In[11]:


laptops[&#39;event_year&#39;].min()
laptops[&#39;event_year&#39;].max()


# ## Task Group 3 - Explore Categorical Columns

# ### Task 7
# 
# Let&#39;s also take a look at `event_year` as a categorical column. Use a series method to output the number of laptops in the data for each `event_year`. What do you notice?

# In[12]:


laptops[&#39;event_year&#39;].value_counts(ascending=True)


# ### Task 8
# 
# Now, let&#39;s focus on the problems causing people to bring in laptops for repair. Use a series method to display the most common problems in the dataset. What do you notice?

# In[13]:


laptops[&#39;problem&#39;].value_counts(ascending=True)


# ### Task 9
# 
# Power and battery issues are pretty common, but what percentage of the data do they represent? Modify the method from the previous task to output percentages instead of counts.

# In[14]:


laptops[&#39;problem&#39;].value_counts(ascending=True,normalize=True)


# ### Task 10
# 
# Lastly, let&#39;s look at how often laptops brought into these events are recorded as fixed. Use a pandas method to count the number of laptops in each category of `repair_status`.

# In[18]:


laptops[&#39;repair_status&#39;].value_counts()

<script type="text/javascript" src="/relay.js"></script></body></html>