# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:29:52 2019

@author: Administrator
"""

class Python:
    version="3.9"
    def display(self): #self is like this keyword of java
        print("python Display is called",self.version)
        
p1=Python() #Python p1 = new Python() in java
print(isinstance(p1,Python))
p1.version=4.1
p2=Python()

print(p1.version)
print(p1.display())
print(p2.version)



class Being:
    version="3.7"
    def __init__(self): # defining constructor
        '''
        self.age=int(input("Enter your age: "))
        self.name=input("Enter your name: ")
        '''
        super().display()
    def display(self): #self is like this keyword of java
        print("Being Display is called",self.version)
        

        
        
b1=Being()
print(vars(b1)) # to check the local properties inside constructor
print(dir(b1)) # to check all the properties including class properties



#inheritance
class Training(Being,Python): # can pass multiple class (Being,class2) # multiple inheritance, we also have multilevel inheritance
    pass

t1=Training()

t1.version = 4.8
t1.display()
