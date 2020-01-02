# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:26:34 2019

@author: Administrator
"""

n1=1


while n1>0 and n1<11:
    print("hello",n1)
    n1+=1
    if n1==5:
        continue
    print("Bye")
    
n1=1

while n1>0 and n1<11:
    print("hello",n1)
    n1+=1
    if n1==5:
        break
    print("Bye")
print("outside")


n1=1


for i in range(2):
    while n1>0 and n1<11:
        print("hello",n1)
        n1+=1
        if n1==5:
            break #no concept of label in python this break will break only from inner loop
        print("Bye")
print("outside")