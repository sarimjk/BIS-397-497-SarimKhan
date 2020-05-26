# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:00:18 2020

@author: skhan

"""

# Modify the script of Fig 3.3.  to validate its inputs. For any input, 
# if the value entered is other than 1 or 2, keep looping until the user 
# enters a correct value. Use one counter to keep track of the number of 
# passes, then calculate the number of failures after all the user’s inputs
# have been received.

# 1 # fig03_03.py
# 2 """Using nested control statements to analyze examination results."""
# 3
# 4 # initialize variables
# 5 passes = 0  # number of passes
# 6 failures = 0  # number of failures
# 7
# 8 # process 10 students
# 9 for student in range(10):
#10     # get one exam result
#11     result = int(input('Enter result (1=pass, 2=fail): '))
#12
#13     if result == 1:
#14         passes = passes + 1
#15     else:
#16         failures = failures + 1
#17
#18 # termination phase
#19 print('Passed:', passes)
#20 print('Failed:', failures)
#21
#22 if passes > 8:
#23     print('Bonus to instructor')



"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

# process 10 students
for student in range(11):
    # get one exam result
    
    correct = 1    #ensure either 1 or 0 are entered. 1 means incorrect
    result = int(input(f' Enter result {student} (1=pass, 2=fail): '))
    #check for null
  
    
    while correct == 1:
        if result != 1 and result !=2 :  
            result = int(input(f'Enter correct value for {student} (1=pass, 2=fail): '))
        
        else:
            correct = 0
            
    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')