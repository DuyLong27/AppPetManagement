import json

#data
data = {
    "id": 0,
    "name": "Peter",
    "birthday": "2020-01-01",
    "image": "dog.jpg",
    "type": "Dog",
    "sex": True,
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)