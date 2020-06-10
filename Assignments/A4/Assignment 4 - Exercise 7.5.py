# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:28:38 2020

@author: skhan
7.5 (FLATTENING ARRAYS WITH FLATTEN VS. RAVEL) Create a 2-by-3 array 
containing the first six powers of 2 beginning with 20. Flatten the array 
first with method flatten, then with ravel. In each case, display the result
 then display the original array to show that it was unmodified.
"""

import numpy as np


array5 = np.zeros(6,dtype=int).reshape(2,3)
array5
x =20
for i in range(2):
    for j in range(3):
        array5[i][j] = 2**x
        x = x+1

print('Array:\n', array5)

flattened = array5.flatten()
print('Flattened: \n',flattened)
print('Array is unchanged:\n ', array5)
print()

raveled= array5.ravel()
print('Raveled: \n', raveled)
print('Array is unchanged:\n', array5)




"""
array1 = np.array([[1048576, 2097152, 4194304],[8388608, 16777216, 33554432]])
array1
print(array1)
print()

flattened = array1.flatten()
print('Flattened: \n',flattened)
print('Array1 is unchanged:\n ', array1)
print()

raveled= array1.ravel()
print('Raveled: \n', raveled)
print('Array 1 is unchanged:\n', array1)
"""