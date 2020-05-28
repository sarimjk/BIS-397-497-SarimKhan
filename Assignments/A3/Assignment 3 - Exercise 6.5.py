# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:21:49 2020

@author: skhan
"""
"""
6.5 (COUNTING DUPLICATE WORDS) Write a script that uses a dictionary to
 determine and print the number of duplicate words in a sentence. Treat
 uppercase and lowercase letters the same and assume there is no punctuation
 in the sentence. Use the techniques you learned in Section 6.2.7. Words 
 with counts larger than 1 have duplicates.

"""

text = ('This is sample text with several words'
        'this is more sample text with some different words')

textcap = text.upper() #ignore upper and lower case

word_counts = {}

# count occurrences of each unique word
for word in textcap.split():
    if word in word_counts:
        word_counts[word] += 1 #increment count
        
    else:
        word_counts[word] = 1
        
print(f'{"WORD":<18} COUNT')

for word, count in sorted(word_counts.items()):
        print(f'{word:<20}{count}')
    
print('\nNumber of unique words: ',len(word_counts) )

"""
print("Duplicate words: ")
for word, count in word_counts.item():
    if word_counts[word] > 1:
        print(f'{word:<20}')
"""