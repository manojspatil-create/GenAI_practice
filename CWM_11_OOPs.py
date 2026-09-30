class person:
    pass

# create option
p = person()
print(p)


## constructor method 
print()
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = person("Manoj", 29)         #same constructor name as class name
print(p.name)
print(p.age)




print()
class employee:
    def __init__(self, name, location):
        self.name = name
        self.location = location

a = employee("Manoj", "Pune")
b = employee("Manji", "Pune")
c = employee("Dnyani", "Pune")
d = employee("Raj", "Indore")
e = employee("Tejas", "Pune")
f = employee("Manish", "Pune")

print(a.name)
print(a.location)

print(b.name)
print(b.location)

print(c.name)
print(c.location)

print(d.name)
print(d.location)

print(e.name)
print(e.location)

print(f.name)
print(f.location)



## Self reference to the instance
print()
class person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}!")

p = person("Manoj")
p.greet() #Hello, I am Manoj!        


