# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:40:13 2021

@author: Manaswini Raghavan
"""
import pandas as pd
import json
import csv
json_path_file=r"C:\Users\Manaswini Raghavan\Desktop\icc_results.json"
with open(json_path_file,"r") as f:
    data = json.load(f)

print(data)

content=pd.read_json(json_path_file)
for k in content.columns:
    print (k)

reviewed = content.groupby(['label','timestamp','tournamentLabel','resultOnly'])
print(reviewed)

with open(r"C:\Users\Manaswini Raghavan\Desktop\files.csv","w") as h:
    
    csvwriter = csv.writer(h)
    
    for i in reviewed:
        csvwriter.writerows(i)