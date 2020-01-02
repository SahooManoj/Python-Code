# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:16:18 2019

@author: Administrator
"""

li1=[12,8,9,12,15,8,8,12,15,9]
li2=[15,2,2,12,15,7,7,15,2,15]
s1=set(li1)
s2=set(li2)
print(s1)
print(s2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))

print(dict.fromkeys(li1))
print(list(dict.fromkeys(li1))) # to make it order
