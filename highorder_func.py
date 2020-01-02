# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:40:38 2019

@author: Administrator
"""

def square(x):
    return x*x
def even(x):
    return x % 2 == 0
print(list(map(square,range(10,20)))) # return modified value
print(list(filter(even, range(10,20)))) # return boolean so ity will filter out those element which returns true value
print(list(map(square, filter(even,range(10,20))))) # will modify the value after filtering



sem1=[12,11,18,9,14]
sem2=[14,12,11,16,17]
print(list(map(lambda x:x*2,sem1)))
print(list(filter(lambda x:x%2 == 0,sem1)))
assert(len(sem1) == len(sem2))
print(list(map(lambda x,y:x+y,sem1,sem2)))
print(list(map(lambda x,y:max(x,y),sem1,sem2)))
print(dict(zip(sem1,sem2))) # will make dictionary
print(list(zip(sem1,sem2))) # will make list of tuples
print(tuple(zip(sem1,sem2))) # will make tuple of tuples
print(list(enumerate(sem1))) # makes an enum [(0, 12), (1, 11), (2, 18), (3, 9), (4, 14)]


li1 = [12, 'ab', 1.3, (11,'op'), -9, 17, 2.9]
allindex = (list(map(lambda x:x[0] if x[1] == 1.3 else -1, enumerate(li1))))
print((list(map(lambda x:x[0] , enumerate(li1)))))
print(list(filter(lambda x:x != -1,allindex)))
print(list(filter(lambda x:x != -1,(list(map(lambda x:x[0] if x[1] == 1.3 else -1, enumerate(li1)))))))


from functools import reduce
print(reduce(lambda x,y:x+y, sem1)) #will give the summation of all elements in sem1
print(reduce(lambda x,y:x^y, sem1))
