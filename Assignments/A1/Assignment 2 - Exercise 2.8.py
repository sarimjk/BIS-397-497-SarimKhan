# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:15:13 2020

@author: skhan
"""

# 2.8 (TABLE OF SQUARES AND CUBES) Write a script that calculates the squares
# and cubes of the numbers from 0 to 5. Print the resulting values in table 
# format, as shown below. Use the tab escape sequence to achieve the 
# three-column output.


numbers = [0, 1, 2, 3, 4, 5]

print("number\tsquare\t\tcube")

for x in numbers:
    print(f'{x:<2} \t\t {x**2:<2} \t\t {x**3:<2}')
    
    