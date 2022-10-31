# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).


year = int(input("Greetings! What is your year of origin?: ")) #The issue here is the parentheses, quotations and = sign

if year < 1900:       #Sign was wrong, no : sign
    print ("Woah, that's the past!")  # the " is needed because 'that's' is confusing the print
elif year == 1900:
    print ("That's totally the present!")
elif year <= 2020:
    print ("That's totally the present!")    #needed one more else if for the 1900-2020 range
elif year > 2020:
    print ("Far out, that's the future!!")
