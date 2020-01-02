# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:12:48 2019

@author: Administrator
"""

import sqlite3
obj=sqlite3.connect("Example1.db")
obj.execute("Create table DEMO (name varchar(20),id int)")
obj.execute("Insert into Demo values('Manoj',23)")
obj.execute("Insert into Demo values('Durgesh',32)")
obj.execute("Insert into Demo values('Nirav',28)")
obj.commit()
cursor=obj.execute("Select * from DEMO")
for value in cursor:
    print(value)
    
obj.close()
