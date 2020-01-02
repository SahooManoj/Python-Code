# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:55:07 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:46:43 2019

@author: Administrator
"""

import pdb #python debugger module

import csv

pdb.set_trace() #just to tell python that we want to go to debugging mode
with open(r"C:\Users\Administrator\Desktop\Basic Python\examplecsv.csv","r") as file:
    csv_handler=csv.reader(file,delimiter="-") # csv_handler=csv.reader(file) delimeter is not required if the csv is comma separated
    for line in csv_handler:
        print(line) # output will be in list format
        
        

#copying csv file from one to another
with open(r"C:\Users\Administrator\Desktop\Basic Python\examplecsv.csv","r") as file:
    with open("Another2.csv","w") as dest:
        csv_handler=csv.reader(file,delimiter="-")
        dest_handler=csv.writer(dest)
        for row in csv_handler:
            dest_handler.writerow(row)
            

#Escaping the delimeter in special cases where my value contain the same delimeter
with open(r"C:\Users\Administrator\Desktop\Basic Python\examplecsv.csv","r") as file:
    csv_handler=csv.reader(file,delimiter="-",escapechar="\\") # it will escape the char (-) by putting Harshit-Shukla as Harshit\-Shukla
    for line in csv_handler:
        print(line) # output will be in list format
        
#making a dictionary out of csv file
with open(r"C:\Users\Administrator\Desktop\Basic Python\Another.csv","r") as file:
    keys_value=["name","age","gender"]
    csv_handler=csv.DictReader(file,delimiter="-",escapechar="\\",fieldnames=keys_value)
    for line in csv_handler:
        print(line) # it will display an ordered dictionary
        
        
#creating csv from keys
data={"Course":"Python","version":"4.5"}
dest=open("Another3.csv","w")
csv_dest=csv.DictWriter(dest,delimiter="-",fieldnames=data.keys())
csv_dest.writeheader()
csv_dest.writerow(data)
dest.close()

