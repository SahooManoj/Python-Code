# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:12:43 2019

@author: Administrator
"""

for i in range(0,10,1): #end range will never be touched, the value will be 0-9
    print(i)

for i in range(50,15,-5):
    print(i)
    
name="Manoj"
for i in range(7): #if we only specify 1 value then that will be the end of range and assume 0 is the start and 1 is the step
    print(name[i])
    
for i in range(10,7): #will not print any output
    print(i)
    
for i in range(10,7,-1): #if we only specify 1 value then that will be the end of range and assume 0 is the start and 1 is the step
    print(i)


for i in range(10,7,-1): #if we only specify 1 value then that will be the end of range and assume 0 is the start and 1 is the step
    print(i)
else:
    print("else part")
    
    
n1=10
while n1>10:
    print("while part")
else:
    print("else part")
    
while n1<20:
    print(n1)
    n1+=1 #n1=n1+1
    

