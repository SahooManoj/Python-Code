# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:06:34 2019

@author: Administrator
"""

def varargs(*args):
    print(args)
    
varargs(12,11,10)
varargs('a','b')

def varkargs(*args,**kwargs):
    print("Non keyword arguments are", args)
    print("Keyword arguments are", kwargs)

print("with only non keywords")
varkargs('a','b')
print("with only keywords")
varkargs(x=9,y=10,z=12)
print("with mixed")
varkargs('e','f',u=1,v=2,w=3)