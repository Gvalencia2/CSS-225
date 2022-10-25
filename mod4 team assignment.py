from simple_colors import *

print("Choose an activity from the list of options below:")

print('')

print("1. Learn Python")
print("2. Learn Java")
print("3. Go Swimming")
print("4. Have Dinner")
print("5. Go To Bed")
print("0. EXIT")

print('')

users_choice = int(input("Type in a number associated with the activity that you want: "))

if users_choice == 1:
    print("You have decided to learn Python!")
elif users_choice == 2:
    print("You have decided to learn Java!")
elif users_choice == 3:
    print("You will go swimming today.")
elif users_choice == 4:
    print("You have decided to have dinner.")
elif users_choice == 5:
    print("You have decided to go to bed. Goodnight.")
elif users_choice == 0:
    print(red("EXITING PROGRAM"))
else:
    print("Invalid option.")