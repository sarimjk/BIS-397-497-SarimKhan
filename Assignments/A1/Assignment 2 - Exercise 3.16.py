# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:49:25 2020
@author: skhan
"""
"""
3.16 (Nested Control Statements) Use a loop to find the two largest values
 of 10 numbers entered.
"""

array = []
largest = int
secondlargest = int


for num in range(1,3):
    entry = int(input(f'Enter a random integer {num}: '))
    array.append(int(entry))

print(array)    
"""
array.sort()

print(array)

"""

for x in array:
   if largest == "":
       largest = x
   elif largest <= int(x):
       largest = int(x)
       
       """
   if secondlargest == "":
        secondlargest = int(x)
   elif x < largest and secondlargest < int(x):
        secondlargest = int(x)
    """
    
print(largest)
"""
print(secondlargest)
"""