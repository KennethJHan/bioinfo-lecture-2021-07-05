import json

with open("data.json", "r") as handle:
    data = json.load(handle)

# print(data)

for elem in data:
    print(f"{elem['id']}\t{elem['sequence']}\t{elem['species']}")
