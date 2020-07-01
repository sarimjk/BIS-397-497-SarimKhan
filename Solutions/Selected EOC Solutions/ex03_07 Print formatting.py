# Exercise 3.7
"""Table of numbers, squares and cubes."""
"""3.7 (Table of Squares and Cubes) In Exercise 2.8, you wrote a script to 
calculate the squares and cubes of the numbers from 0 through 5, then printed
 the resulting values in table format. Reimplement your script using a for 
 loop and the f-string capabilities you learned in this chapter to produce 
 the following table with the numbers right aligned in each column.
"""

print("Number \t square \t cube")
for i in range(6):
    num = i
    sq = i*i
    cu = i*i*i

    print(f'{num:>6} {sq:>8} {cu:>9}')

print()




print(f'number{"square":>8}{"cube":>6}')
for i in range(6):
    print(f'{i:>6}{i ** 2:>8}{i ** 3:>6}')
   
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
