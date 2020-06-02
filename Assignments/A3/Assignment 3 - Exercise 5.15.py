# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:12:29 2020
@author: skhan
"""
"""
5.15 (TUPLES REPRESENTING INVOICES) When you purchase products or services 
from a company, you typically receive an invoice listing what you purchased 
and the total amount of money due. Use tuples to represent hardware store 
invoices that consist of four pieces of data—a part ID string, a part 
description string, an integer quantity of the item being purchased and, 
for simplicity, a float item price (in general, Decimal should be used for 
monetary amounts). Use the sample hardware data shown in the following table.

PN   Description      Qty  Price
83   Electric sander  7    57.98
24   Power saw        18   99.99
7    Sledge hammer    11   21.50
77   Hammer           76   11.99
39   Jig saw           3   79.50


Perform the following tasks on a list of invoice tuples:

a. Use function sorted with a key argument to sort the tuples by part 
description, then display the results. To specify the element of the 
tuple that should be used for sorting, first import the itemgetter function 
from the operator module as in
    from operator import itemgetter
Then, for sorted’s key argument specify itemgetter( index ) where index 
specifies which element of the tuple should be used for sorting purposes.

b. Use the sorted function with a key argument to sort the tuples by price, 
then display the results.

c. Map each invoice tuple to a tuple containing the part description and 
quantity, sort the results by quantity, then display the results.

d. Map each invoice tuple to a tuple containing the part description and the 
value of the invoice (the product of the quantity and the item price), sort 
the results by the invoice value, then display the results.

e. Modify Part (d) to filter the results to invoice values in the range $200 
to $500.

f. Calculate the total of all the invoices.

"""

invoices = [('83','Electric sander',7,7.98),('24','Power saw',18,99.99),
         ('7','Sledge hammer',11,21.50),
         ('77','Hammer',76,11.99),('39','Jig saw',3,79.50)
]

from operator import itemgetter

#a. sort by description
print('A')
for ID, desc, qty, price in sorted(invoices, key = itemgetter(1)):
    print(f'{ID:<4} {desc:<20} {qty:>5} {price: 10.2f}')

#b. sort by price
print()
print('B')
for ID, desc, qty, price in sorted(invoices, key = itemgetter(3)):
    print(f'{ID:<4} {desc:<20} {qty:>5} {price: 10.2f}')

#c. Map each invoice tuple to a tuple containing the part description and 
#quantity, sort the results by quantity, then display the results.
print()
print('C')
newtupleC = [(desc, qty) for ID, desc, qty, price in invoices]

for desc, qty in sorted(newtupleC, key = itemgetter(1)):
    print(f'{desc:<15} {qty:>5}')
   
#d. Map each invoice tuple to a tuple containing the part description and the 
# value of the invoice (the product of the quantity and the item price), sort 
# the results by the invoice value, then display the results.
print()
print('D')
newtupleD = [(desc, qty*price) for ID, desc, qty, price in invoices]

for desc, valueinvoice in sorted(newtupleD, key = itemgetter(1)):
    print(f'{desc:<15} \t ${valueinvoice:<15.2f}')
    
    
#e. Modify Part (d) to filter the results to invoice values in the range $200 
#to $500.
print()
print('E')
newtupleE = [(desc, qty*price) for ID, desc, qty, price in invoices\
             if qty*price >=200 and qty*price <= 500]
    
for desc, valueinvoice in sorted(newtupleE, key = itemgetter(1)):
    print(f'{desc:<15} \t ${valueinvoice:<15.2f}')

# f. Calculate the total of all the invoices.
print()
print('F')
total = 0
for ID, desc, qty, price in sorted(invoices, key = itemgetter(3)):
    total += qty * price
print(f'Total of all invoices is: ${total:0.2f}')
