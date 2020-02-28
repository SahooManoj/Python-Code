# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 20:36:13 2020

@author: manoj.sahoo
"""

#Security_permutation

def main():

    n=int(input())
    f=input().split(" ")
    newf=[]
    for item in f:
        newf.append(int(item))
    if n>=1 and n<=5 and n==len(newf):
        for i in range(n):
            if newf[0]>=1 and newf[0]<=n:
                if i==n-1:
                    print(newf[newf[i]-1],end='')
                else:
                    print(newf[newf[i]-1])
            else:
                break

main()