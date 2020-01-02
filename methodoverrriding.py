# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 17:27:19 2019

@author: Administrator
"""

class Base:
    def magic(self):
        print("From Base")
    def __init__(self):
        if isinstance(self,Base):
            self.name=input("Enter your name: ")

class Child(Base):
    def magic(self):
        print("From Child")
        
c1=Child()
c1.magic() # method overriding, child function gets priority

#method overloading is not allowed in Python


#one way of doing the work of overloading
class Base1:
    def magic(self):
        print("From Base")
        
class Child1(Base1):
    def magic(self,*args):
        if len(args)==0:
            print("From Child")
        elif len(args)==1:
            print(len(args))
        else:
            print("LAST CASE")
            
            
c1=Child1()
c1.magic()
c1.magic("Manoj")
c1.magic("Manoj","Sahoo")
        