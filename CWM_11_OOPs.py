class person:
    pass

# create option
p = person()
print(p)


## constructor method
print()
class person:
    def __init__(self, name, language):
        self.name = name
        self.language = language

p = person("Manoj", "Python")         # same constructor name as class name
print(p.name)
print(p.language)



print()
class employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

a = employee("Manoj", "learner")
b = employee("Alice", "developer")
c = employee("Bob", "tester")
d = employee("Carol", "developer")
e = employee("Dave", "learner")
f = employee("Eve", "developer")

print(a.name)
print(a.role)

print(b.name)
print(b.role)

print(c.name)
print(c.role)

print(d.name)
print(d.role)

print(e.name)
print(e.role)

print(f.name)
print(f.role)



## Self reference to the instance
print()
class person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}!")

p = person("Manoj")
p.greet() #Hello, I am Manoj!
