# Exercise 2.15
"""Script that inputs three different floating-point numbers 
from the user and displays the numbers in increasing order."""

num1 = float(input("Enter 1: "))
num2 = float(input("Enter 2: "))
num3 = float(input("Enter 3: "))

largest = 0.00
middle = 0.00
last = 0.00


if num1 > num2 and num1 > num3:
    largest = num1
    
elif num2 > num1 and num2 > num3:
    largest = num2
    
elif num3>num1 and num3 > num2:
    largest = num3
    

print(largest)

""" Solution
number1 = float(input('Enter first number: '))
number2 = float(input('Enter first number: '))
number3 = float(input('Enter first number: '))

if number1 < number2 < number3:
    print(number1, number2, number3)

if number1 < number3 < number2:
    print(number1, number3, number2)

if number2 < number1 < number3:
    print(number2, number1, number3)

if number2 < number3 < number1:
    print(number2, number3, number1)
    
if number3 < number1 < number2:
    print(number3, number1, number2)

if number3 < number2 < number1:  
    print(number3, number2, number1)

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
