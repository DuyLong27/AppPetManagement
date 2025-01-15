import json

# mo file de doc du lieu
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)