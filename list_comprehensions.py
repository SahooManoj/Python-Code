# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:30:38 2019

@author: Administrator
"""

li = [3,6,2,7]
print([elem*2 for elem in li])

li = [('a',1),('b',2),('c',7)]
print([n*3 for (x,n) in li])

def subtract(a,b):
    return a-b
oplist = [(6,3),(1,7),(5,5)]
print([subtract(y,x) for (x,y) in oplist])

#filered list comprehension
li=[3,6,2,7,1,9]
print([elem*2 for elem in li if elem>4])
