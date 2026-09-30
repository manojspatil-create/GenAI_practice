# ==========================================
# Python Variables & Data Types - Example
# ==========================================

# 1. STRING (str)
# Used to store text
name = "Manoj"

# 2. INTEGER (int)
# Used to store whole numbers
score = 85

# 3. FLOAT (float)
# Used to store decimal numbers
temperature = 21.5

# 4. BOOLEAN (bool)
# Can have only two values: True or False
is_learning_python = True


# ==========================================
# Printing the values
# ==========================================
print()
print(name)
print(score)
print(temperature)
print(is_learning_python)


# ==========================================
# Checking the DATA TYPE of each variable
# ==========================================
print()
print(type(name))               # str
print(type(score))              # int
print(type(temperature))        # float
print(type(is_learning_python)) # bool


# ==========================================
# Using F-STRING
# ==========================================
# f-string allows us to put variables
# directly inside a string using { }
print()
print(f"My name is {name}.")
print(f"My practice score is {score}.")
print(f"The room temperature is {temperature} C.")
print(f"Am I learning Python? {is_learning_python}")


# ==========================================
# Using an expression inside an f-string
# ==========================================

# Python can perform calculations inside { }

next_score = score + 1
print()
print(f"After one more exercise my score will be {next_score}.")


# ==========================================
# Combining EVERYTHING into one sentence
# ==========================================
print()
print(
    f"My name is {name}, my practice score is {score}, "
    f"the temperature is {temperature} C, "
    f"and I am learning Python: {is_learning_python}."
)

############################# END ########################################
