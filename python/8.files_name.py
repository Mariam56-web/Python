# Python File I/O and JSON Handling: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to file input/output operations and JSON handling.
We will explore:
1. Reading and writing to plain text files.
2. Working with CSV files using the csv module.
3. Handling JSON data with the json module.
4. Practical examples and real-world applications.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.

# Example 1: Writing to a Text File
with open('example.txt', 'w') as file:
    file.write("Hello, Python learners!\n")
    file.write("Welcome to file I/O operations.")

# Example 2: Reading from a Text File
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Section 2: CSV Files
# --------------------
# CSV (Comma-Separated Values) files are commonly used for storing tabular data.

import csv

# Example 3: Writing to a CSV File
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 28, "New York"])
    writer.writerow(["Bob", 22, "Los Angeles"])
    writer.writerow(["Carol", 24, "Chicago"])

# Example 4: Reading from a CSV File
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Section 3: JSON Data
# --------------------
# JSON (JavaScript Object Notation) is a lightweight data-interchange format.

import json

# Example 5: Writing JSON to a File
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
with open('data.json', 'w') as file:
    json.dump(data, file)


# Example 6: Reading JSON from a File
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

# Section 4: Practical Applications
# ---------------------------------
# Combining file I/O with real-world data processing.

# Example 7: Processing JSON Data from a File
# Suppose we have a JSON file containing multiple user records.
users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 30, "email": "bob@example.com"}
]
with open('users.json', 'w') as file:
    json.dump(users, file)

with open('users.json', 'r') as file:
    users = json.load(file)
    for user in users:
        print(f"{user['name']} ({user['age']}): {user['email']}")

# Assignments
# ----------- Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.
import csv
import json

def csv_to_json(csv_file, json_file):
    # Read CSV file and convert it to a list of dictionaries
    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Write the data to a JSON file
    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Test the function
csv_file = 'products.csv'
json_file = 'products.json'
csv_to_json(csv_file, json_file)

#
# Assignment 2: 
import datetime

def write_log(log_message, log_file):
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the log message with timestamp
    log_entry = f"[{timestamp}] {log_message}\n"

    # Append the log entry to the log file
    with open(log_file, 'a') as file:
        file.write(log_entry)

# Test the function
log_message = "This is a test log message."
log_file = "log_file.txt"
write_log(log_message, log_file)


# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.
