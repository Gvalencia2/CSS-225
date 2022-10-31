# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

first_grade = int(input("What is your grade for exam one: "))
second_grade = int(input("What is your grade for exam two: "))
third_grade = int(input("What is your grade for exam three: "))

grades = first_grade + second_grade + third_grade
average = grades/3
print('')

if average >= 90:
    print("Student is passing with an A")
elif average <= 89 and average > 80:
    print("Student is passing with a B")
elif average <= 79 and average > 70:
    print("Student is passing with a C")
elif average <= 69 and average > 60:
    print("Student is passing with a D")
elif average <= 59 and average > 0:
    print("Student is failing with an F")

print("Your average grade is",round(average))