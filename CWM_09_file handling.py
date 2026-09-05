import json
print()
########## File handle ###############
# 1. open() with context manager

# f = open("file.txt", "r")
# f.close()

# 1. write 'w'
with open("/Users/manoj/Downloads/red.txt", "w") as f:
    f.write("Hey Bruh hows going duh")


# 2. Read 'r'
with open("/Users/manoj/Downloads/red.txt", "r") as f:
    data = f.read()
    print(data)

# 3. append 'a'

with open("/Users/manoj/Downloads/red.txt", "a") as f:
    f.write("\nNice bruh")

with open("/Users/manoj/Downloads/red.txt", "r") as f:
    data = f.read()
    print(data)

# 4. "rb" — Read Binary

# with open("/Users/manoj/Downloads/wall/255508978854295575.jpg", "rb") as f:
#     data = f.read()
#     print(data)


########## JSON file ###############

print("################ JSON FILE")

# Writing a dict to JSON file
data = {"name": "Manoj", "age": 29, "role": "GenAi Engineer"}
with open("data.json", "w") as f:
    json.dump(data, f)


# Reading JSON file back into a dict
with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded)  # {'name': 'Manoj', 'role': 'GenAI Engineer'} 
print(data["age"])  


user ={"id":1,"name": "Manji", "Location": "Pune"}

with open("user.json", "w") as f:
    json.dump(user,f)

with open("user.json", "r") as f:
    access = json.load(f)
    print(access)


########## read CSV files ###############

