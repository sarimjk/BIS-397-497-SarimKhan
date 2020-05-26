# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:49:25 2020
@author: skhan
"""
"""
3.16 (Nested Control Statements) Use a loop to find the two largest values
 of 10 numbers entered.
"""
"""
array = []

for num in range(1,11):
    entry = input(f'Enter a random integer {num}: ')
    array.append(entry)

print(array)
"""    
"""
array.sort()

print(array)

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




"""

largest = 0
secondlargest = 0

for x in range(len(array)): 
    #largest
    if int(array[x]) > largest:
        largest = int(array[x])
        
        
    elif int(array[x]) <= largest:
        largest = largest
        
    else:
        largest = 5
       
        
    #second largest
    if int(array[x]) < largest:
        secondlargest = secondlargest
    elif int(array[x]) < largest and secondlargest < int(x):
        secondlargest = int(x)
        
        
    
print(f'Largest number is: {largest}')
print(f'Second largest number is {secondlargest}')

"""