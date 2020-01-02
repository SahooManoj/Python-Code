# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:22:56 2019

@author: Administrator
"""

li1 = [12, 'ab', 1.3, (11,'op'), -9, 17, 2.9]
tu1 = (9,'io',7.1,['jk',13],19,-17,'er')
print(li1[3])
print("Last element is",tu1[-4])
subli = li1[2:6] # not refering to the elements of li1 its getting a separate copy this is called slicing 
print("from 2nt index to 5th index",subli)
subtu = tu1[1:-1]
print(subtu)
subtu1 = tu1[:2]
print("upto 1st index",subtu1)
subtu2 = tu1[2:]
print("From 2nd index to last",subtu2)
subtu3 = tu1[:]
print("all",subtu3)

li2 = li1
li3 = li1[:]
print("id of li1 is", id(li1))
print("id of li2 is", id(li2))
print("id of li3 is", id(li3))

print(li1 == li3) # compares value
print(li1 is li3) # compares id
print(li1 == li2)
print(li1 is li2)

alphas = 'abcdefghijklmnopqrstuvwxyz'
print(alphas[4:25:3]) # alphas[m:n:p] where p is the step
print(alphas[25:4:-1]) # alphas[m:n:p] where p is the step
print(alphas[::-1]) # will print all in reverse order
print(alphas[::])
nap = "able was i ere i saw elba"
print(nap == nap[::-1])
print(nap is nap[::-1])

print(12 in li1) #true 
print(11 in li3) #false
print(11 in li1[3]) #true


print((1,2,3) + (4,5,6)) # concatenating tuple
print([1,2,3] + [4,5,6]) # concatenating list
print((1,2,3) + [4,5,6]) # TypeError: can only concatenate tuple (not "list") to tuple
print("Hello" + " " + "world") # string concatenation

print((1,2,3)*3) # printing tuples multiple times
print([1,2,3]*3) # printing list multiple times
print("Hello"*3) # printing string multipl