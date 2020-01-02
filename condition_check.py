# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:49:42 2019

@author: Administrator
"""

x,y,z=5,10,15
print(x > 4 or y > 11 and z < 14)
print(x > 6 and y > 11 or z > 14)
name = input("Enter your name ")
wage = int(input("Enter your wage "))
print("Hello",name, "your daily wage is", wage * 8)

print("High" if wage > 2500 else "Low")