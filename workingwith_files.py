# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 19:27:46 2019

@author: Administrator
"""

def file_wr(filename):
    f=open(filename,"w") # w is used for writing and if file exist it will overwrite else will create a new file
    f.write("Hello World\n")#we can give only one argument
    f.write("Hi world\n")
    f.write("Bye world\n")
    name="Manoj"
    wage=2343
    f.write(name+":"+str(wage*8)) # to give both the value we have concatenate
    f.close
    
file_wr("output.txt")


def file_rd(filename):
    f=open(filename)
    print(f.readline())
    f.seek(0,0) # will again start from 1st line
    print(f.readlines())
    f.seek(0,0)
    print(list(map(lambda x:x.strip(),f.readlines()))) # will strip \n
    f.close

file_rd("output.txt")