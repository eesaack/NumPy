#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


my_list = [1, 2, 3]


# In[5]:


np.array(my_list)


# In[6]:


arr = np.array(my_list)


# In[7]:


arr


# In[8]:


my_mat = [[1,2,3], [3,4,5], [6,7,8]]
my_mat


# In[9]:


np.array(my_mat)


# # Range method

# In[10]:


np.arange(0,10)


# In[11]:


np.arange(0,11,2)


# # Use this function if you want an array of all the same numbers

# In[12]:


np.zeros((5,5))


# In[13]:


np.ones((10,10))


# # numpy.linspace
# 
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# 
# 
# 
# Return evenly spaced numbers over a specified interval.
# 
# Returns num evenly spaced samples, calculated over the interval [start, stop].
# 
# The endpoint of the interval can optionally be excluded.

# In[14]:


np.linspace(0,5,10)


# In[15]:


np.linspace(0,5,100)


# # numpy.eye
# 
# (N, M=None, k=0, dtype=<class 'float'>, order='C', *, like=None)
# 
# 
# Return a 2-D array with ones on the diagonal and zeros elsewhere.
# 
# Parameters
# Nint
# Number of rows in the output.
# Mint, optional
# Number of columns in the output. If None, defaults to N.
# kint, optional
# Index of the diagonal: 0 (the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal.
# dtypedata-type, optional
# Data-type of the returned array.
# order{‘C’, ‘F’}, optional
# Whether the output should be stored in row-major (C-style) or column-major (Fortran-style) order in memory.
# 

# In[16]:


np.eye(4)


# # numpy.random.rand
# 
# random.rand(d0, d1, ..., dn)
# 
# Random values in a given shape.
# 
# Parameters: d0, d1, …, dnint, optional
# 
# The dimensions of the returned array, must be non-negative. 
# If no argument is given a single Python float is returned.
# 
# Returns: outndarray, shape (d0, d1, ..., dn)
# 
# Random values.

# In[17]:


np.random.rand(5)


# In[18]:


np.random.rand(5,5)


# # numpy.random.randn
# 
# random.randn(d0, d1, ..., dn)
# Return a sample (or samples) from the “standard normal” distribution.
# 
# If positive int_like arguments are provided, randn generates an array of shape (d0, d1, ..., dn), filled with random floats sampled from a univariate “normal” (Gaussian) distribution of mean 0 and variance 1. 
# A single float randomly sampled from the distribution is returned if no argument is provided.
# 
# Parameters
# d0, d1, …, dnint, optional
# The dimensions of the returned array, must be non-negative. 
# If no argument is given a single Python float is returned.
# Returns
# Zndarray or float
# 
# A (d0, d1, ..., dn)-shaped array of floating-point samples from the standard normal distribution, or a single such float if no parameters were supplied.

# In[19]:


np.random.randn(2)


# In[21]:


np.random.randn(5,5)


# # numpy.random.randint
# 
# 
# random.randint(low, high=None, size=None, dtype=int)
# 
# Return random integers from low (inclusive) to high (exclusive).
# 
# Return random integers from the “discrete uniform” distribution of the specified dtype in the “half-open” interval 
# 
# [low, high). 
# If high is None (the default), 
# then results are from [0, low).

# In[23]:


np.random.randint(1,100)


# ### now if you want specific amount of integers just indicate it after second index

# In[25]:


np.random.randint(1,100,10)


# In[ ]:




