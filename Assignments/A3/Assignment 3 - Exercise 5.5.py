# -*- coding: utf-8 -*-
"""
5.5 (IPYTHON SESSION: SLICING) Create a string called alphabet containing
 'abcdefghijklmnopqrstuvwxyz', then perform the following separate 
 slice operations to obtain:

The first half of the string using starting and ending indices.
The first half of the string using only the ending index.
The second half of the string using starting and ending indices.
The second half of the string using only the starting index.
Every second letter in the string starting with 'a'.
The entire string in reverse.
Every third letter of the string in reverse starting with 'z'.
"""

string = 'abcdefghijklmnopqrstuvwxyz'

#The first half of the string using starting and ending indices.
print(string[0:13])  #m and n are midway

#The first half of the string using only the ending index.
print(string[:13])

# The second half of the string using starting and ending indices.
print(string[13:27])

#The second half of the string using only the starting index.
print(string[13:])

#Every second letter in the string starting with 'a'.
print(string[::2])

#The entire string in reverse.
print(string[::-1])

#Every third letter of the string in reverse starting with 'z'.
print(string[::-3])

