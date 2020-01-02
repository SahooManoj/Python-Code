# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:06:34 2019

@author: Administrator
"""

user = {'fn':'Anju','ln':'Savvy','id':2134,'ext':4176,'pass':'apass'}
print(user['ln'])

user['cell'] = 9849940940
user['ext'] = 4178

print(user)

user.pop('ext')

print(user)

print(user.keys())
print(user.values())
print(user.items())

