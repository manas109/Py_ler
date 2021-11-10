# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:52:49 2021

@author: Manaswini Raghavan
"""

word = """
Speaking to ANI, Rawat said, "It (Congress face for upcoming state assembly polls) will be decided by the Congress president, but given the circumstances, elections will be fought with the chief minister's cabinet under Punjab Pradesh Congress Committee, whose chief is Navjot Singh Sidhu, who is very popular."
He further stated that Congress had yesterday itself unanimously decided to make Charanjit Singh Channi the next chief minister of Punjab.
"The decision (to choose the new Punjab CM) was taken yesterday. We were only waiting to meet the governor. The party was unanimous on Charanjit Singh Channi's name. We will try to ensure that he (Amarinder Singh) is there at oath-taking, but it's up to him," said Rawat.
He said that the names for two deputy chief ministers are yet to be decided.
"Our mutual feeling is that there should be two deputy CMs. Soon we will take a call on it along with names for the Council of Ministers. Some names have been discussed but it's the CM's prerogative who will discuss it with party high command and take a call," the former Uttarakhand chief minister said.
Congress MLA Charanjit Singh Channi will take the oath as the new Chief Minister of Punjab on Monday at 11am on Monday."""

len(word.split())

with open('word.txt','w') as f:
    f.write(word)
    
#############################
    
with open('word.txt','r') as fr:
    w = fr.read()
    
w_l = w.split()
len(w_l)


