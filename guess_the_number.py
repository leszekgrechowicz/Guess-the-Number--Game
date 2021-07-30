#!/usr/bin/env python3
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 29-07-2021
Purpose: Terminal based Guess the Number Game
"""

from art.logo import logo
from random import randint


def take_input() -> int:
    """Asking for input checking if correct and prompting to enter again if not"""
    while True:
        try:
            pick_num = int(input('\n\tGuess the number: '))
            return pick_num
        except ValueError:
            print("\tThis is not a number ! Please try again.")
            continue


def check_guess(rand_num: int):
    """Checking players number against random generated number"""
    the_same = False
    while not the_same:

        # stores player guess
        player_num = take_input()

        if player_num == rand_num:
            the_same = True

        elif player_num > rand_num:
            print("\tTo big!")
            continue

        else:
            print('\tTo small!')
            continue

    print("\tCongratulations You win!")


def play():
    """Game play"""
    print("\n\tI am thinking about the number between 1 and 100, TRY ME !")

    # stores random generated number for the player to guess:
    number_to_guess = randint(1, 100)

    check_guess(number_to_guess)


def game():
    """Main game loop, when game ends checks if player wants to play again"""
    print(logo)
    game_on = True
    while game_on:
        play()
        response = input("\nDo you want to play again? Y to CONTINUE or ANY key to QUIT >>> ")
        game_on = True if response.lower() == 'y' else False


if __name__ == '__main__':
    game()
