# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:01:39 2020

@author: skhan
"""
"""
Write me a script that creates a function called descriptive, which, when 
passed a list of numbers, will return the mean, median, sample standard 
deviation, and population standard deviation, along with appropriate titles.
 For example:

Mean is: 45.5666
Median is: 23.4589
...and so forth

Put your function in a script and also have the script call the function on 
a set of 10 random numbers to show me that it works.

Please both submit your script as an attachment to this question AND push 
it up to your repo, naming it "Midterm12.py"
"""

import random
import statistics as stat


def descriptive(values):
    Average = sum(values) / len(values)
    Median = stat.median(values)
    Stddev = stat.stdev(values)
    Popstddev = stat.pstdev(values)
    return print(f'Mean is: {Average:0.4f} \nMedian is: {Median:0.4f} \
                 \nSample standard deviation is: {Stddev:0.4f} \
                 \nPopulation standard deviation is: {Popstddev:0.4f}')



definedlist = []

for number in range(10):
    n = random.randint(1,1000)
    definedlist.append(n)

print(f'Numbers include: {definedlist}')
print()

descriptive(definedlist)

