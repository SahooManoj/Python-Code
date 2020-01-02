# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 17:53:07 2019

@author: Administrator
"""

#shortcut method
with open("hello.kt","r") as f:
    print(f.readlines())
    
#normal output
with open("hello.kt","r") as f:
    for line in f.readlines():
        print(line)
    
#byte mode / raw form    
with open("hello.kt","rb") as f:
    for line in f.readlines():
        print(line)
        
#we can decode the byte mode
with open("hello.kt","rb") as f:
    for line in f.readlines():
        print(line.decode())    
        
#appending to  file
with open("hello.kt","a") as f:
    f.write("\nTest")
    

#copying to another file
with open("hello.kt","r") as f:
    with open("hello1.kt","a") as g:
        for line in f.readlines():
            g.write(line)
            
            
with open("hello.kt","rb") as f:
    f.readlines().decode()
    
#longcut method

f1=open("hello.kt","r")
#print(f1)
print(type(f1))
for line in f1.readlines():
    print(line)
f1.close()

with open("hello.kt","r") as f:
    with open("example.txt","a") as g:
        for line in f.readlines():
            g.write(line)
            
            
m=open("hello.kt","r")
m.seek(3)
print(m.readline())
m.close()
m=open("hello.kt","r")
m.seek(3)
m.seek(1) # bydefault this will overwrite the pointer again to 1
help(m.seek)
m.close()

m=open("hello.kt","rb")
m.seek(3)
m.seek(1,1) # (1,1) 2nd 1 is the whence i.e. the current seek position i.e 3+1=4th point
'''
    seek(cookie, whence=0, /) method of _io.TextIOWrapper instance
    Change stream position.
    * 0 -- start of stream (the default); offset should be zero or positive
    * 1 -- current stream position; offset may be negative
    * 2 -- end of stream; offset is usually negative
'''
