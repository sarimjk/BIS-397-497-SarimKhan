"""
Created on Tue Jun  9 12:30:58 2020

@author: skhan
7.20 (PERFORMANCE ANALYSIS) In this chapter, we used %timeit to compare the 
average execution times of generating a list of 6,000,000 random die rolls vs.
 generating an array of 6,000,000 random die rolls. Though we saw 
 approximately two orders of magnitude performance improvement with array, 
 we generated the list and the array using two different random-number 
 generators and different techniques for building each collection. If you use
 the same techniques we showed to generate a one-element list and a 
 one-element array, creating the list is slightly faster. 
 Repeat the %timeit operations for one-element collections. 
 Then do it again for 10, 100, 1000, 10,000, 100,000, and 1,000,000 
 elements and compare the results on your system. The table below shows 
 the results on our system, with measurements in nanoseconds (ns), 
 microseconds (µs), milliseconds (ms) and seconds (s).


This analysis shows why %timeit is convenient for quick performance studies.
 However, you also need to develop performance-analysis wisdom. Many factors 
 can affect performance—the underlying hardware, the operating system, the 
 interpreter or compiler you’re using, the other applications running on your 
 computer at the same time, and many more. The way we thought about 
 performance over the years is changing rapidly now with big data, data 
 analytics and artificial intelligence. As we head into the AI portion of 
 the book, you’ll place enormous performance demands on your system, so it’s
 always good to be thinking about performance issues.
"""

import random
import numpy as np

lista = (1,10,100,1000,10000,100000,1000000)
timer1 = []
timer2 = []


for i in lista:
    print('\nLIST')
    print(f'Avg exec time for {i} value(s)')
    %timeit oneellist = [random.randrange(i)]
    
    print('\nARRAY')
    print(f'Avg exec time for {i} value(s)')
    %timeit onearray = np.random.randint(1,2,i)



    
    
  


