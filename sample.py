#!/usr/bin/env python
# coding: utf-8

# In[1]:


def isprime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
        else:
            return True


# In[2]:


def absolutevaluse(n):
    if n>0:
        return n
    else:
        return n*-1


# In[3]:


def sqrt(n):
    return n**0.5


# In[4]:


def LEN(data):
    c=0
    for i in data:
        c+=1
    return c


# In[ ]:




