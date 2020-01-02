# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:45:43 2019

@author: Administrator
"""

#to verify the data type
student={}
print(isinstance(student,dict))

name="Manoj"
print(id(name))
name=name.replace("M","H")
print(id(name))

#List
#--------------------------------------------------------------------------------
li=[1,2,3]
print(type(li)) #type will be list
print(len(li)) #length will be work
print(li[2]) #can be indexed
print(li[0:-1:2]) #can be sliced
print(li.index(1))


li1=['a','b','c',[1,2,3],23.06,3+4j,":-)"]
for element in li1:
    print(element)
    
for index,element in enumerate(li1):
    print(index,element,sep="-")
    
    
li1.append(1090)
li1.insert(1,2500)
li1.pop() # will remove the last
li1.pop(2) # 2 is the index
li1.remove() # will remove the last
li1.remove(23.06) # will remove the particular value
li1.reverse()

li2=[3,5,2,1,4]
li2.sort()
li2=["Harshit","Abc",3,6]
li2.sort() # cannot be sorted '<' not supported between instances of 'int' and 'str'

li2.count(3) # give the count of element occurence
li2.clear() # will remove the element but object will remain same
del li2 # will remove the object

l2=li1.copy() # will create a different object

nums=[10,20,30,40]
print(li1,nums,sep="\n")
li1.extend(nums) # will insert the nums list into li1
li1

example=[x for x in range(100)]

li=[]
for x in range (100):
    if(x%2!=0):
        li.append(x)
        
example=[x for x in range(100) if x%2!=0]


matrix=[[cols for cols in range(2)]for rows in range(3)]

m1=[[cols for cols in range(2)]for rows in range(3)]
for rows in range(3):
    for cols in range(2):
        m1[rows][cols]=int(input())
        
m1
#---------------------------------------------------------------------------------

employee={}
print(type(employee))
employee={"id":1,"name":"Manoj","designation":"Developer"} # integer value key can be kept without double quotes but string value key needs to be in double quotes
for pair in employee:
    print(pair)

for pair in employee.items():
    print(pair)
    
for pair in employee.values():
    print(pair)
    
backup=employee.copy()
print(backup) # id will be different

employee.clear() #truncated
del employee

print(backup.get('id'))


nesteddict={
        1: {'id':1,'name':"Harshit"},
        2: {'id':2,'name':"Harshit"},
        3: {'id':3,'name':"Harshit"}
}
nesteddict.values()
nesteddict[1]['id']


id1="id"
age="age"
student={}
for i in range(2):
    #val1,val2=int(input("Enter id and age with space").split()) # this will not work as split will give the values in list
    val1=int(input("Enter ID: "))
    val2=int(input("Enter Age: "))
    student[id1]=val1
    student[age]=val2
    
    
print(backup.pop('name'))
print(backup)

print(backup.pop('name',"Error made by me"))

backup.popitem() # remove and return last key and value like a tuple (k,v)

example={"computer":"Thinkpad"}
backup.update(example) # will add the dictionary example into backup

backup.setdefault("marks",[])
k=[1,2,3,4]
another={}
another.fromkeys(k)


#Tuple
tp=(1,2,3,4)
print(type(tp))

atp=tuple(input("Enter tuple:").split(",")) # to give input
atp.count("1") # will return the count of values
atp.index("3") #will give the index of value from left
