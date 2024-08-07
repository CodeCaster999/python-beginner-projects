"""

Coin Flip
This is a Python program used to simulate a coin toss, in which a user is asked to pick a side (heads or tails),
and the program selects a result at random between the two options. If the user's choice matches the result,
they win the coin toss.

How to Play 1) When the program is initiated, you will be prompted to choose either "heads" or "tails". 2) The
program will then determine the winning result by random chance, and display it. 3) If your choice matches the
result, you win the coin toss. If not, you'll receive a "OOF" message to indicate a loss. 4) After the end of each
round, you will be asked if you want to play again. Type "yes" to continue playing or "no" to exit the program.

Enjoy!

"""

import random

coin_side = ["heads", "tails"]
game_on = True # This is for the coin toss game
play_again_menu = False # This is if the user wins the game


def inputConvert(sample): # Convert user input to the corresponding coin side
    if sample.lower() == "h":
        return coin_side[0]
    elif sample.lower() == "t":
        return coin_side[1]
    else:
        return None


while game_on: # This is the game
    coin_flip = random.randint(0, 1)
    answer = coin_side[coin_flip]
    print("Toss the coin! (h/t)")
    user_input = input("-> ")

    converted_input = inputConvert(user_input)

    if converted_input is None:
        print("Input Error! Type h or t")
        continue  # This skips the rest of the loop and ask for input again

    if converted_input == answer:
        play_again_menu = True
        print("YAY YOU WON\nWould you like to play again? (y/n)")
        while play_again_menu:
            user_input = input("-> ")
            if user_input.lower() == "y":
                play_again_menu = False
            elif user_input.lower() == "n":
                print("Bye!")
                game_on = False
                play_again_menu = False
            else:
                print("Input Error! Type y or n")

    else:
        print("OOF!")
        game_on = False

