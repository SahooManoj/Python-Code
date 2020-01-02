# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:53:56 2019

@author: Administrator
"""
# getting only the ".in" element
urls=['a.in','b.jp',"d.in","in.in"]
print(list(filter(lambda x:x.find(".in") >= 1,urls)))
print(list(filter(lambda x:x.__contains__(".in"),urls))) # most appropriate
print(list(filter(lambda x:x[-2:] == 'in',urls)))


#creating unzip function
zlist=[(12,14),(11,12),(18,11),(9,10),(14,17)]
def unzip(myli):
    print(list(map(lambda x:x[0],myli)))
    print(list(map(lambda x:x[1],myli)))
    
unzip(zlist)    
    

#validating palindrome 
string="A man, a plan, a canal; Panama"
string=string.upper()
lialpha=list(filter(lambda x:x.isalpha(),list(string)))
if lialpha == lialpha[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
