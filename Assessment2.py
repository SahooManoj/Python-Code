# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:12:16 2019

@author: Administrator
"""

user = {'fn':'Anju','ln':'Savvy','id':2134,'ext':4176,'pass':'apass'}
x=str(input("Enter a key:"))
if x in user:
    print(user[x])
else:
    print("No such keys")

z=str(input("Enter a value:"))
if z in user.values():
    for (x,y) in user.items():
        if y == z:
            print(x)
else:
    print("No such values")


