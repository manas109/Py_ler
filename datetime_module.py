# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:27:10 2022

@author: Manaswini Raghavan
"""
print("hello")
import datetime

#DATE AND TIME MODULE
grv=datetime.date(1996,1,13)
print(grv) 

print(grv.year)
print(grv.month)
print(grv.date)

#time delta : which allows to add r subtract the time

mlt = datetime.date(2000, 1, 1)
print(mlt)
dt = datetime.timedelta(100)
qw = mlt+ dt
print(qw)

# to print a format of the time and date

print(grv.strftime("%A,%B %d,%Y"))

message="gvr was born in {:%A,%B %d,%Y}."
print(message.format(grv))

l_date=datetime.date(2013, 3, 12)
l_time=datetime.time(12,3,4)
l_datetime=datetime.datetime(2013, 3, 12,12,3,4)

print(l_date)
print(l_time)
print(l_datetime)

#to get current datetime
#it even shows th emicro sec
now = datetime.datetime.today()
print(now)

#converting string to time 
moon_landing = """12/2/1988"""
type(moon_landing)
moon_landing = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing)
print(type(moon_landing))