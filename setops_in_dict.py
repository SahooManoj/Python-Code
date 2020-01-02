# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:26:13 2019

@author: Administrator
"""

d1 = {'a':8,'b':6,'c':9,'d':5}
d2 = {'e':7,'a':4,'d':8,'f':3}
def uni_dict(myd1,myd2):
    s1=set(myd1)
    s2=set(myd2)
    retdict={}
    for var in s1.union(s2):
        if var in s1 and var in s2:
            retdict[var]=[myd1[var],myd2[var]]
        elif var in s1:
            retdict[var]=myd1[var]
        else:
            retdict[var]=myd2[var] 
    return retdict
    
print(uni_dict(d1,d2))

def sym_def_dict(myd1,myd2):
    s1=set(myd1)
    s2=set(myd2)
    retdict={}
    for var in s1.symmetric_difference(s2):
        if var in s1:
            retdict[var]=myd1[var]
        else:
            retdict[var]=myd2[var] 
    return retdict

print(sym_def_dict(d1,d2))

def intersection_dict(myd1,myd2):
    s1=set(myd1)
    s2=set(myd2)
    retdict={}
    for var in s1.intersection(s2):
        retdict[var]=[myd1[var],myd2[var]] 
    return retdict

print(intersection_dict(d1,d2))