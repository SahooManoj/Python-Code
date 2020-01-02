# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:16:01 2019

@author: Administrator
"""

li1 = [12, 'ab', 1.3, (11,'op'), -9, 17, 2.9]
tu1 = (9,'io',7.1,['jk',13],19,-17,'er')
print(li1)
li1[2] = 2.3 # list elements can be change
print(li1)

tu1[2] = 2.3 # tuple elements can't be change
print(tu1) 

print(li1.append(12))
li1.append(34) # append at last
print(li1)
li1.insert(4,45) # append at 4th index
print(li1)

li2=li1
li1.extend([10,12,13]) # extend the value but don't create any other reference
print(li2)
#li2 will be also extending
li1 =li1 + [10,12,13] # extend the value but create another reference
# li2 will remain unchange
print(li1)
print(li2)

li1.index(45) # will give the index number of 1st occurence
li1.count(10) # will count total number of 10 present in li1
li1.remove(10) # will remove 10 from li1 at the first occurence


li1.reverse()
print(li1)
li3 = [3,6,8,4]
li3.sort()
print(li3)


li1.pop(5) # delete that index element