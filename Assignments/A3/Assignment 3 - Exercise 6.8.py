# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:39:49 2020

@author: skhan
"""
"""
6.8 (CHALLENGE: WRITING THE WORD EQUIVALENT OF A CHECK AMOUNT) In 
check-writing systems, it’s crucial to prevent alteration of check 
amounts. One common security method requires that the amount be written
 in numbers and spelled out in words as well. Even if someone can alter 
 the numerical amount of the check, it’s tough to change the amount in
 words. Create a dictionary that maps numbers to their corresponding word
 equivalents. Write a script that inputs a numeric check amount that’s 
 less than 1000 and uses the dictionary to write the word equivalent of 
 the amount. For example, the amount 112.43 should be written as
     ONE HUNDRED TWELVE AND 43/100
 
"""
def convert(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: 
            return d[num] #tens defined in d
        else: 
            return d[num // 10 * 10] + ' ' + d[num % 10] #floor division  in first and then remainder

    if (num < 1000):
        if num % 100 == 0: 
            return d[num // 100] + ' hundred'
        else:
            return d[num // 100] + ' hundred ' + convert(num % 100)

 
amount = input("Amount on check: $")
split = amount.split('.') #separate before and after decimal point
if len(split)==2 : #if there is a decimal value
   print(convert(int(split[0])).upper(),"AND",split[1],"/ 100")

else : #if there is no decimal value
   print(convert(int(split[0])).upper())