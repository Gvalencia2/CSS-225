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
import ch2

def chapter3():

    paths = ["elevator", "stairs"]
    key = ["key"]

    print("\nCHAPTER 3: The apartments\n")

    print("The building appears to be completely empty. Maybe if you make your way to the top you could climb out")

    user_choice8 = True
    while user_choice8:
        user_input8 = str(input("There is an " + (yellow("elevator") + " and a " + (yellow("staircase") + ". Which path will you choose?: "))))
        if user_input8.casefold() == "elevator":
            time.sleep(2)
            user_choice8 = False
            print("\nYou go to press the button for the elevator")
            time.sleep(4)
            print("Nothing. The elevator seems to be completely out of service.")
            time.sleep(3)
            print("The stairs seem like the only way up")
            time.sleep(5)
            break
        if user_input8.casefold() == "staircase":
            time.sleep(2)
            user_choice8 = False
            print("\nYou choose to go up the stairs.")
            time.sleep(5)
            print
            break
        else:
            user_input8 = str(input("There is an " + (yellow("elevator") + " and an " + (yellow("elevator") + ". Which path will you choose?: "))))
            print("")

    print("You make your way up to the third floor and find the rooftop door\n")
    time.sleep(2)

    user_choice8 = True
    while user_choice8:
        user_input8 = str(input("You go to " + (yellow("open")) + " the door: "))
        if user_input8.casefold() == "open":
            time.sleep(2)
            user_choice8 = False
            print(yellow("Cain: ") + "Of course. Closed.")
            print(yellow("Cain: ") + "I need to find a key.\n")
            break
        else:
            user_input8 = str(input("\nThere is an " + (yellow("elevator") + " and an " + (yellow("elevator") + ". Which path will you choose?: "))))
            print("")

    print("You should search the surrounding rooms.")
    print("Which room will you search first?\n")
    print(yellow("1) ") + "First room\n" + yellow("2) ") + "Second room\n")

    yellow1 = (yellow("1) "))
    yellow2 = (yellow("2) "))
    yellow3 = (yellow("3) "))
    yellowEX = (yellow("4) "))

    user_choice8 = True
    while user_choice8:
        user_input8 = int(input("Room: "))
        if user_input8 == 1:
            time.sleep(2)
            user_choice8 = False
            print("\nYou enter the first room")
            print("What will you search?\n")
            print(yellow1 + "Drawer\n" + yellow2 + "Bed\n" + yellow3 + "Jacket\n" + yellowEX + "Leave the room\n")
            room1 = int(input("Action: "))
            break
        if user_input8 == 2:
            time.sleep(2)
            user_choice8 = True
            print("\nYou enter the second room")
            break
        else:
            user_input8 = int(input("Room: "))
            print("")

    user_choice9 = True
    while user_choice9:
        if room1 == 1:
            time.sleep(2)
            user_choice9 = True
            print("The drawer is empty. Just a used medical syringe and some loose change")
            print(yellow("Cain: ") + "No key in here.\n")
            room1 = int(input("Action: "))
        if room1 == 2:
            time.sleep(2)
            user_choice9 = True
            print("There is nothing on the bed or underneath")
            print(yellow("Cain: ") + "Just dirty sheets.\n")
            room1 = int(input("Action: "))
        if room1 == 3:
            user_choice9 = True
            print("The jacket does not have any key on it")
            print(yellow("Cain: ") + "Nothing.\n")
            room1 = int(input("Action: "))
        if room1 == 4:
            user_choice9 = False
            print("You leave the room\n")
            print("You have another room to check")
            print("You go into the next room\n")
            user_inputLeave1 = int(input("Room: "))
            break

        user_inputLeave1 = True
        if user_inputLeave1 == 1:
            print("What will you search?\n")
            print(yellow1 + "Desk\n" + yellow2 + "Backpack\n" + yellow3 + "Wallet\n" + yellowEX + "Leave the room\n")
        if user_inputLeave1 == 1:
            print(green("You find a bright yellow key!"))
            print(yellow("Cain: ") + "Finally. The key.\n")
            break
        if user_inputLeave1 == 2:
            print(green("The backpack is empty. It has a foul odor."))
            print(yellow("Cain: ") + "This.. Doesn't smell too good.\n")
        if user_inputLeave1 == 3:
            print(green("The wallet only has a small note inside it."))
            print(yellow("Cain: ") + "543-214.. Hm. That's the number from earlier.\n")
        if user_inputLeave1 == 4:
            print("")

        print("You go up to the door to open it.")
        time.sleep(5)
        print("As you open the door and go through a monster charges at you and launches itself through the window with you")
        time.sleep(5)
        print("You scream as everything goes blank")

chapter3()