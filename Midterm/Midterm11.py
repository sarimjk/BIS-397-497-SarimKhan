# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:30:53 2020

@author: skhan
"""
"""
One of my favorite games as a kid was Yahtzee. In case you've never played, 
the objective of the game is to score points by rolling five dice to make 
certain combinations. The dice can be rolled up to three times in a turn to 
try to make various scoring combinations.

I do not want you to program the entire game, but would like you to program 
one "turn", consisting of three dice rolls. So please make me a script that 
does the following:

1. Upon running the script, it uses a random number generator to virtually 
roll five 6-sided dice, showing the result like this:
1 3 3 2 5

2. The user is then asked to input which dice they would like to roll again,
followed by a value of "-99" to indcacte they are done choosing.  Dice are 
chose as a set of numbers corresponding to the dice positions from left to 
right. For example, continuing the depiction above, if the user wanted to 
"keep" the two "3" values, but roll the rest, they would input
"1", "4", "5", "-99". (And, yes, if you want to use an approach fro the
later chapters  have the user enter the numbers as a single string 
[e.g., "145"] without the necessity for entering [-99], that's fine: 
just direct them accordingly in your prompt). 

3. The chosen dice are re-rolled and the new, resulting set is displayed. E.g.:

4 3 3 5 3

4. Users are asked to choose for the last time which dice to roll again,
 the chose dice are redetermined randomly, and the final set of 5 dice values 
 are displayed.
"""
import random

#Roll the die

roll = []
for number in range(1,6):
    n = random.randint(1,6)
    roll.append(n)


#Show the results
print('Your die have been cast')
print('Here are the results!')
print(roll)
#print(roll1, roll2, roll3, roll4, roll5, end=' ')

reroll = []
entry = 0
print('\nFIRST TRY')
print('Only first 5 entries will be rerolled since there are only 5 die.\
      \nEnter -99 if you do not want to change anymore.')
while entry != -99:
    entry = int(input('Which die do you want to reroll?  '))
    if entry >=1 and entry <=5:
        reroll.append(entry)
    
    elif entry == -99:
        print("We will reroll the die you chose.")
        print()
    
    else:
        print("You have to choose between 1 - 5")
        print()
    


if reroll == []:
    print("You did not want to reroll any dice.")
    
else:
    print(f'You want to reroll die: {reroll[:5]}')
    
    for number in reroll:   
        roll[number-1] = random.randint(1,6)
    print("You new results are:")
    print(roll)



# Last run
reroll.clear
entry = 0
print('\nLAST TRY \nEnter -99 if you do not want to change anymore')
while entry != -99:
    entry = int(input('Which die do you want to reroll?  '))
    if entry >=1 and entry <=5:
        reroll.append(entry)
    
    elif entry == -99:
        print("We will reroll the die you chose.")
        print()
    
    else:
        print("You have to choose between 1 - 5")
        print()
    


if reroll == []:
    print("You did not want to reroll any dice.")
    
else:
    print(f'You want to reroll die: {reroll[:5]}')
    
    for number in reroll:   
        roll[number-1] = random.randint(1,6)
    print("You final results are:")
    print(roll)