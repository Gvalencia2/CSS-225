# Gabriel Valencia
# 12/15/22
# Final Project
# "Cain, Come Home"

from simple_colors import *
import time
import sys
import random
import os



def chapter4():

    print("\nCHAPTER 4: Home\n")

    print("You wake up light headed and blurry visioned...")
    time.sleep(5)
    print("You spend a few minutes trying to get up")
    time.sleep(5)
    print("You see your home clear in the distance\n")
    time.sleep(5)
    print(yellow("Cain: ") + "Is that.. Mom's house? But how, out here?")
    time.sleep(5)
    print("The only thing between you and home is a lake")
    time.sleep(2)
    print("There seems to be a row boat right next to you")

    user_choice01 = True
    while user_choice01:
        user_input01 = str(input("You " + yellow("walk") + " up to the row boat at the dock: "))
        if user_input01.casefold() == "walk":
            time.sleep(2)
            user_choice01 = False
            print("\nYou push the boat into the water and board it")
            break
        else:
            user_input01 = str(input("\nYou " + yellow("walk") + " up to the row boat at the dock: "))
            print("")

    user_choice02 = True
    while user_choice02:
        user_input02 = str(input("You " + yellow("row: ")))
        if user_input02.casefold() == "row":
            time.sleep(2)
            user_choice02 = False
            print(magenta("\nVoice: Cain..."))
            time.sleep(3)
            print(yellow("Cain: Hello? Who is that?\n"))
            break
        else:
            user_input02 = str(input("You " + yellow("walk") + " up to the row boat at the dock"))
            print("")

    user_choice03 = True
    while user_choice03:
        user_input03 = str(input("And " + yellow("row: ")))
        if user_input03.casefold() == "row":
            time.sleep(2)
            user_choice03 = False
            print(magenta("\nVoice: Cain... Please, come home. I miss you."))
            time.sleep(3)
            print(yellow("Cain: Mother? What is happening? Where are you?!"))
            break
        else:
            user_input03 = str(input("\nAnd " + yellow("row: ")))
            print("")

    user_choice04 = True
    while user_choice04:
        user_input04 = str(input("\nAnd " + yellow("row" + " more: ")))
        if user_input04.casefold() == "row":
            time.sleep(2)
            user_choice04 = False
            print(magenta("\nVoice: I'm sorry I didn't take care of you.."))
            time.sleep(3)
            print(yellow("Cain: I don't know what's happening. I don't know what to think anymore"))
            break
        else:
            user_input04 = str(input("\nAnd " + yellow("row") + " more: "))
            print("")

    print("You continue to row deeper into the lake")
    time.sleep(5)
    print("As you get closer to home. Everything slowly gets brighter and brighter until you can't stand it anymore")
    time.sleep(5)
    print(magenta("\nVoice: Cain, you're home."))
    print(red("END"))

chapter4()