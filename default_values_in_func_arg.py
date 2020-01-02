# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:46:45 2019

@author: Administrator
"""

def defval(a=9,b=6,c="Hello"): #def defval(a=6,b,c="Hello"): is not allowed
    print("c is", c)
    return a+b
print(defval(5))
print(defval(10,20))
print(defval(10,20,"Hi"))
print(defval(b=21))

def kargs(a,b,c):
    return a+b-c

print(kargs(5,6,7))
print(kargs(c=7,b=6,a=5))
print(kargs(5,c=6,b=7))
