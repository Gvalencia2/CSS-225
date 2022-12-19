# Gabriel Valencia
# 12/15/22
# Final Project
# "Cain, Come Home"

from simple_colors import *
import time
import sys
import random
import os
import ch1

def chapter2():

# title
    print("\nCHAPTER 2: The code\n")

    print("You've been walking for a while now")
    time.sleep(2)
    print("You've reached a dead end and you're going to have to enter the building up ahead to find a different way out")
    time.sleep(5)

    # multiple while loops to integrate user with the dialogue
    user_choice4 = True
    while user_choice4:
        user_input4 = str(input("You approach the door and attempt to " + (yellow("open")) + " it: "))
        if user_input4.casefold() == "open":
            time.sleep(2)
            user_choice4 = True
            print("\nThe door wont budge. There is a heavy lock on the door")
            break
        else:
            user_input4 = str(input("\nYou approach the door and attempt to " + (yellow("open")) + " it: "))
            print("")

    print("You're going to have to find a code for the lock")
    time.sleep(3)
    print("You look around and see a newspaper on the ground\n")

    user_choice5 = True
    while user_choice5:
        user_input5 = str(input("You go to " + (yellow("pick")) + " it up: "))
        if user_input5.casefold() == "pick":
            time.sleep(2)
            user_choice5 = True
            break
        else:
            user_input5 = str(input("\nYou go to " + (yellow("pick")) + " it up: "))
            print("")

    print("\nThe newspaper is all ripped up and is barely readable. There is however a helpline number on it")
    print("Answers. Do you need answers? Call our number " + blue("543-214") + " and we'll help answer all of your concerns\n")

    yellowCain = yellow("Cain: ")

    newspaper = yellowCain + "Hello\n" + yellowCain + "Hello?\n" + "Voice: Follow your heart. The number. Remember the number and you shall proceed\n" + yellowCain + "What?! What are you talking about? I need help, please!"


    user_choice6 = True
    while user_choice6:
        user_input6 = int(input("You pull out your phone to call that number: "))
        if user_input6 == 543214:
            time.sleep(2)
            user_choice6 = False
            print(newspaper)
            print("Voice: 5...2...4...7")
            print(yellowCain + "Please help me")
            time.sleep(3)
            print("The phone cuts off\n")
            break
        else:
            user_input6 = int(input("\nYou pull out your phone to call that number: "))
            print("")

    time.sleep(10)
    print(yellowCain + "I really need to get out of here. I should give that code a try.")
    print("You approach the lock")

    user_choice7 = True
    while user_choice7:
        user_input7 = int(input("You input the code that the voice gave you: "))
        if user_input7 == 5247:
            time.sleep(2)
            user_choice7 = False
            print("\nThe lock opens up. and you enter the apartments.")
            break
        else:
            user_input7 = int(input("\nYou input the code that the voice gave you: "))
            print("")


chapter2()