# Exercise 4.10
"""
4.10 (GUESS THE NUMBER) Write a script that plays “guess the number.” Choose
 the number to be guessed by selecting a random integer in the 
 range 1 to 1000. Do not reveal this number to the user. Display the prompt
 "Guess my number between 1 and 1000 with the fewest guesses:". The player 
 inputs a first guess. If the guess is incorrect, 
 display "Too high. Try again." or "Too low. Try again." as appropriate to 
 help the player “zero in” on the correct answer, then prompt the user for
 the next guess. When the user enters the correct answer, 
 display "Congratulations. You guessed the number!", and allow the user to 
 choose whether to play again.
"""

import random

def randnum():
    return random.randrange(1,1001)


Correct = False
Newgame = False

def newgame():
    number = randnum()
    print(number)
    return number

    
number = newgame()


while Correct == False or Newgame == True:

    
    guess = int(input('Enter guess: '))
    
    if guess > number:
        print('Number is too high')
        
    elif guess < number:
        print('Number is too low')
        
    elif guess == number:
        print('Congrats, You guessed the number!')
        Correct  = True
        
        Newgamequest = input("Do you want to play again? Y / N: ")
        if Newgamequest == 'Y':
            Newgame = True
            number = newgame()
        else:
            Newgame = False
            print('Have a good day')
            


"""
#Guess the number.
import random

def get_number():
    #Create a new number to guess.
    return random.randrange(1, 1001)
   
def new_game():
    #Start a new game.
    return get_number()
    print('Guess a number between 1 and 1000')

def check_guess(guess, answer):
    #Check user input
    correct = False
    
    if (guess < answer):
        print(f'{guess} is too low. Try again.')
    elif (guess > answer):
        print(f'{guess} is too high. Try again.')
    else:
        correct = True 
        print('Congratulations. You guessed the number!')
        print()

    return correct

# game logic
game_over = False    
            
while not game_over:
    answer = new_game()

    correct = False
    
    while not correct:
        correct = check_guess(int(input('Guess (1 - 1000): ')), answer)

    play_again = input('Play again (yes or no)? ')

    if play_again == 'no': 
       game_over = True

print('Thanks for playing!')
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
