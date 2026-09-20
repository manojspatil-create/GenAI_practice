# list =============================================================================
print()
print("1: Lists — Ordered, Mutable Collection ==============")
my_list = [1, "hello", 3.5, True]
print(my_list)

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Indexing (same as Java arrays — 0-based)
print(fruits[0])      # apple
print(fruits[-1])     # cherry (negative index = from the end)

# Slicing — [start:stop:step]
print(fruits[0:2])    # ['apple', 'banana']  -> stop index is EXCLUDED
print(fruits[::-1])   # ['cherry', 'banana', 'apple']  -> reversed list

# append() — add to the end (like Java's ArrayList.add())
fruits.append("mango")
print(fruits)          # ['apple', 'banana', 'cherry', 'mango']

# pop() — remove and RETURN the last item (or item at given index)
last_item = fruits.pop()
print(last_item)       # mango
print(fruits)           # ['apple', 'banana', 'cherry']

# sort() — sorts IN PLACE (modifies original list, returns None)
nums = [5, 2, 9, 1]
nums.sort()
print(nums)             # [1, 2, 5, 9]

nums.sort(reverse=True)
print(nums)             # [9, 5, 2, 1]

# tuples ===========================================================================
print()
print("2: Tuples — Ordered, Immutable ==================")

coordinates = (10, 20 , 10, 30)
print(coordinates)

person = ("Manoj", 29, "India")
print(person)
print(person[2])

# Creating a tuple — parentheses (optional but common)
point = (10, 20)
print(point)          # (10, 20)
print(type(point))    # <class 'tuple'>

# Indexing works just like lists
print(point[0])       # 10

# Immutability — this will ERROR
# point[0] = 99        # TypeError: 'tuple' object does not support item assignment

# Use case 1: Tuple as a dictionary key
locations = {
    (19.99, 73.78): "Nashik",
    (28.61, 77.20): "Delhi"
}
print(locations[(19.99, 73.78)])   # Nashik

# Use case 2: Returning multiple values from a function
def get_min_max(numbers):
    return min(numbers), max(numbers)   # this is secretly a tuple: (min, max)

low, high = get_min_max([4, 9, 1, 7])   # tuple unpacking
print(low, high)       # 1 9

# Single-element tuple needs a trailing comma!
single = (5,)
not_a_tuple = (5)      # this is just an int in parentheses!
print(type(single))       # <class 'tuple'>
print(type(not_a_tuple))  # <class 'int'>

# Dictionaries =================================================================
print()
print("3: Dicts — Key-Value Store =========================")
person = {"name":"Manoj", "age": 29, "Location":"Pune"}
print(person)


# Access values
# You access the value using its key:
print(person["name"])
person["name"] = "Manji"
print(person)

# Creating a dict
person = {"name": "Manoj", "age": 30, "role": "learner"}

# Accessing values
print(person["name"])         # Manoj

# .get() — SAFER than [] because it won't crash if key is missing
print(person.get("email"))            # None (no error!)
print(person.get("email", "N/A"))     # N/A (default value if missing)
# print(person["email"])              # This would raise KeyError!

# update() — add new key OR modify existing key
person.update({"age": 31, "city": "Nashik"})
print(person)   # {'name': 'Manoj', 'age': 31, 'role': 'learner', 'city': 'Nashik'}

# Adding a single key directly
person["email"] = "manoj@example.com"

# .keys(), .values(), .items()
print(person.keys())     # dict_keys(['name', 'age', 'role', 'city', 'email'])
print(person.values())   # dict_values(['Manoj', 31, 'learner', 'Nashik', 'manoj@example.com'])

# .items() — most commonly used for looping through a dict
for key, value in person.items():
    print(f"{key}: {value}")
# name: Manoj
# age: 31
# role: learner
# city: Nashik
# email: manoj@example.com


# Sets ========================================================================
print()
print("4: Sets ============================")
numbers = {1, 2, 3, 4, 5}
print(numbers)

numbers = {1, 2, 3, 4, 5, 1, 2}         #remove duplicate elements 
print(numbers)

numbers = {1, 2, 3, 4, 5, 1, 2}         #
numbers.add(10)
numbers.remove(2)
print(numbers)


# Creating a set — curly braces, no key:value (that would be a dict!)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Duplicates auto-removed
nums = [1, 2, 2, 3, 3, 3]
unique_nums = set(nums)
print(unique_nums)     # {1, 2, 3}

# union() — all elements from both sets (no duplicates)
print(a.union(b))      # {1, 2, 3, 4, 5, 6}
print(a | b)            # same thing, operator style

# intersection() — elements common to both
print(a.intersection(b))   # {3, 4}
print(a & b)                # same thing

# difference() — elements in 'a' but NOT in 'b'
print(a.difference(b))     # {1, 2}
print(a - b)                 # same thing

# add() / remove()
a.add(10)
a.remove(1)
print(a)    # {2, 3, 4, 10}

# Membership check — very fast (O(1) average), unlike list's O(n)
print(3 in a)     # True

############################# END ########################################