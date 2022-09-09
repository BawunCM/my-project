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
 

    list = [0]*n
 
    list[0] = donated[0]

    list[1] = max(donated[0], donated[1])

    for i in range(2, n):

        list[i] = max(donated[i]+list[i-2], list[i-1])
 

    return list[-1]
 

input_amount = input("Enter the amounts each family if willing to donate for the cause")
amount = amount.split()
map_object = map(int, list1)
donated = list(map_object)   

 
n = len(donated)

print("The Output collected from families:{}".

format(amountdonated(donated, n)))




# In[ ]:




