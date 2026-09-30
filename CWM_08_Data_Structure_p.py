#1

users = [
    {"id": 101, "name": "Alice", "role": "developer", "skills": ["Python", "SQL"]},
    {"id": 102, "name": "Bob", "role": "developer", "skills": ["Python", "AWS"]},
    {"id": 103, "name": "Carol", "role": "tester", "skills": ["Python", "SQL"]},
    {"id": 104, "name": "Dave", "role": "developer", "skills": ["Java", "SQL"]},
]

"""
Write a program that:

1.Prints the names of all developers.
2.Prints the names of all tester.
3.Finds all unique skills across all users.
4.Counts how many users have "Python".
5.Creates a dictionary containing:

"""
#1
print()
print("# Prints the names of all developers:")
for user in users:
    if user["role"] == "developer":
        print(user["name"])


#2
print()
print("# Prints the names of all tester:")
for user in users:
    if user["role"] == "tester":
        print(f"{user['name']} is {user['role']}")


#3
print() 
print("# Finds all unique skills across all users:")
unique_skills = set()   

for user in users:
    unique_skills.update(user["skills"])

for skill in unique_skills:
    print(skill)

print()

