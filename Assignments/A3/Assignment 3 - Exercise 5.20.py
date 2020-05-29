# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:29:04 2020

@author: skhan
"""
"""
5.20 (DISPLAY A TWO-DIMENSIONAL LIST IN TABULAR FORMAT) Define a function
 named display_table that receives a two-dimensional list and displays its 
 contents in tabular format. List the column indices as headings across the
 top, and list the row indices at the left of each row.
"""

def display_table(a):
    r = 0
    c = 0
    for row in a:

        print(r, end=' ')
        r = r+1
        
        """
        for item in row:
            print(item, end=' ')
        print()
        """
b =        
#b = [[10,11,12],[20,21,22],[30,31,32],[40,41,42]]

display_table(b)