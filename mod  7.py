# Gabriel Valencia
# 11/27/2022

from simple_colors import *
import math
import random

# Problem 1: Area of Circle
# A function which returns the area of a circle radius

print(red("Problem 1: Area of Circle"))
input_circle_area = int(input("Type in a radius to get a circle's area: "))

def areaOfCircle(r):
    circle_area = radius * radius * 3.14
    return circle_area

radius = input_circle_area
print("Your raidus =",green(input_circle_area))
print(green(input_circle_area),"*",green(input_circle_area),"*",green("pi(3.14)"))
print("The area is",green(round((areaOfCircle(radius)))))

print("")
# Problem 2: Check Range
# A function to check whether a number is in a given range
print(red("Problem 2: Check Range"))

print("Is 9 in range of 1 to 10")
def test_range(n):
    if n in range(1,10):
        print("%s is in range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(8)
print("")
# Problem 3: Multiply List
# Write a function that multiplies all numbers in a list
print(red("Problem 3: Multiply List"))

list = [5,2,7,-1]

def mult_list(list):
    product = 1
    for x in list:
        product = product * x
    return product
print(green(mult_list(list)))
print("")

# Problem 4: Unique
# Write a function that returns the list with unique elements
print(red("Problem 4: Unique"))

list = [1,3,3,3,6,2,3,5]

def list_uni(list_uni):
  x = []
  for a in list_uni:
    if a not in x:
      x.append(a)
  return x
print(list_uni([1,2,3,3,3,3,4,5]))

print("")
# Problem 6: Class Car
print(red("Problem 6: Class Car"))

class car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

def get_model(self):
    return self.model

def get_year(self):
    return self.year

def get_color(self):
    return self.color

def fullspecs(self):
    return self.model + ' ' + str(self.year) + ' ' + self.color

car1 = car("Sports", 2012, "Blue")
car2 = car("Sedan", 2020, "Black")
car3 = car("Truck", 2010, "Green")
car4 = car("Convertible", 2022, "Gray")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())
print(car3.get_color())
print(car3.get_model())
print(car4.get_color())
print(car3.fullspecs())
print(car4.fullspecs())