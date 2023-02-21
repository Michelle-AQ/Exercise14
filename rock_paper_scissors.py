# import random allows me to use functions within random to randomise computuer's actions in the game

import random
# a while loop allows you to play indefinitely
# without the while loop, the code stops after you have played once

while True:
    user_action = input("Enter a choice (rock, paper, scissors):")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action},computer chose {computer_action}.\n")

# take user input - ask the user what they would like to choose as an action and then assign that choice to a variable
user_action = input("Enter a choice (rock, paper, scissors): ")
# then we need to make the user choose
# need the computer to select a random action
# random selections allow the computer to choose a pseudorandom value
# computer action is the random choice, possible actions is the user choice

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
# the above allows a random element to be selected from the list so the user can play against te computer
# below code shows the choices that the user and the computer made
# f function does ____, "\n is a line break

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
# at this point, the user and the computer have made their choice

# now need a way to decide who wins
# use an if...elif...else block - will compare players choices and determine a winner
if user_action == computer_action:  # this is asking if the user action (choice) and the computer action (choice) are the same (== means equal to_
    print (f"Both players selected {user_action}. It's a tie!")  #by starting with tie, it eliminates options
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print ("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

