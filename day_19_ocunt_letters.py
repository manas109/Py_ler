# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:11:23 2021

@author: Manaswini Raghavan
"""
a='aaccbyyeeqab' # this is urs which do give accurate results
count=1
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count+=1
    else:
        print(a[i],count)
        count=1
        
# 1 way     
a='aaabbccccddde'
for i in set(a):
    print(i,'--->',a.count(i))
    """
    a is s string
    I hv used count(), this is one way to do 
    
    """
    d=a.count(i)
    """
    d is just a variable i hv assigned to print the value
    """
print(d)

# 2nd way 

{i:a.count(i) for i in set(a)}
"""
 this is a way where dictionary is used in more opptimised way
"""

#3rd way same as 2nd but more ellebrated 
a = 'aabbbccccddddeeeeeeeeeeeeeeevvvvvvv'
d = dict()
for i in set(a):
    print(i,'-->',a.count(i))
    d[i]=a.count(i)
print(d)

a='aaccbyyeeqab'
output=''
previous=a[0]
c=1
i=1
while i<len(a):
    if a[i]==previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=a[i]
        c=c+1
    if i==len(a)-1:
        output=output+str(c)+previous
    i=i+1
print(output)
    