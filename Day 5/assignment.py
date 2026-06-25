# Task 1
Name = "Sahu"
Age = 67
Favorite_Programming_Language = "C++ and Rust"
Is_Student = False


print(f"Hello everyone,my name is {Name}")
print(f"I'm {Age} years old")
print(f"I love to code in {Favorite_Programming_Language}")

if Is_Student:
    print("I am a student")
else:
    print("I am a professional programmer")
    

#Task 2

x = 10
y = 3.14
z = x + y
print(z)
print(type(z))



#Task 3

number = "123"
if number.isdigit():
    x = int(number)
    print(f"The number is {x+10}")
else:
    print("The number is not a valid integer")
    
    
    
    
#Task 4   
# 2nmae= 30
# print(2nmae)
# my-name = "Sahu"
# print(my-name)

#Task 5
''' Can a variable store multiple data types during execution? 
Yes, in Python, a variable can store multiple data types 
during execution. For example, you can assign an integer to 
a variable and later assign a string or a list to the same 
variable. This is because Python is a dynamically typed language, 
which means that the type of a variable is determined at 
runtime and can change as needed. '''

x = 10 # Initially an integer
print(type(x)) # Output: <class 'int'>

x = "Hello" # Now a string
print(type(x)) # Output: <class 'str'>
