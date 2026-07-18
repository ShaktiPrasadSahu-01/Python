# 1. Write a program that:
# Asks the user to enter two numbers
# Adds and multiplies them
# Prints both results

a,b=input("Enter two numbers separated by space: ").split()
sum_result = int(a) + int(b)
product_result = int(a) * int(b)
print(f"Sum: {sum_result}, Product: {product_result}")


# 2. Introduce an error:
# Try adding a string and an integer
# Fix it using typecasting
a = input("Enter a number: ")
string_value = input("enter a string: ")
print(string_value + a)  # Typecasting to string to fix the error


# 3. Create a program that:
# Asks for name and age
# Prints: Hi <name>, you will be 100 years old in the year <calculated_year>
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = 2026
year_when_100 = current_year + (100 - age)
print(f"Hi {name}, you will be 100 years old in the year {year_when_100}.")


# 4. Write a buggy program that crashes, then fix it:

# --python code:--
# # Bug: input not converted to int
# age = input("Enter your age: ")
# years_left = 100 - age
# print("Years left to turn 100:", years_left)
# --python code:--
age = int(input("Enter your age:"))
years_Left = 100 - age  # Fixed by converting input to int
print(f"Years left to turn 100: {years_Left}")