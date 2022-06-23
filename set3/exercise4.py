# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""

import math



def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    found = False
    tries = 0
    guess = 0
    while found == False:
        tries = tries + 1
        guess = (low + high)/2
        guess = int(guess)
        print(f"The guess is currently {guess}, the number of tries is currently {tries} ")
        if guess == actual_number:
            found = True
            print(f"{actual_number} found!")
        elif guess > actual_number:
            high = guess
            print(f"{guess} is higher than {actual_number}")
        elif guess < actual_number:
            low = guess
            print(f"{guess} is lower than {actual_number}")
        else:
            found = True
            print("this code is wrong, fix it you dumb idiot")


        

    # Write your code in here

    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
