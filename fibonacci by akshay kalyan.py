#!/usr/bin/env python
# coding: utf-8

# In[8]:

n=int(input('enter a number upto which you want fibonacci sequence '))
i=0
j=1
print(i)
print(j)
print(j)

while i+j<=n: 
    k=(i+j) 
    i=j
    j=k
    
    print(i+j)
