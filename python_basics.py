#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python Basics Tutorial for Data Visualization
=============================================

This script provides a comprehensive introduction to Python basics
with a focus on concepts relevant to data visualization.

Topics covered:
- Variables and data types
- Operators
- Control flow
- Functions
- Data structures
- Basic data visualization

Author: Your Name
Date: Created for Data Visualization Class
"""

print("=" * 80)
print("PYTHON BASICS FOR DATA VISUALIZATION".center(80))
print("=" * 80)

# ============================================================================
# SECTION 1: VARIABLES AND DATA TYPES
# ============================================================================
print("\n1. VARIABLES AND DATA TYPES")
print("-" * 40)

# Integer
age = 25
print(f"Integer example (age): {age}, Type: {type(age)}")

# Float
temperature = 98.6
print(f"Float example (temperature): {temperature}, Type: {type(temperature)}")

# String
name = "Data Scientist"
print(f"String example (name): {name}, Type: {type(name)}")

# Boolean
is_student = True
print(f"Boolean example (is_student): {is_student}, Type: {type(is_student)}")

# None type
no_value = None
print(f"None example (no_value): {no_value}, Type: {type(no_value)}")

# Type conversion
str_number = "42"
converted_number = int(str_number)
print(f"String '{str_number}' converted to integer: {converted_number}")

# ============================================================================
# SECTION 2: OPERATORS
# ============================================================================
print("\n2. OPERATORS")
print("-" * 40)

# Arithmetic operators
a, b = 10, 3
print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

# Comparison operators
print("\nComparison Operators:")
print(f"Equal (a == b): {a == b}")
print(f"Not Equal (a != b): {a != b}")
print(f"Greater Than (a > b): {a > b}")
print(f"Less Than (a < b): {a < b}")
print(f"Greater Than or Equal (a >= b): {a >= b}")
print(f"Less Than or Equal (a <= b): {a <= b}")

# Logical operators
x, y = True, False
print("\nLogical Operators:")
print(f"x = {x}, y = {y}")
print(f"AND (x and y): {x and y}")
print(f"OR (x or y): {x or y}")
print(f"NOT (not x): {not x}")

# ============================================================================
# SECTION 3: CONTROL FLOW
# ============================================================================
print("\n3. CONTROL FLOW")
print("-" * 40)

# If-Else statements
print("If-Else Example:")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# For loops
print("\nFor Loop Example:")
print("Iterating through a range:")
for i in range(5):
    print(f"  Item {i}")

# While loops
print("\nWhile Loop Example:")
count = 0
while count < 5:
    print(f"  Count: {count}")
    count += 1

# ============================================================================
# SECTION 4: FUNCTIONS
# ============================================================================
print("\n4. FUNCTIONS")
print("-" * 40)

# Basic function
def greet(name):
    """A simple function that greets a person by name."""
    return f"Hello, {name}!"

print(f"Basic function: {greet('Data Scientist')}")

# Function with default parameters
def power(base, exponent=2):
    """Calculate the power of a number.
    
    Args:
        base: The base number
        exponent: The exponent (default is 2)
    
    Returns:
        The result of base raised to the exponent
    """
    return base ** exponent

print(f"Function with default parameter: power(5) = {power(5)}")
print(f"Function with custom parameter: power(2, 3) = {power(2, 3)}")

# Lambda functions (anonymous functions)
square = lambda x: x**2
print(f"Lambda function: square(4) = {square(4)}")

# ============================================================================
# SECTION 5: DATA STRUCTURES
# ============================================================================
print("\n5. DATA STRUCTURES")
print("-" * 40)

# Lists
print("Lists:")
fruits = ["apple", "banana", "cherry", "date"]
print(f"  Original list: {fruits}")
print(f"  First item: {fruits[0]}")
print(f"  Last item: {fruits[-1]}")
print(f"  Slicing (items 1-2): {fruits[1:3]}")

fruits.append("elderberry")
print(f"  After append: {fruits}")

fruits.remove("banana")
print(f"  After remove: {fruits}")

# Tuples (immutable)
print("\nTuples:")
coordinates = (10.5, 20.8)
print(f"  Tuple: {coordinates}")
print(f"  x-coordinate: {coordinates[0]}")
print(f"  y-coordinate: {coordinates[1]}")

# Dictionaries
print("\nDictionaries:")
student = {
    "name": "Alice",
    "age": 22,
    "courses": ["Data Science", "Statistics", "Programming"]
}
print(f"  Dictionary: {student}")
print(f"  Name: {student['name']}")
print(f"  Courses: {student['courses']}")

# Adding a new key-value pair
student["gpa"] = 3.8
print(f"  After adding GPA: {student}")

# Sets
print("\nSets:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"  Set1: {set1}")
print(f"  Set2: {set2}")
print(f"  Union: {set1 | set2}")
print(f"  Intersection: {set1 & set2}")
print(f"  Difference (Set1 - Set2): {set1 - set2}")

# ============================================================================
# SECTION 6: NUMPY BASICS (IMPORTANT FOR DATA VISUALIZATION)
# ============================================================================
print("\n6. NUMPY BASICS")
print("-" * 40)
print("To use NumPy, you need to install it first with: pip install numpy")
print("Then uncomment and run the following code:")

"""
import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {arr1}")

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:\n{arr2}")

