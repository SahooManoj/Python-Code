# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:00:06 2019

@author: Administrator
"""

def magic(x,y):
    print("Magic Happened!")
    return x+y
    
print(magic(2,3))
res=magic(3,4)
print(res)

#Functions are first class object
#can be stored in a variable
#Function can return a function


#supports closure
def outer():
    def inner():
        print("Inner Executed!")
    return inner

ans=outer()
print(ans())


#passing function as parameter


def test(x,y):
    return x**y

def example(a,b):
    return a+b


def magic1(example): #formal parameter example which has test
    print(example(2,3)) #in example it will be pass the address of function so test will be called not example
    
magic1(eval(input("enter the function name:"))) #actual argument == test 


def func(*args):
    print(len(args))
    
func(1,2,3,4)
func(1,2,3,4,5,6,7)
func()



def func1(**kwargs): # to give dictionary as input
    print(isinstance(kwargs,dict))
    for k,v in kwargs.items():
        print(k,v,sep="**")
    
#func1({"n1":10,"n2":20})
func1(n1=10,n2=20)
