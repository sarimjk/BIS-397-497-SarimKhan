# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:46:13 2020

@author: skhan
"""
"""
5.28 (INTRO TO DATA SCIENCE: SURVEY RESPONSE STATISTICS) Twenty students 
were asked to rate on a scale of 1 to 5 the quality of the food in the 
student cafeteria, with 1 being “awful” and 5 being “excellent.” Place 
the 20 responses in a list
    1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5
    
Determine and display the frequency of each rating. Use the built-in 
functions, statistics module functions and NumPy functions demonstrated 
in Section 5.17.2 to display the following response statistics: minimum, 
maximum, range, mean, median, mode, variance and standard deviation
"""

import statistics

response =  [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

for i in range(1,6):
    print(f'Students gave a {i} rating {response.count(i)} many times.')
    print()
    
print(f'Min: {min(response)}')
print(f'Max: {max(response)}')
print(f'Range: {max(response)-min(response)}')
print(f'Mean: {statistics.mean(response)}')
print(f'Median: {statistics.median(response)}')
print(f'Mode: {statistics.mode(response)}')
print(f'Variance: {statistics.variance(response)}')
print(f'Std Dev: {statistics.stdev(response)}')
