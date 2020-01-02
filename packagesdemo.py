# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 13:06:21 2019

@author: Administrator
"""

import csv # from csv import *
from csv import csvreader
# installing library "pip install graphviz" - pip install modulename

#when we write import it import the full module and to call the function or variable we need the module name
import source11
source11.func_test1()

#when we write from modulename import * we can directly call the function without the module name
from source_test import *
func_test1()


#Here __init__.py is a file that will bydefault created when we create a package. so test_package is my package and I need to keep the modules inside the package so that I can import the package and can use all the modules.
import test_package
test_package.func_test11() 


