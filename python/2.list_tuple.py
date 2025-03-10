# Advanced Python: Lists and Tuples

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide an in-depth understanding of Python lists and tuples.
We will explore:
1. Lists - Creation, accessing elements, operations, and methods.
2. Tuples - Characteristics, usage, and differences from lists.
3. Advanced applications including 1D and 2D lists, and lists with mixed data types.

Each section includes detailed explanations, examples, and challenging assignments.
"""

# Section 1: Python Lists
# -----------------------
# Lists in Python are ordered, mutable (changeable), and allow duplicate elements.

# Example 1: Creating Lists
simple_list = [8, 2, 9, 4, 5]
mixed_list = [1, "Hello", 3.14, True]
temp_list = []  # Empty list

# 2D List (List of Lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing Elements
# You can access elements by their index, which starts at 0.
first_element = simple_list[0]  # Outputs 1
second_row_first_col = matrix[1][0]  # Outputs 4

# List Operations
# Adding elements
print("Before Apprend Operation: ", simple_list)
simple_list.append(6)  # Adds 6 to the end
print("After Append operation: ", simple_list)
simple_list.insert(1, 6)  # Inserts 0 at the beginning
print("After Insert operation: ", simple_list)

# Removing elements
simple_list.remove(6)  # Removes the first occurrence of 6
print("After Remove operation: ", simple_list)
popped_element = simple_list.pop()  # Removes and returns the last element
print("Popped element:", popped_element)
print("After Pop operation: ", simple_list)

# List Methods
# Join lists
combined_list = simple_list + mixed_list
print("Combined List: ", combined_list)

# Sort lists
simple_list.sort()  # Sorts the list in place
print("Sorted List: ", simple_list)

# Copy a list
duplicate_list = simple_list

duplicate_list.append(7)
print("simple_list id", id(simple_list), "duplicate_list id: ", id(duplicate_list))
print("Duplicate List: ", duplicate_list)
print("Simple List: ", simple_list)

list_copy = simple_list.copy()
list_copy.append(8)
print("List Copy: ", list_copy)
print("Simple List: ", simple_list)

# Get the number of elements
list_length = len(simple_list)

# Assignment 1: Create a 2D list representing a 3x3 matrix and perform operations like accessing, modifying, and iterating through it.
# Write your code below:
matrix = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

# Accessing elements in the matrix
print("Element at row 1, column 2:", matrix[0][1])  # Should print 2

# Modifying an element in the matrix
matrix[1][1] = 10
print("Modified matrix:")
for row in matrix:
    print(row)

# Iterating through the matrix
print("Iterating through the matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # For a new line after each row

# Section 2: Python Tuples
# ------------------------
# Tuples are ordered collections like lists but are immutable (cannot be changed after creation).

# Example 2: Creating and Using Tuples
simple_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "Hello", 3.14, True)
temp_tuple = ()  # Empty tuple

# Accessing elements
first_tuple_element = simple_tuple[0]

# Tuples are immutable
# Trying to change an element like below will raise a TypeError
# simple_tuple[0] = 0

# Tuples can be used as keys in dictionaries because of their immutability
tuple_dict = {simple_tuple: "My Tuple"}

# Assignment 2: Create a tuple with mixed data types and demonstrate its potential use cases in data structures like dictionaries.
# Write your code below:
mixed_tuple = (1, "apple", 3.14, True)

# Demonstrating the use of the tuple in a dictionary
# Using the tuple as a key
data_dict = {
    mixed_tuple: "Sample data"
}

# Accessing the value using the tuple key
print("Value associated with the tuple key:", data_dict[mixed_tuple])

# Using the tuple as a value
another_dict = {
    "key1": mixed_tuple,
    "key2": (2, "banana", 2.71, False)
}

# Accessing the tuple value from the dictionary
print("Tuple value associated with 'key1':", another_dict["key1"])
print("Tuple value associated with 'key2':", another_dict["key2"])

# Iterating through the dictionary and printing items
print("Iterating through the dictionary:")
for key, value in another_dict.items():
    print(f"{key}: {value}")

# Section 3: Advanced Applications
# --------------------------------
# Dealing with more complex list and tuple structures for real-world applications.

# Example 3: Advanced List Operations
# Filtering with list comprehensions
# even_numbers = [x for x in simple_list if x % 2 == 0]

even_numbers = [x for x in simple_list if x % 2 ==0]

print(even_numbers)


# Nested list comprehensions for 2D list transformations
incremented_matrix = [[cell + 1 for cell in row] for row in matrix]

# Assignment 3: Create a list of tuples, where each tuple contains a student's name and their grade. Sort this list by grades.
# Write your code below:
students_grades = [
    ("Mariam", 88),
    ("Sraboni", 72),
    ("Luzain", 95),
    ("Jerin", 85),
    ("Eva", 90)
]

# Sorting the list by grades
sorted_students_grades = sorted(students_grades, key=lambda student: student[1])

# Printing the sorted list
print("Sorted list by grades:")
for student in sorted_students_grades:
    print(student)

# Congratulations on completing the advanced section on Python lists and tuples!
# Review the assignments, try to solve them, and check your understanding of these versatile data structures.
