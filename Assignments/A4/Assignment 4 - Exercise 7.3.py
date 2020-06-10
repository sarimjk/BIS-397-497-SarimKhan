# -*- coding: utf-8 -*-

"""
7.3 (ELEMENT-WISE ARRAY MULTIPLICATION) Create a 3-by-3 array containing the 
even integers from 2 through 18. Create a second 3-by-3 array containing the 
integers from 9 down to 1, then multiply the first array by the second.

"""
import numpy as np

array1 = np.arange(2,19,2).reshape(3,3)
array1
print(array1)
print()

array2 = np.arange(9,0,-1).reshape(3,3)
array2
print(array2)
print()

array3= array1 * array2
print(array3)