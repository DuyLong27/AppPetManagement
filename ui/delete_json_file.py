import json

# mo file de doc du lieu
with open("data.json", "r") as f:
    data = json.load(f) 

# xoa mot truong du lieu
del data["age"]

# ghi lai file  
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)