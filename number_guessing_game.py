# 2. Number Guessing Game
# Description: Create a game where the computer randomly selects a number, and the user tries to guess it. The computer will give hints if the guess is too high or too low.
# Features:
#     Generate a random number between 1 and 100.
#     Allow the user to input guesses.
#     Provide feedback if the guess is too high, too low, or correct.
#     Count the number of attempts and display it when the game ends.
# Skills Practiced: Random number generation, loops, conditionals, user input/output.

import os
import random 

def main():
    random_number = random.randint(1,100)
    guess = input('Input your guess! (Good luck hehe): ')
    guess = int(guess)

    while random_number != guess:
        if guess < random_number:
            guess = input('Nope... A little HIGHER. Try again: ')
            guess = int(guess)
        
        elif guess > random_number:
            guess = input('Nope... A little LOWER. Try again: ')
            guess = int(guess)

    if guess == random_number:
        input('You did it! Congrats! Press enter to play again.')
        os.system('cls')
        main()

main()