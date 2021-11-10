# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:12:04 2021

@author: Manaswini Raghavan
"""

import my_functions
temp_kelven(99)
area_squr(11)

#classes(obj oriented pro)
#class defines a temp how the class may be

class EemployeDdetsils:
    
    def __init__(self,name,mail_id,mob):#dynamic
        self.name=name
        self.mail_id=mail_id
        self.mob=mob
    
    def firt_name_last_name (self):
        self.fisrt_name=input("enter ur first name")
        self.last_name=input("enrt the last name ")
        
    def pan_nun(self,pan_number):
        self.pan_number=pan_number
        
    
manasvi=EemployeDdetsils("manu","manaswini.mm7@gamil.com",9900)

manasvi.firt_name_last_name()

manasvi.pan_nun(2233)
        
        