# Array operations
print(f"\nArray + 5: {arr1 + 5}")
print(f"Array * 2: {arr1 * 2}")
print(f"Array squared: {arr1 ** 2}")

# Statistical operations
print(f"\nMean: {np.mean(arr1)}")
print(f"Sum: {np.sum(arr1)}")
print(f"Standard Deviation: {np.std(arr1)}")

# Array manipulation
print(f"\nReshaping (1D to 2D): {arr1.reshape(5, 1)}")
"""

# ============================================================================
# SECTION 7: MATPLOTLIB BASICS (DATA VISUALIZATION)
# ============================================================================
print("\n7. MATPLOTLIB BASICS")
print("-" * 40)
print("To use Matplotlib, you need to install it first with: pip install matplotlib")
print("Then uncomment and run the following code:")

"""
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot data
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linewidth=2, linestyle='--')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Line Plot: Sine and Cosine Functions')

# Add grid and legend
plt.grid(True, alpha=0.3)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()

# Bar chart example
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [15, 34, 23, 48]

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=['#5DA5DA', '#FAA43A', '#60BD68', '#F17CB0'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Basic Bar Chart Example')
plt.grid(axis='y', alpha=0.3)
plt.show()
"""

# ============================================================================
# SECTION 8: PANDAS BASICS (DATA MANIPULATION FOR VISUALIZATION)
# ============================================================================
print("\n8. PANDAS BASICS")
print("-" * 40)
print("To use Pandas, you need to install it first with: pip install pandas")
print("Then uncomment and run the following code:")

"""
import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['Data Science', 'IT', 'Marketing', 'Finance', 'HR'],
    'Salary': [72000, 67000, 53000, 81000, 63000],
    'Experience': [2, 3, 1, 5, 4]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Basic DataFrame operations
print("\nBasic DataFrame Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Accessing data
print("\nAccessing a column:")
print(df['Salary'])

print("\nAccessing a row by index:")
print(df.iloc[2])  # Third row

print("\nFiltering data:")
print(df[df['Salary'] > 70000])

# Data visualization with pandas
print("\nTo create a simple bar chart of salaries:")
# df['Salary'].plot(kind='bar', figsize=(10, 6), title='Salary Distribution')
# plt.xlabel('Employee Index')
# plt.ylabel('Salary ($)')
# plt.grid(axis='y', alpha=0.3)
# plt.tight_layout()
# plt.show()
"""

print("\n" + "=" * 80)
print("END OF PYTHON BASICS TUTORIAL".center(80))
print("=" * 80)
print("\nTo run this tutorial, use the command: python python_basics.py")
print("For the visualization sections, make sure to install the required packages and uncomment the code.")