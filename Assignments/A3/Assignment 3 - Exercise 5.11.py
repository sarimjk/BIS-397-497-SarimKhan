# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:26:39 2020

@author: skhan
"""
"""
5.11 (SUMMARIZING LETTERS IN A STRING) Write a function summarize_letters 
that receives a string and returns a list of tuples containing the unique
 letters and their frequencies in the string. Test your function and display
 each letter with its frequency. Your function should ignore case sensitivity
 (that is, 'a' and 'A' are the same) and ignore spaces and punctuation. When
 done, write a statement that says whether the string has all the letters of
 the alphabet.
"""

from collections import Counter

def summarize_letters(string):
    string2 = [item.upper() for item in string]
    #result = Counter(string2)
    
    ignore = {' ','','.',',',':',';'}
    result = Counter(x for x in string2 if x not in ignore)
    print(result)
    inputlettercount = len(result)
    print(inputlettercount)
    

    #compare against alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetupper = [item.upper() for item in alphabet]
    alphabetconfirm = Counter(alphabetupper)
    print(alphabetconfirm)
    
    if inputlettercount == 26:
        print("It contains all the alphabet!")
        
    else:
        print("It does not contain all the alphabet")
    
    
    """
    if alphabetconfirm == result:
        print("It contains all the alphabet")
    else:
        print("It does not contain all the alphabet")
    """
    
    """
    if result.issuperset(alphabetconfirm):
        print("Contain all alphabet")
    else:
        print("Does NOT contain all alphabet")
    """
    
#call function
summarize_letters(input('Enter a string: '))
