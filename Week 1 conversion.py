# Author: Gabriel
# Week 1 Lab
# Date: 10/4/22
# Purpose: Converts KMH into MPH

kmh = int(input("Enter km/h: ")) # This line takes a number that the user types and converts it into mph from kmh
mph =  0.6214 * kmh # This line multiplies whatever number the user inputs by .6214
print("Speed:", kmh, "KM/H = ", mph, "MPH") # This line prints the converted answer

# SIDE NOTES
# -Error whenever a symbol other than a number is typed
# -Answer is not rounded