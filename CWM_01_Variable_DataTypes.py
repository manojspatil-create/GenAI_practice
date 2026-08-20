# ==========================================
# Python Variables & Data Types - Example
# ==========================================

# 1. STRING (str)
# Used to store text
name = "Manoj"

# 2. INTEGER (int)
# Used to store whole numbers
age = 29

# 3. FLOAT (float)
# Used to store decimal numbers
height = 5.11

# 4. BOOLEAN (bool)
# Can have only two values: True or False
is_learning_python = True


# ==========================================
# Printing the values
# ==========================================
print()
print(name)
print(age)
print(height)
print(is_learning_python)


# ==========================================
# Checking the DATA TYPE of each variable
# ==========================================
print()
print(type(name))               # str
print(type(age))                # int
print(type(height))             # float
print(type(is_learning_python)) # bool


# ==========================================
# Using F-STRING
# ==========================================
# f-string allows us to put variables
# directly inside a string using { }
print()
print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My height is {height} feet.")
print(f"Am I learning Python? {is_learning_python}")


# ==========================================
# Using an expression inside an f-string
# ==========================================

# Python can perform calculations inside { }

next_year_age = age + 1
print()
print(f"Next year I will be {next_year_age} years old.")


# ==========================================
# Combining EVERYTHING into one sentence
# ==========================================
print()
print(
    f"My name is {name}, I am {age} years old, "
    f"my height is {height} feet, "
    f"and I am learning Python: {is_learning_python}."
)