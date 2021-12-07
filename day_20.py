# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:24:22 2021

@author: Manaswini Raghavan
"""


b = bin(100)
r = b[:2]+b[3:]+b[2]
int(r,2)


class DemoDetsils01:
    def __init__(self):
        self.car_name=input("enter the car name: ")
        self.engine_cap = int(input(" enter power of engine:  "))
        self.seats=int(input("Enter the number of seats in the car: "))
        self.version=input("Enter the  version(p/d): ")
        self.model=int(input("Enter the model number: "))
                     

    
    def __gt__(self,other):
        return self.model>other.model
    
    def __repr__(self):
        return f'the car name is {self.car_name}, Engine capactiy is {self.engine_cap}, Number of seats are {self.seats}, Car Version is {self.version}, Model number is {self.model}'


number_of_cars = int(input('Enter number of Cars details you like to enter: '))
Car_list = [DemoDetsils01() for i in range(number_of_cars)]


sorted(Car_list,reverse=True)


import pickle      
with open('model_02.pkl', 'wb') as f:
    pickle.dump(DemoDetsils01,f)
with open('model_02.pkl','rb')as f:
    gi=pickle.load(f)




import pandas as pd

df = pd.DataFrame({'years':range(2000,2022),'sales':range(230,230+22)})





df = pd.read_csv(r"C:\Users\Manaswini Raghavan\Downloads\archive (2)\government-procurement-via-gebiz.csv")



df.columns

df['tender_no.']
df[['tender_no.','awarded_amt']]

len(df['tender_no.'].unique())


df['tender_no.'].count()

df[['tender_no.','awarded_amt']][(df['awarded_amt']>75000) & (df['awarded_amt']<100000)]



df[['awarded_amt']].plot()

#
import numpy as np

lst1= [i for i in range(1, 11) if i % 1 == 0]
lst2=[j for j in range(2, 21) if j % 2 == 0]
lst3=[k for k in range(3, 31) if k % 3 == 0]
multp_list=pd.DataFrame(np.column_stack([lst1, lst2, lst3]))





l = [i for i in range(3, 31) if i % 3 == 0]

d = {i:list(range(1*i,11*i,i)) for i in range(1,11)}


df = pd.DataFrame(d)

delim = "X"
print (delim+"text"+delim+'delim'+"delim"+delim+\
  str(93.2)+delim)




def x(y): pass

if ('-1'):
    print ('ouch')
else: 
    print ('echo')
    
if ((5!=5) and (5>3)):
  print ("1")
elif ((5!=5) or (5<3)):
  print ("2")
elif ((5!=5) or (3>5)):
  print ("3")
elif ((5!=5) or (5>3)):
  print ("4")
elif ((5<=3) or (5>=3)):
  print ("5")
elif ((5>3) and (5<10)):
  print ("6")
else:
  print ("7")
#X=?
  abs(26) + abs(-1) - abs(-0)

s = [1,2,3,4,5,6,3]
s[6]
len(s)
s.index(3,3,8)


def goat(b): b.append("wolf")

sheep = []
goat(sheep)
print (sheep)

y = 12L
z = 12
v = y + z
print v


a=print(input("enter a integer")
if (a.is_integer()):
    print("true")
else:
    print("false")

f = 1.23

print(f.is_integer())
# False
else:
    print("true")
# True