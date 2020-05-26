# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:13:46 2020

@author: skhan
"""
"""
In this problem, you’ll re-create the classic race of the tortoise and the 
hare. You’ll use random-number generation to develop a simulation of this 
memorable event.

Our contenders begin the race at square 1 of 70 squares. Each square 
represents a position along the race course. The finish line is at square 
70. The first contender to reach or pass square 70 is rewarded with a pail 
of fresh carrots and lettuce. The course weaves its way up the side of a 
slippery mountain, so occasionally the contenders lose ground.

A clock ticks once per second. With each tick of the clock, your application 
should adjust the position of the animals according to the rules in the table 
below. Use variables to keep track of the positions of the animals (i.e., 
position numbers are 1–70). Start each animal at position 1 (the “starting 
gate”). If an animal slips left before square 1, move it back to square 1.
                                                             
Create two functions that generate the percentages in the table for the 
tortoise and the hare, respectively, by producing a random integer i in the
 range 1 ≤ i ≤ 10. In the function for the tortoise, perform a “fast plod” 
 when 1 ≤ i ≤ 5, a “slip” when 6 ≤ i ≤ 7 or a “slow plod” when 8 ≤ i ≤ 10.
 Use a similar technique in the function for the hare.
 
 
Begin the race by displaying
    BANG !!!!!
    AND THEY'RE OFF !!!!!

Then, for each tick of the clock (i.e., each iteration of a loop), display 
a 70-position line showing the letter "T" in the position of the tortoise 
and the letter "H" in the position of the hare. Occasionally, the contenders
will land on the same square. In this case, the tortoise bites the hare,
and your application should display "OUCH!!!" at that position. All 
positions other than the "T", the "H" or the "OUCH!!!" (in case of a 
tie) should be blank.

After each line is displayed, test for whether either animal has reached or 
passed square 70. If so, display the winner and terminate the simulation. 
If the tortoise wins, display TORTOISE WINS!!! YAY!!! If the hare wins, 
display Hare wins. Yuch. If both animals win on the same tick of the clock, 
you may want to favor the tortoise (the “underdog”), or you may want to 
display "It's a tie". If neither animal wins, perform the loop again to 
simulate the next tick of the clock. When you’re ready to run your 
application, assemble a group of fans to watch the race. You’ll be amazed 
at how involved your audience gets!

 """
 
 
from random import randint

# Initial position
tortoise = 0
hare = 0
timer = 0

# Start the race!
print('Bang!!!')
print('And they are off!!!')


# Movement during the race
while True:
    r = randint(1, 11)
    
    # tortoise's movement
    if r<= 5:
        tortoise = tortoise + 3
    elif r<=7:
        tortoise = tortoise - 6
    else:
        tortoise = tortoise + 1

    # hare's movement
    if r <= 2:
        hare = hare
    elif r <= 4:
        hare = hare + 9
    elif r <= 5:
        hare = hare - 12
    elif r <= 8:
        hare = hare + 1
    else:
        hare = hare - 1
    
    
    
    


    
    # Creating the table
    t=[]
    t[2] = 'h'
    t[2]
    l = list(t)
    l[tortoise] = 'T'
    l[hare] = 'H'
    print(f'{l}')
 
    # if they are at same spot
    if tortoise == hare:
        l[tortoise] = ' OUCH '
    
# Winner
    if tortoise >= 70:
        print("Tortoise wins!!!YAY!!!")
        break
    elif hare >= 70:
        print("Hare wins!!!Yuch!!!")
        break
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 