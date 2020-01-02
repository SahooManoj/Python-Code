# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 15:54:35 2020

@author: manoj
"""
import random
import base64

li = ["UG93ZXJTaGVsbA==","UHl0aG9u","SmF2YVNjcmlwdA=="]

img1="ICB8LS0tLS0tLS0tCiAgfCAgICAgICAgfAogIHwgICAgICAgIHwKICB8ICAgICAgICBPCiAgfCAgICAgICAvfFwKICB8ICAgICAgIC8gXAogIHwKICB8CiAgfA=="
img1=(base64.b64decode(img1.encode())).decode()
img2="ICB8LS0tLS0tLS0tCiAgfCAgICAgICAgfAogIHwgICAgICAgIHwKICB8ICAgICAgICBPCiAgfAogIHwKICB8CiAgfAogIHw="  
img2=(base64.b64decode(img2.encode())).decode()
img3="ICB8LS0tLS0tLS0tCiAgfCAgICAgICAgfAogIHwgICAgICAgIHwKICB8ICAgICAgICBPCiAgfCAgICAgICAvfFwKICB8CiAgfAogIHwKICB8"  
img3=(base64.b64decode(img3.encode())).decode()
img4="ICB8LS0tLS0tLS0tCiAgfCAgICAgICAgfAogIHwgICAgICAgIHwKICB8CiAgfAogIHwKICB8ICAgICAgICBPCiAgfCAgICAgICAvfFwKICB8ICAgICAgIC8gXAo="
img4=(base64.b64decode(img4.encode())).decode()

imglist=[img2,img3,img1,img4]

for value in li:
    count=0
    attempt=3
    value=(base64.b64decode(value.encode())).decode()
    randlist=random.sample(range(1, (len(value)-1)), 3)
    randlist.sort()
    newvalue=value[0:int(randlist[0])] + " _ " + value[int(randlist[0])+1:int(randlist[1])]  + " _ " + value[int(randlist[1])+1:int(randlist[2])] + " _ " + value[int(randlist[2])+1:len(value)]
    print("\nComplete the word :",newvalue)
    for i in range(3):
        count+=1
        attempt-=1
        userinput=input("Attempt {} : ".format(count))
        if userinput.lower() == value.lower():
            print(imglist[3])
            print("\nYou saved my life!")
            break
        elif i<2:
            print(imglist[count-1])
            print("\nWrong ans, you have {} more attempt left!".format(attempt))
        else:
            print(imglist[2])
            print("\nYou Kill me!")
