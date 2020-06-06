# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:56:52 2020

@author: skhan
"""
"""
2.12 (7% INVESTMENT RETURN) Some investment advisors say that it’s 
reasonable to expect a 7% return over the long term in the stock market. 
Assuming that you begin with $1000 and leave your money invested, calculate 
and display how much money you’ll have after 10, 20 and 30 years. Use the 
following formula for determining these amounts:

a = p(1 + r)n
where
p is the original amount invested (i.e., the principal of $1000),
r is the annual rate of return (7%),
n is the number of years (10, 20 or 30) and
a is the amount on deposit at the end of the
nth year.

"""

r = .07
a = 1000

print (f'Year \t Amount')

list = [10,20,30]
for n in list:
    a = a * (1 + r) ** n
    print('%0.0f \t\t $%0.2f' %(n, a))
    a = 1000

    