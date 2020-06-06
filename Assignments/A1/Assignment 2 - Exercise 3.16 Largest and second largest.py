# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:49:25 2020
@author: skhan
"""
"""
3.16 (Nested Control Statements) Use a loop to find the two largest values
 of 10 numbers entered.
"""

largest = int(input("Enter number 1: "))
num = int(input("Enter number 2: "))

if num > largest:
    secondlargest = largest
    largest = num
    
else:
    secondlargest = num
    
for count in range(3,11):
    num = int(input(f"Enter number {count}: "))

    if num > largest:
        secondlargest = largest
        largest = num
    elif num > secondlargest:
        secondlargest = num
                     
print(f'Largest number is {largest} and the second largest number is {secondlargest}.')