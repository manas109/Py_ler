# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 18:06:39 2021

@author: Manaswini Raghavan
"""


[[1 if (i==0 or i==4) or (j == 0 or j ==4) else 0 for i in range(5) ] for j in range(5)]



name = input('enter your name')
mob = input('enter your mobile no.')



class StudetnDetails:
    
    def __init__(self):
        self.get_name()
        self.get_mobile_number()
        
    def get_name(self):
        self.name = input('enter your name')
    
    def get_mobile_number(self):
        self.mob = input('enter your mobile no.')
        
    def display_pd(self):
        print(f'Student name is{self.name} and mobile number is {self.mob}')


stud_1 = StudetnDetails()

stud_1.get_name()
stud_1.name

stud_1.get_mobile_number()
stud_1.mob


stud_1.display_pd()

class DemoDetails:
    
    def __init__(self):
        self.get_name()
        self.get_marks()
        self.get_total()
        self.get_avg()
        
    def get_name(self):
        self.name = input("enter the name")
    
    def get_marks(self):
        self.marks=[0]*3
        for i in range(1,4):
            self.marks[i-1] = int (input( 'enter' f"{i}, subj marks"))
    
    def get_total(self):
        self.tot= sum(self.marks)
        
    def get_avg(self):
        self.avg = (self.marks)
        
        
class DemoDetsils01:
    def __init__(self):
        self.roll_num = int (input("enter the roll num: "))
        self.stname = input(" enter your name:  ")
        self.get_marks()
        self.get_total()
        self.get_avg()
                     
        
    def get_marks(self):
        self.marks=[0]*3
        for i in range(3):
            self.marks[i] = int (input( f'enter subj {i} , subj marks: ' ))
            
    def get_total(self):
        self.__sum  = sum(self.marks)
        print(self.__sum)
       # self.__add__ =__add__m(self.get_marks())
        
    def get_avg(self):
        self.avge = self.__sum/3
    
    
    def __gt__(self,other):
        return self.__sum>other.__sum
    
    def __repr__(self):
        return f'the student name is {self.stname}, roll number is {self.roll_num}, marks is {self.__sum}, avg is {self.avge}'
    
#stud = DemoDetsils01()


number_of_students = int(input('Enter number of students: '))
studetn_list = [DemoDetsils01() for i in range(number_of_students)]



sorted(studetn_list,reverse=True)



print("total:")
stud.__sum
stud.sum()
print("average : ")
stud.avge
        
class Student:
    def getStudentDetails(self):
        self.rollno=input("Enter Roll Number : ")
        self.name = input("Enter Name : ")
        self.physics =int(input("Enter Physics Marks : "))
        self.chemistry = int(input("Enter Chemistry Marks : "))
        self.maths = int(input("Enter Math Marks : "))

    def printResult(self):
        self.percentage = (int)( (self.physics + self.chemistry + self.maths) / 300 * 100 ); 
        print(self.rollno,self.name, self.percentage)

S1=Student()
S1.getStudentDetails()

print("Result : ")
S1.printResult()


        
 




