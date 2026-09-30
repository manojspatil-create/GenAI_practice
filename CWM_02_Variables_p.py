#Problem 1 — Learner Profile ⭐ =====================================================
#Create variables for:
#Your name
#Your practice score
#Whether you are learning Python (True/False)
#Then print one sentence using an f-string:
#My name is ____, my practice score is ____, and I am learning Python: ____.


name = "Manoj"
score = 85
is_learning_python = True

print()
print("#Problem 1 — Learner Profile ⭐ =====================================================")
print(f"My name is {name}, my practice score is {score}."
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


# Problem 3 — Next Score 🎂 ============================================================
# Create:
# name = "Manoj"
# score = 85
# Print a greeting and the next score using Python (do not hard-code 86).

print()
name_a = "Manoj"
score_a = 85

next_score = score_a + 1

print("#Problem 3 — Next Score 🎂 ============================================================")
print(f"Hello {name_a}, your current practice score is {score_a}, "
      f"Next exercise your score will be {next_score}.")


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
modules_completed = 5
learning_ai = True

print()
print("#Problem 5 — Learner Profile 🧑‍💼 =====================================================")
print(f"My name is {name}, I have completed {modules_completed} modules. I am Learning AI: {learning_ai} ")

next_modules = modules_completed + 1
print(f"After the next lesson I will have completed {next_modules} modules.")

print()
person = {"name": "Manoj", "role": "learner"}   # dict — key-value pairs
print(person)


my_set = {2, 1, 3, 3,1}           # set — unordered, no duplicates
print(my_set)


############################# END ########################################
