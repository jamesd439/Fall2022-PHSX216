#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def fred(a,b):
    c = (a+b)*12 
    return c

a = 13.2
b = 3.9
c = fred(a,b)

print('c = ',c)


# In[3]:


import numpy as np

def rule3(dA, dB):
    dQ = np.sqrt(dA**2+dB**2)
    return dQ

dA = 1.4 
dB = 2.1

dQ = rule3(dA,dB)
print(dQ)


# In[8]:


import numpy as np

x = np.array([1,1.1,1.2,0.9,0.85])
y = x*3
print(y)
ysq = y**2
print(ysq)

err_x = np.std(x)/np.sqrt(5)
avgx = np.average(x)
print(avgx,err_x)


# #This is so fun

# $ delta F = g\delta m$

# $\delta Q = \sqrt{(\delta A)^2 + (\delta B)^2}$

# $\frac{\delta A}{A}$

# #Everything below is part of the assignment!

# $\delta Q = c * \delta A$
# 
# $\delta V_i = \sqrt{(\frac{\delta X} {X})^2 + (\frac{\delta 2Y} {2Y}})^2$
# 
# $\delta Q = \sqrt{(\delta A)^2 + (\delta B)^2}$

# In[26]:


import numpy as np
def rule1(c, dA):
    dQ = (c * dA)
    return dQ

c = 15
dA = 12
dQ = rule1(c, dA)
print(dQ)
    


# In[27]:


def rule2(c, m, A, dA):
    dQ = c * m * (A**(m-1)) * dA
    return dQ
c = 1
m = 2
A = 5
dA = 10
dQ = rule2(c, m, A, dA)
print(dQ)


# In[28]:


import numpy as np

def rule3(dA, dB):
    dQ = np.sqrt(dA**2+dB**2)
    return dQ

dA = 2.5 
dB = 3.7

dQ = rule3(dA,dB)
print(dQ)


# In[30]:


def rule4(m, dA, A, n, dB, B):
    dQ = np.sqrt(((m * dA)/(A))** 2 + ((n * dB)/(B))**2)
    return dQ
m = 4
dA = 4
A = 5
n = 6.7
dB = 7.5
B = 2
dQ = rule4(m, dA, A, n, dB, B)
print(dQ)


# In[34]:


import numpy as np

x = np.array([1.1, 1.3, 1.4, 0.9, 0.95, 1.05])
avg = np.average(x)
std = np.std(x)
print(f'The average of the data is {avg} and the standard deviation is {std}')


# In[ ]:




