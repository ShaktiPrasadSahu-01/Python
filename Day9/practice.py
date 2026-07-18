#1. Create a function area_of_circle(radius) that returns the area using π ≈ 3.14 and includes a docstring.

radius = float(input("Enter the radius of the circle: "))
def area_of_circle(radius):
    '''Calculate the area of a circle given its radius.'''
    pi = 3.14
    area = pi * (radius ** 2)
    return area

print(area_of_circle(radius))

# 2. Use an f-string to print:
# Name: Alice, Age: 25, Score: 89.5%
name = "Alice"
age = 25    
score = 89.5
print(f"Name: {name}, Age: {age}, Score: {score}%")


# 3. USing an fstring, write a program that takes two numbers from the user and prints:
# Sum of <a> and <b> is <sum>

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"sun of {a} and {b} is {a + b}")

# 4. Write a function is_even(num) that returns True if number is even. Add a docstring explaining the logic.
num = int(input("Enter a number: "))
def is_even(num):
    '''Check if a number is even. Returns True if the number is divisible by 2, otherwise returns False.'''
    return num % 2 == 0
print(is_even(num))

# 5. Challenge: Take name and marks as input and print a report card like(use fstring):
# Student Report:
# ---------------
# Name: Rahul
# Marks: 86.45%
# Grade: B+
Name = input("Enter student's name: ")
Marks = float(input("Enter marks: "))   
grade = input("Enter grade: ")
print(f"Student Report:\n----------------\nName: {Name}\nMarks: {Marks}%\nGrade: {grade}")
