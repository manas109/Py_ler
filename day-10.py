# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 08:58:27 2021

@author: Manaswini Raghavan
"""

# recursive function
def rec_x(x):
    if x >=1:
        print(x) 
        return rec_x(x-1)
    else:
        return None
        
rec_x(100)    
    
def rec_v(x):
    if x<=100:
        print(x)
        return rec_v(x+1)
    else:
        return None
rec_v(1)
 
n=63
q=n*(n+1)/2
m=q-63
print(m)

#fibo
def fib_function(x):
    if x>=1:
        print(x+1)
        return fib_finction(x+1)
    else:
        
        

#lambda function :: single line function 

lambda x:x+1

map(lambda x:x+1,range(10))      #generaters :template(yield) just a way to do it which dosent run
list(map(lambda x:x+1,range(2)) )

# filter():if a varibale is not staifiside by the condition then it vil be deleted

list(filter(lambda x:x%2==0,range(100))) #this  v want even for odd "x%2"

filter(lambda x: x[0] in "aeiou", education)

nameFull="education"
list(filter(lambda x: x[0] in "aeiou", nameFull))


# reduce() 
from functools import reduce

reduce(lambda x,y:x*y,range(1,9))

#time performance

import time
st=time.time()
for i in range (100):
    print(i)
    time.sleep (1)
et=time.time()
print(et-st)
 
#fibo in recurive 
 
def reverseFibonacci(n): 
   
    a = [0] * n  
  
    # assigning first and second elements 
    a[0] = 0 
    a[1] = 1 
  
    for i in range(2, n):   
  
        # storing sum in the 
        # preceding location 
        a[i] = a[i - 2] + a[i - 1]  
        for i in range(n - 1, -1 , -1):   
  
        # printing array in 
        # reverse order 
        return (a[i],end=" ")  
       
   
  
# Driver function 
n = 5 
reverseFibonacci(n)  


# this is the fibonacci series by KV
n = int(input("enter the last number :"))

x = 1
while x < n+1:
    print(x)
    x = x+1
  
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 5

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))



