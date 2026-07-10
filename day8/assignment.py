'''
1. Given a string "machinelearning", print:
First 5 characters
Last 3 characters
The string in reverse
'''
string = "machinelearning"
print(string[:5])  # First 5 characters
print(string[-3:])  # Last 3 characters
print(string[::-1])


'''
2. Ask the user to enter their full name. Then:
Print it in uppercase
Print only the first name (assume it's before the first space)
Count how many times the letter 'a' appears
'''
name = input("Enter your full name: ")
print(name.upper())  # Print in uppercase
print("First name is: ",name[:name.find(" ")])  # Print only the first name
print("Count of 'a': ", name.count('a'))  # Count occurrences of 'a'


'''
3. Ask the user for a sentence and print each word in a new line using .split().
4. Replace all spaces in a sentence with dashes (-).
5. Challenge: Ask the user to enter a filename and check if it ends with .py — if yes, print "Python file detected", else "Not a Python file".
'''

sentence = input("Enter a sentence: ")

print(*sentence.split(), sep="\n")
sentence = input("Enter a sentence: ")

print(sentence.replace(" ", "-"))
filename = input("Enter a filename: ")

if filename.endswith(".py"):
    print("Python file detected")
else:
    print("Not a Python file")