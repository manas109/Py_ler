# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 16:14:32 2021

@author: Manaswini Raghavan
"""
for i in range (10):
    print(("*"*i).ljust(10))
    
for j in range(10):
    for i in range(10):
        print(" * ")
        
        
[[1 for j in range(5)] for i in range(5)]
[1 for j in range(5)]

#list comprenction
[1 if i>2 else 0 for i in range(5)  ]

[1 for m in range(5)for m in range(5)]
[0 if n==0&5 else 1 for n in range(5)]

side=5 #border * and inside 1
for i in range(side):
    for j in range(side):
        if(i==0 or i==side-1 or j==0 or j==side-1):
            print('*', end=' ')
        else:
            print('1',end=' ')
    print()    
  
# hallow       
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()