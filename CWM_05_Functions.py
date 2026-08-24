# 1. Creating a Function ============================================================================================================

def say_hi():
    print("Hello, def!")
    print("Welcome to Python Functions")

say_hi()  # Calling the function
print()  # Adding a blank line for better readability
say_hi()  # Calling the function again


#2. Function with Parameters ============================================================================================================
print()  # Adding a blank line for better readability
def say_hi(name):
    print(f"Hello, {name}!")
    print("Welcome to Python Functions")

say_hi("MAnoj")  # Calling the function with a parameter
say_hi("Manji")    # Calling the function with a different parameter  


#3. Function with Return Value ============================================================================================================
print()  # Adding a blank line for better readability
def add_numbers(a,b):  # Function with two parameters and a return value
    return a + b       

print(f"Result: {add_numbers(5,3)}")  # Printing the result of the function call

# addition_result = add_numbers(5, 3)  # Calling the function and storing the result
# print("Addition Result:", addition_result)  # Printing the result   

#4. Multiple Parameters ============================================================================================================
print()  # Adding a blank line for better readability

def multiply_numbers(a, b):
	print(a * b)
multiply_numbers(3, 6)

def introduce_yourself(name, age, location):  # Function with multiple parameters
    print(f"My name is {name} and I am {age} years old. and i live in {location}.")
introduce_yourself("Manoj", 25, "Pune")  # Calling the function with two parameters
introduce_yourself("Manji", 30, "Pune")  # Calling the function with


#5 Default Parameters ============================================================================================================
print()  # Adding a blank line for better readability
def greet(name ="Manoj"):  # Default parameter defined in the function
    print(f"Hello, {name}!")    
greet()  # Calling the function without any argument, will use the default value

#6. Keyword Arguments ============================================================================================================
print()  # Adding a blank line for better readability
def introduce_yourself(name, age, location):
     print(f"My name is {name} and I am {age} years old. and i live in {location}.")
introduce_yourself(age=25, location="Pune", name="Manoj")  # Calling the function with keyword arguments

#7. Local Variables ============================================================================================================

print()  # Adding a blank line for better readability
def greet():
    name = "Manoj"  # Local variable defined inside the function
    print(name)
greet()  # Calling the function, will print the local variable 'name'



#8. Global Variables ============================================================================================================
name = "Manoj" # Global variable defined outside the function

def greet():
     print(name)

greet()     

#8 Function Calling Another Function ============================================================================================================

def add(a, b):
    return a + b


def calculate():
    result = add(10, 20) # Calling the 'add' function and storing the result
    print(result)

calculate()


#9. Variable-Length Arguments (*args) ============================================================================================================

print()  # Adding a blank line for better readability
def add(*numbers):
    return sum(numbers)
print(add(1, 2, 3, 4, 5))
print(add(10, 20, 30))


def show(*args): # Using *args to accept variable-length arguments
     print(args)
show(1, 2, 3)


def introduce_yourself(*args): # Using *args to accept variable-length arguments
     name, age, location = args # Unpacking the arguments into separate variables
     print(f"My name is {name}, and i am {age} years old, and i live in{location}.")
introduce_yourself("Manoj", 25, "Pune")  # Calling the function with two parameters
introduce_yourself("Manji", 30, "Pune")  # Calling the function with two parameters


def make_pizza(size, *toppings): # Using *toppings to accept variable-length arguments
    print(f"Making a {size}-inch pizza with:")
    for topping in toppings:     # Iterating through the toppings tuple and printing each topping
        print(f"- {topping}")

make_pizza(12, "pepperoni")
make_pizza(16, "mushrooms", "green peppers", "extra cheese")

#10. Variable-Length Keyword Arguments (**kwargs) ============================================================================================================

print()  # Adding a blank line for better readability
def introduce_yourself(**kwargs): # Using **kwargs to accept variable-length keyword arguments
    for key, value in kwargs.items(): # Iterating through the key-value pairs in the kwargs dictionary
        print(f"{key}: {value}")
introduce_yourself(name="Manoj", age=25, location="Pune")  # Calling the function with keyword arguments
introduce_yourself(name="Manji", age=30, location="Pune")  # Calling the function with keyword arguments

#11 Using *args and **kwargs Together

print()

def test(*args, **kwargs):
    print(args)
    print(kwargs)
test(10,20,30, name="Manoj", age=29)

