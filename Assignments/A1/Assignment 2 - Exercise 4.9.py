# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:52:38 2020

@author: skhan
"""
"""
Implement a fahrenheit function that returns the Fahrenheit equivalent of 
a Celsius temperature. Use the following formula:

F = (9 / 5) * C + 32

Use this function to print a chart showing the Fahrenheit equivalents of 
all Celsius temperatures in the range 0–100 degrees. Use one digit of 
precision for the results. Print the outputs in a neat tabular format.
"""


def Far(C):
    return (9/5) * C + 32

print(f'C \t\t\t F')

for celsius in range(0,101):
    farenheit = Far(celsius)
    #print('%.0f \t\t  %0.1f' %(celsius, farenheit))
    
    if celsius < 100:
        print('%.0f \t\t  %0.1f' %(celsius, farenheit))
    else:
        print('%.0f \t  %0.1f' %(celsius, farenheit))


