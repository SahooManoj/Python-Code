# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:49:49 2019

@author: Administrator
"""
import sys
sys.setrecursionlimit(2040)
c=0

def calculate(x):
    global c
    c=c+1
    if x == 1:
        return 1
    return x*calculate(x-1)

val=calculate(2000)
print(val,c)

#we can set the recursion limit by default it is 996




m=0
def magic():
    return 1,"Harshit"

print(magic()) # it will return tuples