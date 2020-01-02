# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:20:11 2019

@author: Administrator
"""
val=int(input("Enter a number "))
li=[1,2,3,4,5]
for i in range(val):
    li[0],li[1:len(li):1]=li[-1],li[0:len(li)-1:1]

print(li)



li[0:-1:1],li[-1::]=li[-1::],li[0:-1:1]

