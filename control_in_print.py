# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:20:55 2019

@author: Administrator
"""

fname="Manoj"
lname="Sahoo"
print(fname,lname)
print(fname,lname,sep="") #separating the two string without space
print(fname,lname,sep="-")
print(fname,lname,sep="",end="") #ending the line with an empty string, not going to next line
print(sep="",end="",fname,lname) #will not work, positional argument follows keyword argument, if we declare keyword argument 1st then all should be keyword language
print("My name is {} and surname is {}".format("Manoj",lname))
print("{}{}".format(fname,lname))
print('{' '}{}'.format(fname,87678))
