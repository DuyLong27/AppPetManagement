import json

#mo file de doc du lieu
with open("data.json", "r") as f:
    data = json.load(f)
    
#chinh sua voi du lieu da co san
data["name"] = "Coil"

#them du lieu moi
data["age"] = 2

#ghi lai file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)