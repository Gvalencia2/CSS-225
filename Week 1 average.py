# Author: Gabriel
# Week 1 Lab
# Date: 10/4/22
# Purpose: Calculates the average of three different numbers

round1 = int(input("Enter score for round 1: ")) # Lines 6-8 Log the numbers typed by the user
round2 = int(input("Enter score for round 2: "))
round3 = int(input("Enter score for round 3: "))
average = (round1 + round2 + round3) / 3 # This line adds each number and then divides them by 3 to calculate the average
print ("the average score is: ", average) # This line prints the answer

# SIDE NOTES
# -Error whenever a symbol other than a number is typed
# -Error when using decimal points