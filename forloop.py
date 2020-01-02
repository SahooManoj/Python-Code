# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:33:44 2019

@author: Administrator
"""

for i in "Hello World":
    print(i)
    
for i in [10,24,(11,40),50]:
    print(i)

for (x,y) in [('a',1),('b',2),('c',3),('d',4)]:
    print(x)
    print(y)
    
for i in range(5):
    print(i)
    
    
    
user = {'fn':'Anju','ln':'Savvy','id':2134,'ext':4176,'pass':'apass'}

for name in user.keys():
    print(name,user[name])
    
for (x,y) in user.items():
    print(str(x)+"=>"+str(y))