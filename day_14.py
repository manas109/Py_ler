# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:17:16 2021

@author: Manaswini Raghavan
"""
us=[10,9,8,7,6,5,4,3,2,1]
for n in range(len(us)-1, 0,):
    for i in range(n):
        if us[i] > us[i + 1]:
              
            us[i],us[i + 1] = us[i + 1], us[i]#Swapping
print(us)

uns=[10,9,8,7,6,5,4,3,2,1]
for i in range (len(uns)):
    for j in range (len(uns)-1):
        if uns[j]>uns[i]:
            uns[i],uns[j]=uns[j],uns[i]#swapping
    print(uns)
