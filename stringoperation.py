# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:39:46 2019

@author: Administrator
"""

name="Harshit"
print(len(name))

#indexing
for i in range(-1,-12,-1):
    print(name[i],end="")
    
for letter in name:
    print(letter,end="")
    
#slicing
print(name[::])
print(name[0:4:1])
print(name[0:-4:1])
print(name[0:-4:-1])


#swapping
n1=10
n2=20
n3=50
print(n1,n2,n3)
n1,n2,n3=n2,n3,n1
print(n1,n2,n3)

n1=10
n2=20
n3=30
print(n1,n2,n3)
n1,n2,n3=n2,n1,n1
print(n1,n2,n3)

name,surname=input("Enter your fullname: ").split()
print(name)
print(surname)

name="    Manoj     "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

name="Harshit"
print(name.replace('H','Z'))
print(name.replace('Har','XYZ'))

name="harshit"
print(name.index('h'))
print(name.rindex('h'))
print(name.find('h'))
print(name.rfind('h'))

print(name.index('p')) #will give error
print(name.find('p')) #will not through error

#to get help of function
help(str.find)
help(name.index)