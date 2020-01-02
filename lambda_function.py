# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:42:32 2019

@author: Administrator
"""

def magic(x):
    return x*x
print(magic(7))

#lambda    x         : x*x
#keyword input params:output
var=lambda x:x*x
print(var(8))

lambda x,y:x+y
print(var(8,9))


ans=map(lambda x : x*x,[1,2,3,4]) # map required 2 parameters, function and object and it returns object reference

for value in ans:
    print(value)