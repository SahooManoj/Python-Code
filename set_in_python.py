# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 19:50:35 2019

@author: Administrator
"""

s1=[1,1,1,2,2,2,3,3,3,4,4,4]
example=set(s1)
print(example)
print(type(example))
s2={1,2,6,7}
print(example.intersection(s2)) # & symbol for intersection print(example & s2)
print(example.union(s2)) # | symbol for union print(example | s2)
print(example.difference(s2))