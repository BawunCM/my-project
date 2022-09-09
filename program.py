#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def amountdonated(donated, n):
    
    if n == 0:

        return 0

    if n == 1:

        return donated[0]

    if n == 2:

        return max(donated[0], donated[1])
 

    li = [0]*n
 
    li[0] = donated[0]

    li[1] = max(donated[0], donated[1])

    for i in range(2, n):

        li[i] = max(donated[i]+li[i-2], li[i-1])
 

    return li[-1]
 

input_amount = input("Enter the amounts each family if willing to donate ")
amount = amount.split()
map_object = map(int, list1)
donated = list(map_object)   

 
n = len(donated)

print("Output:{}".

format(amountdonated(donated, n)))


# In[ ]:




