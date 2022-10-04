# Author: Gabriel
# Week 1 Lab
# Date: 10/4/22
# Purpose: This program presents a login page locked behind a username/password

username = input("Login: >> ") # This line detects what the user has typed next to "Login:"
user1 = "Jack" # Lines 7-8 are the only two possible usernames that the user has to type to get access
user2 = "Jill"
if username == user1: # Lines 9-12 are the messages that the user will get if they type one of the two answers
    print("Access granted")
elif username == user2:
    print("Welcome to the system")
else:
    print("Access denied") # This line will display a message if the user types an incorrect answer

# SIDE NOTES
# -Username is case sensative