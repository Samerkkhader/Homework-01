"""
Write a command line number guessing game.
Get user input on a number.
Give the person a hint on the number (higher or lower).
Make the maximum number be the first input to the program
"""

import random                                             # importing the random Module from python 

max_number = input("Lets play a game, i will select a number and you will guess it, but first tell me the maximum number i can choose")
# ask the user to insert input with explain messege
max_number = int(max_number)                              # convert the user input from str to int 
final_number = random.randrange(0, max_number)            # choose a random number using the random module within the range of user input

while True:                                               # adding infinite while statment
    user_guess = input("Guess a number")                  # asking the user to insert new input value                  
    user_guess = int(user_guess)                          # convert the user input from str to int  
    if user_guess > final_number :                        # adding if statment with condition (user_input) > (random value choosed above)
        print("Lower, try again")                         # if true, print this statment "Lower, try again" and start the while loop again
    if user_guess < final_number :                        # adding if statment with condition (user_input) < (random value choosed above)
        print("higher, try again")                        # if true, print this statment "Higher, try again" and start the while loop again
    if user_guess == final_number :                       # adding if statment with condition (user_input) equal to (random value choosed above)
        print("congratulations, you guessed it")          # if true, print this statment "congratulations, you guessed it"
        break                                             # if true, break the while loop
