# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:48:11 2019

@author: Administrator
"""
#printing the index of an element in list
def indices_check(li,a):
    i=0
    index=""
    while i<len(li):
        if str(a) == str(li[i]):
            if index == "":
                index=str(i)
            else:
                index=index + "," + str(i)
        i=i+1           
    if index == "":
        print("Element doesn't exist in the given list of element")
    else:
        print("Index of", a, "in list", li, "are", index) 
        
list=['g',30,"ab",40,30,'g',20.1]
x=input("Enter the element:")
indices_check(list,x)