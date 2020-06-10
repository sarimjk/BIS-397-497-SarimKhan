# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:29:06 2020

@author: skhan

7.9 (INDEXING AND SLICING ARRAYS) Create an array containing the values 1–15,
 reshape it into a 3-by-5 array, then use indexing and slicing techniques to 
 perform each of the following operations:

a. Select row 2.
b. Select column 4.
c. Select rows 0 and 1.
d. Select columns 2–4.
e. Select the element that is in row 1 and column 4.
f. Select all elements from rows 1 and 2 that are in columns 0, 2 and 4.
"""

import numpy as np
array1 = np.arange(1,16).reshape(3,5)

print(array1)


#a
print('\nSelect Row 2:')
print(array1[1])

#b
print('\nSelect Col 4:')
print(array1[:,4])

#c
print('\nSelect rows 0 and 1:')
print(array1[[0,1]])

#d
print('\nSlect  columns 2-4')
print(array1[:,2:5])

#e
print('\nSelect element in row 1 and column 4')
print(array1[1,4])

#f
print('\nSelect all elements from rows 1 and 2 that are in columns 0,2, and 4:')
print(array1[1:3,0:5:2])
