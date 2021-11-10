# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 07:45:44 2021

@author: Manaswini Raghavan
"""

eval() # evaluates and executes an argument
       # build in function
       #syntax
       eval(expression, globals=None, locals=None)
       
x = 1
print(eval('x + 1'))

num=9
squ_num = eval('num * num')
print(squ_num)

#function
# 

#take the key value 
def string_function(word):
    dic={word:len(word)}
    print(dic)
    
string_function('class')    
        