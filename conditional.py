# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:56:14 2019

@author: Administrator
"""

n1=10
if n1%10==0:
    print("From if statement")
elif n1>5:
    print("From else if")
else:
    print("Else part")
    
n1=50 if 5<4 else 20
print(n1)