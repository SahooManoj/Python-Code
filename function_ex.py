# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:22:52 2019

@author: Administrator
"""

def mymath(x,y):
    x = 7.1*x + 3.91/y
    y = 6.11*x + 2.9/y
    return x+y

a,b=5,6
ret = mymath(a,b)
print("Return value is", ret)
print("Return value is %0.1f" %ret) # format specifier decide the number of decimal places. No comma in between.
print('a is ',a, 'and b is', b)
print('x is ',x, 'and y is', y)






