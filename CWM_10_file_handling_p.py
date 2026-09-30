import json

# Write Python object -> JSON file
empData = {
    "name": "Manoj",
    "role": "learner",
    "team": "example-team"
}

with open("empData.json", "w") as f:
	json.dump(empData, f)

# Read JSON file -> Python object
with open("empData.json", "r") as f:
	loaded = json.load(f)

print(loaded)
print(loaded["role"])
