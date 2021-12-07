# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:34:19 2021

@author: Manaswini Raghavan
"""
print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))

def convert(lst):
    return([i for items in lst for i in items.split()])

lst=[hello world in a frame]
print(convert(list))

print("********")
for i in range(lst):
print("*",list[i],"*")
print("*********")

lst=["hello", "world", "in", "a", "frame"]
print("********")
for i in range(lst):
    print("*",list[i],"*")
    print("*********")
    
import re
mystr="mnasaswni ijoij jhi"
wordList = re.sub("[^\w]","")
mystr.split()

for s in range(3):
    if s %2 == 0: 
        print("Bus")
        continue
    elif s % 3 ==0:
        print("Car")
        continue
    elif s % 4 == 0:
        print("bike")

for fizzbuzz in range(5):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
    
for s in range(11):
    if s / 2 == 0 :
        print("Bus")
    elif s / 3 ==0 and s/4 == 0:
        print("Car")
    else:
        print("bike")