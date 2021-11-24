# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:57:28 2021

@author: Manaswini Raghavan
"""


2+3

fi = open('trial_1.txt','w')

fi.close()


with open('trial_2.txt','a') as f:
    f.write('ha')
    
    #f.write('Haaaaaa_1')


d={1:2}
    
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(d,f)

with open('model.pkl', 'rb') as f:
    fi =pickle.load(f)

d={"name":"manu","dob":"jun","num":"9900662117"}
with open('model_01.pkl', 'wb') as f:
    pickle.dump(d,f)
with open('model_01.pkl','rb')as f:
    gi=pickle.load(f)
    
