# Exercise 4.7
"""
4.7 (DATE AND TIME) Python’s datetime module contains a datetime type with a 
method today that returns the current date and time as a datetime object.
Write a parameterless date_and_time function containing the following 
statement, then call that function to display the current date and time:
    print(datetime.datetime.today())
On our system, the date and time display in the following format:
    2018-06-08 13:04:19.214180
"""

import datetime

def dateandtime():
    print(datetime.datetime.today())


dateandtime()

"""
import datetime

def date_and_time():
    print(datetime.datetime.today())

date_and_time()
"""    
##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
