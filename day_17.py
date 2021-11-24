# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 17:54:01 2021

@author: Manaswini Raghavan
"""
def fizzBuzz(n):
    #for i in range(1,n+1):
        if i%3==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        elif i%3==0 and i%5==0:
            print("FizzBuzz")
        else:
            print(n)
fizzBuzz(15)

i=6
a,b=[int(i) for i in input().split()]
for i in range(a,b+1):
    if i%3==0 and i%5==0:
        print(f"{i}fizzBuzz",end=" ")
    elif i%3==0:
        print(f"{i}Fizz",end=" ")
    elif i%5==0:
        print(f"{i}Buzz",end=" ")
    else:
        print(i)



def fizz_buzz(i):
    if i%3==0 and i%5==0:
        print("fizzBuzz",end=" ")
    elif i%3==0:
        print("Fizz",end=" ")
    elif i%5==0:
        print("Buzz",end=" ")
    else:
        print(i)
        

