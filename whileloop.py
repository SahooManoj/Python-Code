# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:21:39 2019

@author: Administrator
"""

x=0
while x<5:
    print('x is', x)
    x=x+1
    
    
i=0
while i<10:
    i=i+1
    if i<=4:
        print("continue")
        continue
    print("i is",i)
    if i>=8:
        print("Break")
        break