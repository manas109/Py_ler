# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
for num in range(1,11):
    if num!=5 and num!=8:
        print(num)
   """     
       
    # 8 36 52 45 91 83 
#for num in range(1,101):
 #   num1=num.remove(8, 36, 52, 45, 91, 83)
  #  print(num1)
"""    
for numb in range(1,101):
    if numb!=5 and numb!=8 and numb!=36 and numb!=52 and numb!=91 and numb!=83:
        print(numb)
  """ 
"""     
for num in range(1,101):
    if num not in[5, 8, 36, 52, 45, 91, 83]:
        print(num)
"""

#1900 2021 finding the leap year in range 
start = 1900
end = 2021
while start<end:
    if start%4==0 and start%100!=0:
        print(start)
    if start%100==0 and start%400==0:
        print(start)
    start+=1
    
 
#right shift more than 10 bite wise right shift and print in binary
a=20
c=a>>2
print('a>>2=',c)

def decimalToBinary(c):
    if c>=1:
        decimalToBinary(c//2)
    print(c%2,end="")
     
decimalToBinary(c)   #y this line ?

     
