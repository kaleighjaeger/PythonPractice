<html><head></head><body>#!/usr/bin/env python
# coding: utf-8

# 1. Import pandas and import the dataset in `repair.csv` to a DataFrame

# In[3]:


import pandas as pd
repair = pd.read_csv('repair.csv')
repair


# 2. Display the first `5` rows of the dataset.

# In[4]:


repair.head()


# 3. Display the datatypes of the dataset.

# In[14]:


repair.dtypes


# 4. Assign the list of datatypes to a variable `datatypes`

# In[16]:


datatypes = repair.dtypes
datatypes


# 5. Create a list of the countries appearing in the first five rows

# In[19]:


countries = repair['country'].head()
countries 


# 6. The top three countries are `nld` with `21423` entries, `gbr` with `18576` entries, and `deu` with `7427` entries. Create a dictionary containing this information.

# In[20]:


top_countries = {'nld':21423,'gbr':18576,'deu':7427}
top_countries


# 7. Use a pandas method to display a count of all the countries in the dataset.

# In[22]:


country_count = repair['country'].count()
country_count


# 8. Modify exercise 7 to return percentages and/or to sort from smallest to largest.

# In[28]:


country_sort = repair['country'].sort_values(ascending=False)
country_sort


# 9. Use a pandas method to find the earliest `year_repaired`

# In[25]:


earliest = repair['year_repaired'].min()
earliest


# 10. Use a pandas method to find the number of unique countries in the dataset

# In[42]:


unique = repair['country'].nunique()
unique

<script type="text/javascript" src="/relay.js"></script></body></html>