# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:35:41 2019

@author: Administrator
"""

def square(x):
    return x*x
def applier(q,x):
    return q(x)

print(applier(square,7))
print(applier(square,8))

print(applier(lambda x:x*x,7))
print(applier(lambda x:x*2,7))


def duoapplier(q,x,y):
    return q(x,y)
print(duoapplier(lambda x,y:x+y,7,8))

cube = lambda x:x*x*x
print(cube(7))


def inc_x(n):
    return lambda x:n+x
f1 = inc_x(1)
f2 = inc_x(2)
print(f1(2))
print(f2(3))

ie = inc_x('http://')
gc = inc_x('https://')
print(ie("facebook.com"))
print(gc("facebook.com"))