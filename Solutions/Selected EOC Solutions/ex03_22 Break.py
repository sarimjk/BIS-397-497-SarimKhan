# Exercise 3.22
"""
3.22 (Optional else Clause of a Loop) The while and for statements each have 
an optional else clause. In a while statement, the else clause executes when 
the condition becomes False. 
In a for statement , the else clause executes when there are no more items to
process. If you break out of a "while" or "for" that has an else, the else part 
does not execute.

Execute the following code to see that the else clause executes only if the 
 break statement does not:
    for i in range(2):
        value = int(input('Enter an integer (-1 to break): '))
        print('You entered:', value)
    
        if value == -1:
           break
    else:
        print('The loop terminated without executing the break')
        
For more information on loop else clauses, see
https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
"""

for i in range(2):
    value = int(input('Enter an integer (-1 to break): '))
    print('You entered:', value)

    if value == -1:
       break

else:
    print('The loop terminated without executing the break')



"""
for i in range(2):
    value = int(input('Enter an integer (-1 to break): '))
    print('You entered:', value)
    
    if value == -1:
        break
else:
    print('The loop terminated without executing the break')
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
