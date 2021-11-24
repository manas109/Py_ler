# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:07:54 2021

@author: Manaswini Raghavan
"""
ppl=list(range(1,101))
print("list of 100 ppl")
print(ppl)
del ppl[1::2]
print("remaining ppl after one round of killing")
print(ppl)
ppl_00=ppl
del ppl_00[1::2] #sliceing
print("remaining ppl after two rounds of killing")
print(ppl_00)
ppl_1=ppl
del ppl_1[1::2] #sliceing
print("remaining ppl after three rounds of killing")
print(ppl_1)
ppl_2=ppl_1
del ppl_2[ ::2] #sliceing
print("remaining ppl after fourth rounds of killing")
print(ppl_2)
ppl_3=ppl_2
del ppl_3[1::2] #sliceing
print("remaining ppl after 5th rounds of killing")
print(ppl_3)
ppl_4=ppl_3
del ppl_4[1::2] #sliceing
print("remaining ppl after 6th rounds of killing")
print(ppl_4)
ppl_5=ppl_4
del ppl_5[::2] #sliceing
print("remaining ppl after 7th rounds of killing")
print(ppl_5)

l=list(range(1,101))
x=2*list(range(1,101))+1

from itertools import cycle
NUMBER = 100
people = list(range(1, NUMBER + 1))
dead = []
print  ("Runing")

print (people)
people_list = cycle(people)

while len(people) != 1:
    tolive = next(people_list)
    if tolive not in dead:
        todel = next(people_list)

    if todel not in dead:
        dead.append(todel)
    else:
        people = set(people) - set(dead)
        print (sorted(people))
        people_list = cycle(sorted(people))

print (people)
print ( "over")

circle = list(range(1,7))
#100 people numbered 1-100


while len(circle) > 1: #run this code as long as the circle has more than one person
    print(str(circle[0]) + " kills " + str(circle[1]))
    survivor = circle[0] #save the survivor to a variable
    circle.pop(1) #remove the person killed from the list
    circle.pop(0) #remove the person who survives from the list
    #now the new start of the list is whoever is next in line

    circle.append(survivor) #re-add the survivor to the list at the end

print(str(circle[0]) + "is the winner") #print out the survivor

