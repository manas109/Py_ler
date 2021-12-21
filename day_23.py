# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:33:36 2021

@author: Manaswini Raghavan
"""
import pandas as pd
import json
import csv
#json_path_file=r"C:\Users\Manaswini Raghavan\Downloads\AXISBANK.csv"

df=pd.read_csv(r"C:\Users\Manaswini Raghavan\Downloads\AXISBANK.csv")

df.std()
threshold = 2.5

df.drop(df.std()[df.std() < threshold].index.values, axis=1)
    
