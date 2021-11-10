# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:52:13 2021

@author: Manaswini Raghavan
"""


import pandas as pd


def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

char_list = [chr(i) for i in range(97,97+26)]

di = dict()
with open('word.txt') as f:
    for piece in read_in_chunks(f):
        w = piece.lower()
        w_l = w.split()
        for i in char_list:
            if i in di.keys() :
                di[i].extend(list(filter(lambda x: x[0] == i, w_l)))
            else:
                di[i]=list(filter(lambda x: True if x[0] == i else False, w_l))
            


original= pd.DataFrame()

for i in char_list:
    additional = pd.DataFrame({i:di[i]})
    original = pd.concat([original, additional], axis=1) 


original.to_excel('word.xlsx')


for i in char_list:
    di[i] = [len(di[i])]
    
df = pd.DataFrame(di)

df.to_excel('word1.xlsx')
