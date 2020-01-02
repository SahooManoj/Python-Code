# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:55:03 2019

@author: Administrator
"""

#Take keys as input from the user
#accep values for each key from the user and modify the dictionary
#print the final dictionary

li=[]
dict_hash={}
for i in range(5):
    li.append(input("Enter key{} : ".format(i+1)))
dict_hash=dict_hash.fromkeys(li)
for key in dict_hash:
    dict_hash[key]=input("Enter the value for key '{}' : ".format(key)) 
    #dict_hash.update({key:input("Enter the value for key '{}' : ".format(key))})
print(dict_hash)