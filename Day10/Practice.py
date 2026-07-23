# 1. Create a list of 5 cities. Then:
Cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# Add a new city at the end
Cities.append("Philadelphia")
# Insert one at the 2nd position
Cities.insert(1, "San Francisco")
# Remove the last city and print it
City_removed = Cities.pop()
print(f"Removed city: {City_removed}")
print(f"Updated list of cities: {Cities}")


# 2. Create a list of numbers: [3, 1, 4, 1, 5, 9]. Then:
numbers=[3, 1, 4, 1, 5, 9]
# Count how many times 1 appears
print(numbers.count(1))

# Sort the list
numbers.sort()
print(numbers)
# Reverse the list
numbers.reverse()
print(numbers.reverse())
# 3. Ask the user to enter 3 favorite foods (one by one), store them in a list, and print the final list.
input_foods = []
for i in range(3):
    food = input(f"Enter favorite food {i + 1}: ")
    input_foods.append(food)
print(f"Your favorite foods are: {input_foods}")

# 4. Create a list of 4 student names and:
Students = ["Alice", "Bob", "Charlie", "David"]
# Print the list in reverse (using slicing)
print(Students[::-1])
# Check if "John" is in the list
if "john" in Students:
    print("John is in the list.")
else:
    print("John is not in the list.")

# 5. Challenge:
# Create a list of even numbers from 2 to 20 using list repetition or a loop (if already covered).
even_numbers = []
for i in range(2,21,2):
    even_numbers.append(i)
print(f"Even numbers from 2 to 20: {even_numbers}")
# Store multiple student records in a nested list (e.g., ["Alice", 90])
student_records = [["Alice", 90], ["Bob", 85], ["Charlie", 92]]
for record in student_records:
    print(f"Student: {record[0]}, Marks: {record[1]}")