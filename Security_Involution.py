# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:02:29 2020

@author: manoj.sahoo
"""

#Security Involution
def main():

    n=int(input())
    f=input().split(" ")
    newf=[]
    c=0
    for item in f:
        newf.append(int(item))
    if n>=1 and n<=20 and n==len(newf):
        for i in range(n):
            if newf[0]>=1 and newf[0]<=n:
                if newf[newf[i]-1]!=i+1:
                    print("NO",end='')
                    c=1
                    break
            else:
                print("NO",end='')
                c=1
                break
        if c==0:
            print("YES",end='')
main()