# Gabriel Valencia
# 12/15/22
# Final Project
# "Cain, Come Home"

from simple_colors import *
import time
import sys
import random
import os

def intro():

# displays the title
    title = "Cain, Come Home\n"
    titleCenter = title.center(50)
    print(yellow(titleCenter))
    print("CHAPTER 1: Cain's Lost\n")

    print("*Beep Beep*\n")
    time.sleep(5)
    print("*Beep Beep*\n")
    time.sleep(5)
    print("You wake up in an unknown location...")

# multiple while loops to integrate user with the dialogue
    user_choice0 = True
    while user_choice0:
        user_input0 = str(input("You check your phone and see multiple missed calls. You decide to " + (yellow("call") + " back: ")))
        if user_input0.casefold() == "call":
            user_choice0 = True
            print("\nYou call back")
            time.sleep(5)
            print("But no one answers\n")
            time.sleep(2)
            print("You notice a message sent hours ago")
            print("Mom: Please come home soon, Cain. It's getting dark. You shouldn't be alone!\n")
            break
        else:
            user_input0 = str(input("\nYou check your phone and see multiple missed calls, you should probably " + (yellow("call") + " back: ")))
            print("")

    user_choice1 = True
    while user_choice1:
        user_input1 = str(input((yellow("Cain: ") + "Mom? " + "I need to " + (yellow("text")) + " her back: ")))
        if user_input1.casefold() == "text":
            user_choice1 = True
            print("\nAs you're about to text her...")
            time.sleep(5)
            print(red("\nYou get attacked by a monster!\n"))
            time.sleep(2)
            break
        else:
            user_input0 = str(input((yellow("\nCain: ") + "Mom? " + "I need to " + (yellow("text")) + " her back: ")))
            print("")

    user_choice2 = True
    while user_choice2:
        user_input2 = str(input("You quickly " + (yellow("check")) + " your backpack for a weapon: "))
        if user_input2.casefold() == "check":
            time.sleep(2)
            user_choice2 = True
            print("\nYou are able to find a switchblade in your bag and prepare to fight back.")
            break
        else:
            user_input2 = str(input("\nYou quickly " + (yellow("check")) + " your backpack for a weapon: "))
            print("")

    user_choice3 = True
    while user_choice3:
        user_input3 = str(input("The monster charges at you. You " + (yellow("strike")) + " at the monster: "))
        if user_input3.casefold() == "strike":
            time.sleep(1)
            user_choice3 = True
            print(red("\nThe monster screams and runs away\n"))
            time.sleep(2)
            break
        else:
            user_input3 = str(input("\nThe monster charges at you. You " + (yellow("strike")) + " back: "))
            print("")

    print("You catch your breath")
    time.sleep(2)
    print(yellow("Cain: ") + "What is going on?! What was that thing? Where even am I...?")

intro()


