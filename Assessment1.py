# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:12:52 2019

@author: Administrator
"""

name=input("Enter your name:")
wage=int(input("Enter your wage:"))
if wage < 1000 :
    print("Hello", name,"your salary is low")
elif wage < 2500:
    print("Hello", name,"your salary is Moderate")
else :
    print("Hello", name,"your salary is High")
print("Thank you for using our program")