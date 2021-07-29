#!/usr/bin/env python3
"""
Author : Leszek Grechowicz <leszek_grechowicz@o2.pl>
Date   : 29-07-2021
Purpose: Terminal based Guess the number Game
"""

from art.logo import logo
from random import randint


def check_guess():
    """checking if players input is correct(a number), prompting to enter again if not"""
    while True:
        try:
            pick_num = int(input('\t>>> '))
            return pick_num
        except ValueError:
            print("\tIt is not a number !, Please try again.")
            continue


def game():
    print("\n\tI am thinking about the number between 1 and 100, TRY ME !")
    number_to_guess = randint(1, 100)
    guess = check_guess()
    pass


def main():
    """game main loop, checking if player wants to play again"""
    print(logo)
    game_on = True
    while game_on:
        game()
        response = input("Do you want to play again? Y to CONTINUE or ANY key to QUIT >>> ")
        game_on = True if response.lower() == 'y' else False


if __name__ == '__main__':
    main()
