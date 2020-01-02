# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:52:43 2019

@author: Administrator
"""

greet = "good evening"
print(dir(greet))
print(greet.upper())
print(greet.capitalize())
print(greet.title())
print(greet.strip())

#example 1
def yesno():
    ans=input("Enter yes or no: ").strip()
    if ans.upper() == "YES":
        print("You typed yes")
    elif ans.upper() == "NO":
        print("You typed no")
    else:
        print("please enter yes or no")
        
yesno()

#example 2
wage=input("Enter your wage ")
if wage.isdigit():
    wage=int(wage)
else:
    wage=250
print("Daily wage is",wage*8)

#justification
fn,ln="Manoj","Sahoo"
print("|%-10s|%10s|" %(fn,ln))
print("Hello","world",sep="\t") # separates the 2 string with tab
print("Hello","world",end=" ") # end of line will be replace by space
print("Hello\nWorld") # will print World in new line
print(r"Hello\nWorld") # r is raw stream and act as escape character



#join,split - it will only works in case of string
print(",".join(["ab","cd","ef"]))

print("abc;def;ghi".split(";"))
