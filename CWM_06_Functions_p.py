# 1. Greeting Function ⭐
# Create a function greet(name) that takes a person's name and prints:
# # Hello, Manoj! Welcome to Python.
# Test it with 3 different names.

def greet(name):
    print(f"Hello, {name}, Welcome to Python.")
greet("Manoj")  # Calling the function with an argument
greet("Manji")  # Calling the function with a different argument
greet("Bhau")  # Calling the function with an argument

# ============================================================================================================

# 2. Calculator Function ⭐
# Create a function:
# calculate(a, b)
# It should return the sum, difference, product, and division of the two numbers.
# Example:
# calculate(10, 5)


print()  # Adding a blank line for better readability
def calculate(a, b):
    return a + b, a - b, a * b, a / b

calculate_result = calculate(10, 5)
print(f"Sum: {calculate_result[0]}, Difference: {calculate_result[1]}, Product: {calculate_result[2]}, Division: {calculate_result[3]}")  # Printing the result of the function call
# ============================================================================================================

# 3. Default Argument ⭐
# Create a function:
# introduce(name="Guest", city="Unknown")
# It should print:
# My name is Guest and I live in Unknown.
# Test these:
# introduce()
# introduce("Manoj")
# introduce("Manoj", "Pune")
# Observe what happens in each case.

print()  # Adding a blank line for better readability
def introduce(name="Guest", city="Unknown"):
    print(f"My name is {name} and I live in {city}.")

introduce()  # Calling the function without any arguments, will use default values
introduce("Manoj")  # Calling the function with one argument, will use default value
introduce("Manoj", "Pune")  # Calling the function with both arguments

# ============================================================================================================

# 4. Student Result ⭐⭐
# Create a function:
# calculate_percentage(name, marks1, marks2, marks3)
# It should:
# Calculate total marks.
# Calculate percentage.
# Return the percentage.
# Example:
# result = calculate_percentage("Manoj", 80, 75, 90)
# print(result)


print()  # Adding a blank line for better readability
def calculate_percentage(name, marks1, marks2, marks3):
    total_marks = marks1 + marks2 + marks3
    percentage = (total_marks / 300) * 100
    return name, percentage
print(calculate_percentage("Manoj", 80, 75, 90))  # Calling the function with arguments

# ============================================================================================================

# 5. *args — Sum of Numbers ⭐⭐
# Create a function:
# calculate_sum(*args)
# It should accept any number of numbers and return their total.
# For example:
# calculate_sum(10, 20)
# calculate_sum(10, 20, 30)
# calculate_sum(5, 10, 15, 20, 25)


print()  # Adding a blank line for better readability
def calculate_sum(*args):
    total = sum(args)
    return total
print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30))
print(calculate_sum(5, 10, 15, 20, 25))

# ============================================================================================================

# 6. *args — Find Maximum ⭐⭐
# Create:
# find_max(*numbers)
# It should accept any number of numbers and return the largest number.
# Example:
# print(find_max(10, 5, 30, 8, 20))
# Expected:
# 30



print()  # Adding a blank line for better readability
def find_max(*numbers):
        if not numbers:
            return None  # Return None if no numbers are provided
        return max(numbers)  # Return the maximum number from the provided arguments

print(find_max(10, 5, 30, 8, 20))

# ============================================================================================================


