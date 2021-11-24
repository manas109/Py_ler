# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:26:35 2021

@author: Manaswini Raghavan
"""
txt=input('enter a sitring')
print(txt)
a=txt.upper()
alphabet_txt = txt.ascii_Uppercase


import my_txt
a = 'aabbbccccddddeeeeeeeeeeeeeeevvvvvvv'

#b = 'this is python coding class at 9am class'
#a = b.split()


a = 'aabbbccccddddeeeeeeeeeeeeeeevvvvvvv'
d = dict()
for i in set(a):
    print(i,'-->',a.count(i))
    d[i]=a.count(i)
print(d)


{i:a.count(i) for i in set(a)}


a = 'bbbccccddddeeeeeeeeeeeeeeevvvvvvv'
for i in set(a):
    print(i,'--->',a.count(i))
    d=a.count(i)
print(d)