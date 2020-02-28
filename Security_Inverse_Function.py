# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:26:06 2020

@author: manoj.sahoo
"""

#Security Inverse Function

def main():

    n=int(input())
    f=input().split(" ")
    newf=[]
    output=[]
    for item in f:
        newf.append(int(item))
    if n>=1 and n<=20 and n==len(newf):
        for i in range(n):
            if i+1==newf[i]:
                output.append(newf[i])
            elif i+1>newf[i]:
                output.append(i+i+2-newf[i])
            else:
                output.append(i+1-(newf[i]-(i+1)))
            if i==n-1:
                print(output[i],end='')
            else:
                print(output[i])

main()