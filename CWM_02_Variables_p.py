#Problem 1 — Personal Profile ⭐ =====================================================
#Create variables for:
#Your name
#Your age
#Your height
#Whether you are learning Python (True/False)
#Then print one sentence using an f-string:
#My name is ____, I am ____ years old, my height is ____ feet, and I am learning Python: ____.


name = "Manoj"
age = 29
height = 6
is_learning_python = True

print()
print("#Problem 1 — Personal Profile ⭐ =====================================================")
print(f"My name is {name}, I am {age} years old, and my height is {height} feet."
      f" I am learning Python: {is_learning_python}.")


#Problem 2 — Shopping 🛒 =============================================================
# Create these variables:
# * product_name → "Laptop"
# * price → 75000
# * quantity → 2
# * is_available → True
# Calculate the total price:
# total = price × quantity

# Then print:
# I bought 2 Laptop(s). Total price is ₹150000. Available: True


product_name = "Laptop"
price = 75000
quantity = 2
is_available = True

total = price * quantity

print()
print("#Problem 2 — Shopping 🛒 =============================================================")
print(f"I bought {quantity} Laptop(s). Total price is {total}. Available: {is_available}")


# Problem 3 — Next Year 🎂 ============================================================
# Create:
# name = "Manoj"
# age = 29
# Print:
# print(f”Hello Manoj, you are currently {age} years old.”,
# f”Next year you will be {next_year} years old.”)

# Condition: Calculate the next year's age using Python. Don't manually write 30.

print()
name_a = "Manoj"
age_a = 29

next_year = age_a + 1

print("#Problem 3 — Next Year 🎂 ============================================================")
print(f"Hello {name_a}, you are currently {age_a} years old, " 
      f"Next year you will be {next_year} years old.")


# Problem 4 — Data Type Detective 🔍
# Create these variables:


# a = 100
# b = 10.5
# c = "100"
# d = True

# Print the value and data type of each variable.
# Expected idea:


# 100 → int
# 10.5 → float
# 100 → str
# True → bool

# Use type().

print()
a = 100
b = 10.5
c = "100"
d = True

print("#Problem 4 — Data Types 🧪 ============================================================")
print(f"{a} → {type(a).__name__}")
print(f"{b} → {type(b).__name__}")
print(f"{c} → {type(c).__name__}")
print(f"{d} → {type(d).__name__}")



name = "Manoj"
experience = 4.4
salary = 50000
learning_ai = True

print()
print("#Problem 5 — Employee Profile 🧑‍💼 =====================================================")
print(f"My name is {name}, I have {experience} years of experience and my salary is {salary}. I am Learning AI: {learning_ai} ")

next_year_experience = experience + 1
print(f"Next year I will have {next_year_experience} years of experience.")

print()
person = {"name": "Manoj", "age": 28}   # dict — key-value pairs
print(person)


my_set = {2, 1, 3, 3,1}           # set — unordered, no duplicates
print(my_set)


############################# END ########################################
