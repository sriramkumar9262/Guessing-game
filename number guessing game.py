#!/usr/bin/env python
# coding: utf-8

# ## guessing number game
# 

# In[2]:


import random
n=random.randrange(1,100)
guess=int(input("Enter the number:"))
while n!=guess:
    if n>guess:
        print("the number is too low ")
        guess=int(input("enter the number again"))
    elif n<guess:
        print("the number is too high")
        guess=int(input("enter the number again"))
    else:
        break
print("the number you guess is right and n is {}".format(n))


# In[ ]:





# In[ ]:




