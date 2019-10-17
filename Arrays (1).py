#!/usr/bin/env python
# coding: utf-8

# In[10]:


## Python does not have a native array data sctucture
## However, it does have the list, which is much more general and can be used as a multidimensional array
## The List in Python is an ordered collection of items which can be of any type


# In[11]:


numbers = [10, 20, 30, 40, 50]


# In[12]:


# random indexing --> O(1) get items we know the index for


# In[13]:


print(numbers[4])


# In[14]:


# We iterated through the list as such
numbers[1] = 200
print(numbers[1])


# In[16]:


# iterate through a given 1 dimensional array
for num in numbers:
    print(num)


# In[18]:


# update the second item to a string
numbers[1] = 'Adam'


# In[19]:


numbers


# In[20]:


# we are not able to store multiple data types in Java or C++ as we can in Python


# In[21]:


# the below works the same as the for loop above
for i in range (len(numbers)):
    print(numbers[i])


# In[24]:


# use semicolun operator to print out just the first two items in list
print(numbers[0:2])


# In[25]:


# print out all items
print(numbers[:])


# In[26]:


# print out all but the last item
print(numbers[:-1])


# In[31]:


# find the maximum

# O(N) search running time / linear time complexity

numbers = [10, 20, 300, 40, 50]

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
            
print(maximum)


# In[33]:


# Binary Search Trees have O(logN) time complexity
# Associative Arrays such as dictionaries have 0(1) time complexity - constant time complexity


# In[ ]:




