# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 09:03:34 2021

@author: Manaswini Raghavan
"""
#triangles 
for i in range(1,11):
    print(' * '*i)
    
n=20
for i in range(1,11):
    print(' '*n, ' ')
    print(' * '*i)
    n-=1
   
n=20
for i in range(1,11):
    print(' '*(n-i) + '* '*(i))
    
for i in range(1,11):
   
    print((' * '*i).ljust(40))
    
num=5
for i in range(1,11):
    print(num,'X', i, '=', num*i)
    
num=9
for i in range(1,11):
     print(num*i,'=', i, 'x', num)
     
num=5 # f format
for i in range(1,11):
    print(f'{num} X {i} = {num*i}') #{} place holders
    
eval() # evaluates od executes an argument
       # build in function
       
    
        